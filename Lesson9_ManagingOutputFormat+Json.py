from pydantic import BaseModel
from google import genai  # calls Google's Gemini Python library
from google.genai import types
import os  # os is needed when reading API key from ".env" file
from dotenv import (
    load_dotenv,
    find_dotenv,
)  # to make reading ".env" files possible

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# =============================================================================
load_dotenv(find_dotenv(), override=True)
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

class Review(BaseModel):
    Enum: str # "positive", "negative" or "neutral"
    product: str
    complaint: str | None
response = client.models.generate_content(
model="gemini-3-flash-preview",
    contents="Review: The kettle boils fast but the lid broke in a week.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Review,
    ),
)
print(response.text) # a JSON string
print(response.parsed) # a Review object