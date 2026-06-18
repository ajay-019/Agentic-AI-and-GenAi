from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt=PromptTemplate(
    template='generate a creative story about {topic} in 100 words',
    input_variables=['topic']
)
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.9)

parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({'topic': 'Love Breakup'})
print(result)

chain.get_graph().print_ascii()