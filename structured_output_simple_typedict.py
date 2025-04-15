from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Create the chat model
model = ChatOpenAI()

# Schema


class Review(TypedDict):
    summary: str
    sentiment: str


structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """ India is my country, I love my country. India has 29 states. All states are diverse in culture and language"""
)

print(result)
print(result["summary"])
print(result["sentiment"])
