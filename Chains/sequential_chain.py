from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.9)

prompt1 = PromptTemplate(
    template='give me a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='extract the 5 important points or summary from the given {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain=prompt1 | model | parser | prompt2 | model | parser 

result = chain.invoke({'topic':'Virat kohli'})
print(result)