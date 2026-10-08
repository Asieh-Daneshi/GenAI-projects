from google import genai  # calls Google's Gemini Python library

client = genai.Client(
    api_key="AQ.Ab8RN6KS15VEkmW2QMsuXtUq5IR1J5uwEQwiklWA0yHzrH96PQ"
)  # creates a connection between my Python code and Google's API

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    # contents="Explain machine learning to a 10-year-old.",
    # contents="Explain machine learning to a senior software engineer.",
    # contents="Explain machine learning using a cooking analogy."
    contents="Explain using a simple real-world analogy 'What is the difference between an AI application and an AI agent?', and give a simple example of each",
)
print(response.text)
