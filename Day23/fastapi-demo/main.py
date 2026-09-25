import math
import os
from pathlib import Path

import fitz
import mysql.connector
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from openai import OpenAI
from pydantic import BaseModel


# =========================================================
# CONFIGURATION
# =========================================================

# Load variables from .env
load_dotenv()


# Create FastAPI application
app = FastAPI(
    title="Employee Management, AI and RAG API"
)


# Current project folder
BASE_DIR = Path(__file__).resolve().parent


# Create OpenAI client
# It automatically reads OPENAI_API_KEY from .env
client = OpenAI()


# OpenAI LLM model
OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-5.6"
)


# OpenAI embedding model
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "text-embedding-3-small"
)


# =========================================================
# PYDANTIC MODELS
# =========================================================

# Model for adding an employee
class Employee(BaseModel):
    id: int
    name: str
    age: int
    salary: float
    desig: str


# Model for updating an employee
class EmployeeUpdate(BaseModel):
    name: str
    age: int
    salary: float
    desig: str


# Model for normal AI POST request
class AIRequest(BaseModel):
    question: str


# Model for RAG POST request
class RAGRequest(BaseModel):
    question: str


# =========================================================
# MYSQL CONNECTION
# =========================================================

def get_connection():

    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "employee_db")
    )


# =========================================================
# SIMPLE IN-MEMORY RAG STORAGE
# =========================================================

# This list stores:
# text, page number, filename and embedding
rag_documents = []


# =========================================================
# BASIC APIs
# =========================================================

# Display index.html
@app.get("/")
def home():

    return FileResponse(
        BASE_DIR / "index.html"
    )


# Simple welcome API
@app.get("/welcome/{name}")
def welcome(name: str):

    return {
        "message": f"Welcome, {name}!"
    }


# Simple addition API
@app.get("/add")
def add(a: int, b: int):

    result = a + b

    return {
        "number1": a,
        "number2": b,
        "result": result
    }


# =========================================================
# EMPLOYEE CRUD APIs
# =========================================================

# 1. POST: Add a new employee
@app.post("/employees")
def add_employee(employee: Employee):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO employees
        (id, name, age, salary, desig)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        employee.id,
        employee.name,
        employee.age,
        employee.salary,
        employee.desig
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return {
        "message": "Employee added successfully",
        "employee": employee
    }


# 2. GET: Get all employees
@app.get("/employees")
def get_all_employees():

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    query = "SELECT * FROM employees"

    cursor.execute(query)

    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return employees


# 3. GET: Get employee by ID
@app.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: int):

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    query = """
        SELECT * FROM employees
        WHERE id = %s
    """

    cursor.execute(
        query,
        (employee_id,)
    )

    employee = cursor.fetchone()

    cursor.close()
    connection.close()

    return employee


# 4. PUT: Update employee by ID
@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate
):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE employees
        SET name = %s,
            age = %s,
            salary = %s,
            desig = %s
        WHERE id = %s
    """

    values = (
        employee.name,
        employee.age,
        employee.salary,
        employee.desig,
        employee_id
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return {
        "message": "Employee updated successfully",
        "employee_id": employee_id
    }


# 5. DELETE: Delete all employees
# Keep this API above the delete-by-ID API
@app.delete("/employees/all")
def delete_all_employees():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM employees"
    )

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "message": "All employees deleted successfully"
    }


# 6. DELETE: Delete employee by ID
@app.delete("/employees/{employee_id}")
def delete_employee_by_id(employee_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        DELETE FROM employees
        WHERE id = %s
    """

    cursor.execute(
        query,
        (employee_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "message": "Employee deleted successfully",
        "employee_id": employee_id
    }


# =========================================================
# NORMAL LLM APIs
# =========================================================

# GET: Ask a general question
@app.get("/ai")
def ask_ai_get(question: str):

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=question
    )

    return {
        "question": question,
        "answer": response.output_text
    }


# POST: Ask a general question
@app.post("/ai")
def ask_ai_post(request: AIRequest):

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=request.question
    )

    return {
        "question": request.question,
        "answer": response.output_text
    }


# =========================================================
# RAG HELPER FUNCTIONS
# =========================================================

# Extract text from PDF pages
def extract_pdf_text(file_bytes):

    pdf = fitz.open(
        stream=file_bytes,
        filetype="pdf"
    )

    pages = []

    for page_index, page in enumerate(pdf):

        page_text = page.get_text()

        if page_text.strip():

            pages.append({
                "page": page_index + 1,
                "text": page_text
            })

    pdf.close()

    return pages


# Split text into smaller chunks
def create_chunks(
    text,
    chunk_size=1000,
    overlap=200
):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start = end - overlap

    return chunks


