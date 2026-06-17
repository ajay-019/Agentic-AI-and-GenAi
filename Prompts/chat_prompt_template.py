from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
load_dotenv()

chat_template = ChatPromptTemplate.from_messages([
    ('system', "You are a helpful {domain} expert."),
    ('human', "Explain in Simple term, what is {topic}?"),
])

prompt = chat_template.invoke({'domain':'Cricket','topic':'Dusra'})
print(prompt)
