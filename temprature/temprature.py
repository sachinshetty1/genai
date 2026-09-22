import os
from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv

# Load the project key file before creating the client.
load_dotenv(Path(__file__).parent / ".venv" / ".env", override=True)

# Initialize the OpenAI client (reads OPENAI_API_KEY from environment)
client = OpenAI()

# Prompt designed to test creative variation
PROMPT = "Write a 3-sentence story about a robot discovering a flower on a desolate planet."
TEMPERATURES = [0.1, 0.5, 1.0]

results = {}

# Iterate over temperature settings
for temp in TEMPERATURES:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": PROMPT}
        ],
        temperature=temp,
    )
    # Store response text
    results[temp] = response.choices[0].message.content.strip()

# Print formatted side-by-side comparison
print("=" * 80)
print(f"PROMPT: {PROMPT}")
print("=" * 80)

for temp, text in results.items():
    print(f"\n--- TEMPERATURE: {temp} ---")
    print(text)

print("\n" + "=" * 80)
