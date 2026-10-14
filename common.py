import os  # os is needed when reading API key from ".env" file
from dotenv import (
    load_dotenv,
    find_dotenv,
)  # to make reading ".env" files possible
from google import genai  # calls Google's Gemini Python library

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# =============================================================================
# since API_KEY is something personal, we save it in an ".env" file (inside the file we write: GEMINI_API_KEY=personal API_KEY), then we call that file here
# step 1: load the key
# load_dotenv(find_dotenv())
load_dotenv(find_dotenv(), override=True)
# step 2: create the client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
