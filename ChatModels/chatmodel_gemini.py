from google import genai

client = genai.Client(api_key="xyz")

chat = client.chats.create(
    model="gemini-2.5-flash"
)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = chat.send_message(user_input)

    print("AI:", response.text)