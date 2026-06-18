from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token="xyz"
)
model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']  
)

template2 = PromptTemplate(
    template='write 2 line summary on {text}',
    input_variables=['text']    
)
parser=StrOutputParser()
chain = template1 | model | parser| template2 | model | parser
print(chain.invoke({'topic': 'black hole'}))
