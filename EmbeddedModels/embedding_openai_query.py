from google import genai

client = genai.Client(api_key="zyz")

result = client.models.embed_content(
    model="text-embedding-004",
    contents="What is the capital of India?"
)

print(result.embeddings[0].values)