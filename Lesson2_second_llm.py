import os
from dotenv import (
    load_dotenv,
    find_dotenv,
)  # to make reading ".env" files possible
from google import genai  # calls Google's Gemini Python library

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# =============================================================================
# Since every day we can use each model only a few number of times. Here we find which models are available for our purpose so that we can switch between them when the capacity of one is over
# for m in client.models.list():
#     if "generateContent" in (m.supported_actions or []):
#         print(m.name)
# =============================================================================

# =============================================================================
# since API_KEY is something personal, we save it in an ".env" file (inside the file we write: GEMINI_API_KEY=personal API_KEY), then we call that file here
# load_dotenv(find_dotenv())
load_dotenv(find_dotenv(), override=True)
client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)  # creates a connection between my Python code and Google's API

response = client.models.generate_content(
    # model="gemini-3-flash-preview",
    model="gemini-3.5-flash-lite",
    contents="Explain machine learning to a 10-year-old.",
    # contents="Explain machine learning to a senior software engineer.",
    # contents="Explain machine learning using a cooking analogy."
    # contents="Explain using a simple real-world analogy 'What is the difference between an AI application and an AI agent?', and give a simple example of each",
)
print(response.text)
