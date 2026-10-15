from common import client
from google import genai  # calls Google's Gemini Python library
from google.genai import types

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
prompt = "Write a one-sentence tagline for a coffee shop."  # First place for instructions
# variables: 1) temperature, 2) top_p ,3) top_k, 4) max_output_tokens,
# 5) total_token_count (adds prompt tokens and output tokens)
# testing different temperatures. 0 is nearly deterministic, higher values give
# more variety and more risk of nonsense
# at 0.0 the output is almost the same every run; at 1.0 it varies but stays
# sensible; at 2.0 it often becomes odd or loses coherence.
for temp in [0.0, 1.0, 2.0]:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temp,
            # system_instruction="You are a grumpy poet.",  #system_instruction   # Second place for instructions
            # sets a role the model keeps for the whole call.
        ),
    )
    print(f"--- temperature={temp} ---")
    print(response.text)
    print("Metadata:", response.usage_metadata)  # response.usage_metadata
    # shows prompt, output and total counts separately.
    print("tokens used:", response.usage_metadata.total_token_count)
# =============================================================================
# testing different maximum output tockens. Only consider the k most likely
# tokens.
for maxOut in [10, 15]:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            max_output_tokens=maxOut,
        ),
    )
    print(f"--- max_output_tokens={maxOut} ---")
    print(response.text)
    print("tokens used:", response.usage_metadata.total_token_count)
# =============================================================================
# testing different top_ps. Keep the smallest group of tokens whose
# probabilities add up to this share
for topP in [0.1, 0.95]:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            top_p=topP,
        ),
    )
    print(f"--- top_p={topP} ---")
    print(response.text)
    print("tokens used:", response.usage_metadata.total_token_count)
# =============================================================================
# testing different top_ks. Keep only this many of the most likely tokens
for topK in [4, 6]:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            top_k=topK,
        ),
    )
    print(f"--- top_k={topK} ---")
    print(response.text)
    print("tokens used:", response.usage_metadata.total_token_count)
