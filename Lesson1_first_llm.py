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

# =============================================================================
from google.genai import types

prompt = "Write a one-sentence tagline for a coffee shop."

for temp in [0.0, 1.0, 2.0]:
    # step 3: call client model and read the response
    response = client.models.generate_content(
        # model="gemini-3-flash-preview",
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temp,
            max_output_tokens=10,
            # system_instruction="You are a witty marketing copywriter.",
            system_instruction="You are a grumpy poet.",
        ),
    )
    print(f"--- temperature={temp} ---")
    print(response.text)
    print("tokens used:", response.usage_metadata.total_token_count)
