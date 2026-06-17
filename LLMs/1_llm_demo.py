from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key="xyz"
)
chat_history = []
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break
    else:
        chat_history.append(HumanMessage(content=user_input))
        result = llm.invoke(chat_history)
        print("AI:", result.content)