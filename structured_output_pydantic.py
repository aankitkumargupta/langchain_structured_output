from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Create the chat model
model = ChatOpenAI()

# Schema


class Review(BaseModel):
    key_themes: list[str] = Field(
        description="Write down all the key themes discussed in list"
    )
    summary: str = Field(description="A brief summary of the text snippet")
    sentiment: Literal["pos", "neg"] = Field(
        description="Return Sentiment of the review, either positive, negative or neutral"
    )
    pros: Optional[list[str]] = Field(
        default=None, description="write down all the pros in list"
    )
    cons: Optional[list[str]] = Field(
        default=None, description="write do wn all the cons in list"
    )
    name: Optional[str] = Field(
        default=None, description="Write the name of the reviewer"
    )


structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """ Flagship Smartphone Review:
This phone is a powerhouse—stunning display, super-fast performance, and a top-tier camera that shines in all lighting conditions. Battery life is solid, and the design feels premium. A bit pricey, but if you want the best, it's worth it.
                               
Budget Smartphone Review:
Great value for the price! Smooth performance, decent camera, and solid battery life. The display is good, though not flagship-level. Some minor lag with heavy apps, but for everyday use, it’s reliable."""
)

print(result)
