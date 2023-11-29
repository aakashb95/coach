import discord
from prompts import GENERIC_SYSTEM_PROMPT
from src.llm import get_llm_response, OpenAIProps, ModelName

async def construct_reply(message: discord.Message):
    message_list = [
        {"role":"system", "content":GENERIC_SYSTEM_PROMPT},
        {"role": "user", "content": message.content}
    ]

    props = OpenAIProps(
        temperature=1,
        model=ModelName.gpt3,
    )
    print(message_list)
    reply = get_llm_response(props=props, message_list=message_list)
    print(reply)
    return reply

