from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch, RunnableLambda
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.9)
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative', 'neutral'] = Field(description='Sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)    

prompt1 = PromptTemplate(
    template='classify the sentiment of the following text as positive, negative or neutral: {text} \n {format_instructions}',
    input_variables=['text'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='write the appropriate response to this positive {feedback}',
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template='write the appropriate response to this negative {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2 | model | parser),
    (lambda x:x.sentiment=='negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)


chain = classifier_chain | branch_chain

print(chain.invoke({'text':'this product is terrible'}))
chain.get_graph().print_ascii()