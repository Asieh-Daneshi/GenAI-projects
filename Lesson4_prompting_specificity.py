from common import client
from google import genai  # calls Google's Gemini Python library
from google.genai import types

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
prompt = "Write a one-sentence tagline for a coffee shop."
temp = 0.0
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=temp,
    ),
)
print("Normal")
print(response.text)
# =============================================================================
prompt = "Write a one-sentence tagline for a coffee shop."
temp = 0.0
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=temp,
        system_instruction="less than 5 words",  # system_instruction
    ),
)
print("limited to 5 words")
print(response.text)
# =============================================================================
prompt = "Write a one-sentence tagline for a coffee shop."
temp = 0.0
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=temp,
        system_instruction="in a poetic tone",  # system_instruction
    ),
)
print("poetic tone")
print(response.text)
# =============================================================================
prompt = "Write a one-sentence tagline for a coffee shop."
temp = 0.0
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=temp,
        system_instruction="in persian",  # system_instruction
    ),
)
print("persian language")
print(response.text)
# =============================================================================
prompt = "Write a one-sentence tagline for a coffee shop."
temp = 0.0
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=temp,
        system_instruction="not to use word 'and' ",  # system_instruction
    ),
)
print("not to use 'and'")
print(response.text)
