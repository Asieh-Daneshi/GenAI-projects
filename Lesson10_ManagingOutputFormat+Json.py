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

Emails = ["hey can we meet tmrw at 2 to go over the stuff? lmk if that works thanks",
    "Hi, booking us in for Thursday at 10am to discuss the updates. hope thats okay, thx!",
    "hey are u free monday around 3? lets set up a quick meeting and figure this out lol",
    "Hello, I've scheduled a meeting for Friday at 11:30 to talk through the project. pls confirm when u can",
    "hey, we should book some time to talk about the plan. when are u free? need to get this sorted soon",
]

class Meeting(BaseModel):
    date: str | None = None
    time: str | None = None
    attendees: list[str] | None = None
    topic: str | None = None
    
    
for email in Emails:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Email : " + email,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Meeting,
        ),
    )
    print(email)
    print(response.parsed)
    print()