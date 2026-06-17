from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

document=["Delhi is the capital of india.",
        "Mumbai is the financial capital of india.",
        "Bangalore is the IT capital of india."
        ]

vector = embedding.embed_documents(document)
print(str(vector))