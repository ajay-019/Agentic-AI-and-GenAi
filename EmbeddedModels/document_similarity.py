from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", dimensions=300)
documents = ["Delhi is the capital of india.",
            "Mumbai is the financial capital of india.",   
            "Bangalore is the IT capital of india.",
            "Chennai is the cultural capital of india."
            ]
query = "Which city is the it capital of india?"
document_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)
similarity_scores = cosine_similarity([query_embedding], document_embeddings)[0]
print(documents[sorted(list(enumerate(similarity_scores)), key=lambda x: x[1], reverse=True)[0][0]])
# most_similar_index = np.argmax(similarity_scores)
# print(f"Most similar document: '{documents[most_similar_index]}' with similarity score: {similarity_scores[most_similar_index]:.4f}")   

