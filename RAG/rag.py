import os
import sys
from importlib import import_module


def _import_symbol(module_name, symbol_name):
    try:
        return getattr(import_module(module_name), symbol_name)
    except (ImportError, AttributeError) as exc:
        raise RuntimeError(
            "Missing RAG dependencies. Install them with: "
            "python -m pip install python-dotenv langchain-community "
            "langchain-text-splitters langchain-openai langchain-chroma"
        ) from exc


# Load dependencies dynamically so static analyzers do not report unresolved
# imports when this file is opened outside the project's configured environment.
try:
    load_dotenv = _import_symbol("dotenv", "load_dotenv")
    TextLoader = _import_symbol("langchain_community.document_loaders", "TextLoader")
    RecursiveCharacterTextSplitter = _import_symbol(
        "langchain_text_splitters", "RecursiveCharacterTextSplitter"
    )
    OpenAIEmbeddings = _import_symbol("langchain_openai", "OpenAIEmbeddings")
    ChatOpenAI = _import_symbol("langchain_openai", "ChatOpenAI")
    Chroma = _import_symbol("langchain_chroma", "Chroma")
    ChatPromptTemplate = _import_symbol("langchain_core.prompts", "ChatPromptTemplate")
except RuntimeError as exc:
    print(f"Error: {exc}", file=sys.stderr)
    sys.exit(1)

# 1. Load Environment Variables
load_dotenv(override=True)

if not os.getenv("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY environment variable is not set.")
    sys.exit(1)


# 2. Setup Sample Document (or pass an existing .txt file)
DOCUMENT_PATH = "sample_data.txt"

def create_sample_document():
    """Helper to generate a dummy document if one doesn't exist."""
    if not os.path.exists(DOCUMENT_PATH):
        sample_text = """
        The Apollo 11 mission was the spaceflight that first landed humans on the Moon. 
        Commander Neil Armstrong and Lunar Module Pilot Buzz Aldrin landed the Apollo Lunar Module Eagle on July 20, 1969.
        Neil Armstrong became the first person to step onto the lunar surface six hours and 39 minutes later on July 21 at 02:56 UTC.
        Buzz Aldrin joined him 19 minutes later. They spent about two and a quarter hours together outside the spacecraft.
        They collected 47.5 pounds (21.5 kg) of lunar material to bring back to Earth.
        Command Module Pilot Michael Collins flew the Command Module Columbia alone in lunar orbit while they were on the Moon's surface.
        Armstrong and Aldrin spent 21 hours, 36 minutes on the lunar surface at a site they named Tranquility Base.
        The mission was launched by a Saturn V rocket from Kennedy Space Center in Merritt Island, Florida.
        """
        with open(DOCUMENT_PATH, "w", encoding="utf-8") as f:
            f.write(sample_text.strip())
        print(f"[+] Created sample document at '{DOCUMENT_PATH}'")


# 3. Build RAG Pipeline
def initialize_rag_pipeline(file_path: str):
    print("\n--- Loading Document & Indexing Vector Store ---")
    
    # Load raw text document
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    
    # Split text into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    chunks = text_splitter.split_documents(documents)
    print(f"[+] Document split into {len(chunks)} chunks.")
    
    # Embed chunks and index into Chroma vector store
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="rag_demo"
    )
    print("[+] Vector store indexed successfully.")
    
    return vector_store


# 4. Query Execution Loop
def run_interactive_rag_loop(vector_store):
    # Initialize LLM and Prompt Template
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)
    
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Answer the user's question using ONLY the provided context below. If the answer is not contained within the context, respond with 'I cannot answer this based on the provided document.'\n\nContext:\n{context}"),
        ("human", "{question}")
    ])
    
    print("\n" + "=" * 80)
    print("RAG System Ready! Ask your questions (type 'exit' or 'quit' to stop).")
    print("=" * 80)
    
    question_count = 0
    
    while True:
        try:
            user_question = input(f"\nQuestion #{question_count + 1}: ").strip()
            if not user_question:
                continue
            if user_question.lower() in ["exit", "quit"]:
                print("Exiting RAG pipeline session.")
                break
            
            # Step A: Retrieve Top-K Context Chunks
            retriever = vector_store.as_retriever(search_kwargs={"k": 2})
            retrieved_docs = retriever.invoke(user_question)
            
            # Step B: Display Retrieved Chunks Explicitly
            print("\n" + "-" * 40 + " RETRIEVED CONTEXT CHUNKS " + "-" * 40)
            for idx, doc in enumerate(retrieved_docs, start=1):
                clean_content = doc.page_content.replace("\n", " ").strip()
                print(f"[Chunk {idx}]: {clean_content}")
            print("-" * 106)
            
            # Step C: Combine Context & Generate Response
            context_str = "\n\n".join([doc.page_content for doc in retrieved_docs])
            formatted_prompt = prompt_template.format_messages(
                context=context_str,
                question=user_question
            )
            
            response = llm.invoke(formatted_prompt)
            
            # Step D: Print Final Output
            print("\n[GROUNDED ANSWER]:")
            print(response.content)
            
            question_count += 1

        except KeyboardInterrupt:
            print("\nSession interrupted. Exiting.")
            break


if __name__ == "__main__":
    create_sample_document()
    vector_db = initialize_rag_pipeline(DOCUMENT_PATH)
    run_interactive_rag_loop(vector_db)
