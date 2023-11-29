import discord
from prompts import GENERIC_SYSTEM_PROMPT
from src.llm import get_llm_response, OpenAIProps, ModelName

async def construct_reply(message: discord.Message):

    # TODO: add prompt switcher?
    message_list = [
        {"role":"system", "content":GENERIC_SYSTEM_PROMPT},
    ]
    context = await get_context(message)

    message_list += context

    props = OpenAIProps(
        temperature=1,
        model=ModelName.gpt3,
    )
    reply = get_llm_response(props=props, message_list=message_list)
    return reply

async def get_context(message: discord.Message):

    #TODO: what if there are images? deal with it differently, use different prompts
    context = []
    async for msg in message.channel.history(limit=50):
        if msg.author.bot:
            assistant = {"role": "assistant", "content": msg.content}
            context.append(assistant)
        else:
            user = {"role":"user", "content":msg.content}
            context.append(user)
    
    return context[::-1]