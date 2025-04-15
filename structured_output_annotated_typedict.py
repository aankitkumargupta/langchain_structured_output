from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Optional, Literal
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Create the chat model
model = ChatOpenAI()

# Schema


class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in list"]
    summary: Annotated[str, "A brief summary of the text snippet"]
    sentiment: Annotated[
        Literal["pos", "neg"],
        "Return Sentiment of the review, either positive, negative or neutral",
    ]
    pros: Annotated[Optional[list[str]], "write down all the pros in list"]
    cons: Annotated[Optional[list[str]], "write do wn all the cons in list"]


structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """ Flagship Smartphone Review:
This phone is a powerhouse—stunning display, super-fast performance, and a top-tier camera that shines in all lighting conditions. Battery life is solid, and the design feels premium. A bit pricey, but if you want the best, it's worth it.
                               
Budget Smartphone Review:
Great value for the price! Smooth performance, decent camera, and solid battery life. The display is good, though not flagship-level. Some minor lag with heavy apps, but for everyday use, it’s reliable."""
)

print(result)