# Generate embeddings
def create_embeddings(texts):

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )

    embeddings = []

    for item in response.data:
        embeddings.append(
            item.embedding
        )

    return embeddings


# Calculate cosine similarity
def cosine_similarity(
    vector1,
    vector2
):

    dot_product = sum(
        value1 * value2
        for value1, value2
        in zip(vector1, vector2)
    )

    vector1_length = math.sqrt(
        sum(
            value * value
            for value in vector1
        )
    )

    vector2_length = math.sqrt(
        sum(
            value * value
            for value in vector2
        )
    )

    return dot_product / (
        vector1_length * vector2_length
    )


# Retrieve top matching chunks
def retrieve_chunks(
    question,
    top_k=3
):

    question_embedding = create_embeddings(
        [question]
    )[0]

    results = []

    for document in rag_documents:

        score = cosine_similarity(
            question_embedding,
            document["embedding"]
        )

        results.append({
            "text": document["text"],
            "page": document["page"],
            "filename": document["filename"],
            "score": score
        })

    # Highest similarity first
    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results[:top_k]


# Generate an answer using retrieved context
def generate_rag_answer(question):

    # Check whether PDF was uploaded
    if len(rag_documents) == 0:

        return {
            "question": question,
            "answer": "Please upload a PDF document first.",
            "sources": []
        }

    # Retrieve top 3 chunks
    retrieved_chunks = retrieve_chunks(
        question,
        top_k=3
    )

    context_parts = []

    for chunk in retrieved_chunks:

        context_parts.append(
            f"""
Document: {chunk["filename"]}
Page: {chunk["page"]}

Content:
{chunk["text"]}
"""
        )

    context = "\n".join(
        context_parts
    )

    prompt = f"""
You are a document question-answering assistant.

Answer the question using only the document context
provided below.

If the answer is not present in the context, respond:
"I could not find the answer in the uploaded document."

Document context:
{context}

User question:
{question}
"""

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=prompt
    )

    sources = []

    for chunk in retrieved_chunks:

        source = {
            "document": chunk["filename"],
            "page": chunk["page"]
        }

        # Avoid duplicate sources
        if source not in sources:
            sources.append(source)

    return {
        "question": question,
        "answer": response.output_text,
        "sources": sources
    }


# =========================================================
# RAG APIs
# =========================================================

# 1. POST: Upload PDF and generate embeddings
@app.post("/rag/upload")
async def upload_rag_document(
    file: UploadFile = File(...)
):

    # Read uploaded PDF
    file_bytes = await file.read()

    # Extract PDF pages
    pages = extract_pdf_text(
        file_bytes
    )

    all_chunks = []

    # Create chunks page by page
    for page in pages:

        page_chunks = create_chunks(
            page["text"]
        )

        for chunk in page_chunks:

            all_chunks.append({
                "text": chunk,
                "page": page["page"],
                "filename": file.filename
            })

    # If PDF does not contain readable text
    if len(all_chunks) == 0:

        return {
            "message": "No readable text found in the PDF",
            "filename": file.filename,
            "pages": 0,
            "chunks": 0
        }

    # Collect only chunk texts
    chunk_texts = []

    for chunk in all_chunks:

        chunk_texts.append(
            chunk["text"]
        )

    # Generate embeddings for all chunks
    embeddings = create_embeddings(
        chunk_texts
    )

    # Remove previously uploaded document
    rag_documents.clear()

    # Store chunks and embeddings
    for index, chunk in enumerate(all_chunks):

        rag_documents.append({
            "text": chunk["text"],
            "page": chunk["page"],
            "filename": chunk["filename"],
            "embedding": embeddings[index]
        })

    return {
        "message": "PDF uploaded and processed successfully",
        "filename": file.filename,
        "pages": len(pages),
        "chunks": len(rag_documents)
    }


# 2. GET: Ask question using RAG
@app.get("/rag/ask")
def ask_rag_get(question: str):

    return generate_rag_answer(
        question
    )


# 3. POST: Ask question using RAG
@app.post("/rag/ask")
def ask_rag_post(request: RAGRequest):

    return generate_rag_answer(
        request.question
    )


# 4. GET: View uploaded RAG document
@app.get("/rag/documents")
def get_rag_documents():

    if len(rag_documents) == 0:

        return {
            "message": "No RAG document uploaded",
            "documents": []
        }

    first_document = rag_documents[0]

    return {
        "message": "RAG document found",
        "documents": [
            {
                "filename": first_document["filename"],
                "chunks": len(rag_documents)
            }
        ]
    }


# 5. DELETE: Delete RAG document and embeddings
@app.delete("/rag/documents")
def delete_rag_documents():

    rag_documents.clear()

    return {
        "message": "RAG document and embeddings deleted successfully"
    }