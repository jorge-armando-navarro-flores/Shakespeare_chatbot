from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

parser = StrOutputParser()
model = ChatOpenAI(model="gpt-3.5-turbo")
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an assistant that speaks like Shakespeare.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

shakespeare_chain = prompt_template | model | parser
