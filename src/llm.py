from typing import Optional
import openai
import os
from dotenv import load_dotenv
from pydantic import BaseModel, validator

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=OPENAI_API_KEY)


from enum import Enum
from pydantic import BaseModel

class ModelName(str, Enum):
    gpt4 = "gpt-4-1106-preview"
    gpt3 = "gpt-3.5-turbo-1106"
    gpt4v = "gpt-4-vision-preview"

class OpenAIProps(BaseModel):
    temperature: int = 0
    model: ModelName
    top_p: Optional[int] = None
    top_k: Optional[int] = None
    return_json: Optional[dict] = {"type": "json_object"}
    

def get_chat_response(props: OpenAIProps, message_list: list, return_json: bool = False) -> str:
    response = client.chat.completions.create(
        model=props.model,
        temperature=props.temperature,
        response_format=props.return_json if return_json else None,
        messages=message_list
    )

    return response.choices[0].message.content
