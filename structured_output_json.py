from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Create the chat model
model = ChatOpenAI

# Schema

json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
            "title": "Key Themes",
            "type": "array",
            "items": {"type": "string"},
            "description": "Write down all the key themes discussed in list",
        },
        "summary": {
            "title": "Summary",
            "type": "string",
            "description": "A brief summary of the text snippet",
        },
        "sentiment": {
            "title": "Sentiment",
            "type": "string",
            "enum": ["pos", "neg"],
            "description": "Return Sentiment of the review, either positive, negative or neutral",
        },
        "pros": {
            "title": "Pros",
            "type": "array",
            "items": {"type": "string"},
            "description": "write down all the pros in list",
        },
        "cons": {
            "title": "Cons",
            "type": "array",
            "items": {"type": "string"},
            "description": "write do wn all the cons in list",
        },
        "name": {
            "title": "Name",
            "type": "string",
            "description": "Write the name of the reviewer",
        },
    },
    "required": ["key_themes", "summary", "sentiment"],
}


structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke(
    """ Flagship Smartphone Review:
This phone is a powerhouse—stunning display, super-fast performance, and a top-tier camera that shines in all lighting conditions. Battery life is solid, and the design feels premium. A bit pricey, but if you want the best, it's worth it.
                               
Budget Smartphone Review:
Great value for the price! Smooth performance, decent camera, and solid battery life. The display is good, though not flagship-level. Some minor lag with heavy apps, but for everyday use, it’s reliable."""
)

print(result)
