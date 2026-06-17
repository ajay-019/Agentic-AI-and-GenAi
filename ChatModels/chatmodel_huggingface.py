import os

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llms = HuggingFaceEndpoint(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=os.environ.get("HUGGINGFACEHUB_API_TOKEN")
)

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    model = ChatHuggingFace(llm=llms)
    response = model.invoke(user_input)
    print(response.content)