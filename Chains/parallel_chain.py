import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.9)
model2 = ChatGroq(model="llama-3.3-70b-versatile")

prompt1 = PromptTemplate(
    template='give me a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='generate the quiz on {topic} ,make sure each question has 4 option and 1 of 4 is correct',
    input_variables=['topic']
)

prompt3= PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and {quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes':prompt1 | model1 | parser,
    'quiz':prompt2 | model2 | parser
})

chain = parallel_chain | prompt3 | model1 | parser

result = chain.invoke({'topic':'Rajasthan'})
print(result)
chain.get_graph().print_ascii()