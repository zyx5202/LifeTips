import os
import discord
from discord.ext import commands
import os
from pathlib import Path
from datetime import datetime
import openai
import pickle

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.environ["TOKEN"]
API_KEY = os.environ["API_KEY"]
ORGANIZATION = os.environ["ORGANIZATION"]

token = TOKEN
bot = commands.Bot(command_prefix='!')

openai.organization = ORGANIZATION
openai.api_key = API_KEY
openai.Model.list()

@bot.command()
async def hello(ctx, arg=None):
  await ctx.send("hello! I'm test-bot!")

@bot.command()
async def bye(ctx, arg=None):
  await ctx.send("Goodbye! See you later.")

@bot.command()
async def short_advice(ctx, *arg):
    '''
    Function: generates short advice based on a prompt. 
    '''
    if arg is not None:
        the_prompt = ' '.join(arg)
        if isinstance(the_prompt, str):
          prompt = "Write a sentence of advice for someone that tells you: " + the_prompt

          response = openai.Completion.create(
          engine="text-curie-001",
          prompt=prompt,
          temperature=0.5,
          max_tokens=256,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )
          await ctx.send(response['choices'][0]['text'])
        else:
            await ctx.send("Prompt should be a string. Not sure where this went wrong.")

@bot.command()
async def advice(ctx, *arg):

    '''
    Function: generates some advice based on a prompt. 
    '''
    if arg is not None:
        the_prompt = ' '.join(arg)
        if isinstance(the_prompt, str):
          prompt = "Write some advice for someone that tells you: " + the_prompt

          response = openai.Completion.create(
          engine="text-curie-001",
          prompt=prompt,
          temperature=0.5,
          max_tokens=256,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )
          await ctx.send(response['choices'][0]['text'])
        else:
            await ctx.send("Prompt should be a string. Not sure where this went wrong.")

@bot.command()
async def long_advice(ctx, *arg):

    '''
    Function: generates a paragraph of advice based on a prompt. 
    '''
    if arg is not None:
        the_prompt = ' '.join(arg)
        if isinstance(the_prompt, str):
          prompt = "Write a paragraph of advice for someone that tells you: " + the_prompt

          response = openai.Completion.create(
          engine="text-curie-001",
          prompt=prompt,
          temperature=0.5,
          max_tokens=256,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )
          await ctx.send(response['choices'][0]['text'])
        else:
            await ctx.send("Prompt should be a string. Not sure where this went wrong.")

@bot.command()
async def essay_advice(ctx, *arg):

    '''
    Function: generates an essay of advice based on a prompt. 
    '''
    if arg is not None:
        the_prompt = ' '.join(arg)
        if isinstance(the_prompt, str):

          prompt = "Write an essay of advice for someone that tells you: " + the_prompt

          response = openai.Completion.create(
          engine="text-curie-001",
          prompt=prompt,
          temperature=0.5,
          max_tokens=256,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )
          await ctx.send(response['choices'][0]['text'])
        else:
            await ctx.send("Prompt should be a string. Not sure where this went wrong.")

@bot.command()
async def story(ctx, *arg):

    '''
    Function: generates a terrible story. 
    '''
    prompt = "Write a good story about unicorns"
    prompt = prompt[0]

    response = openai.Completion.create(
    engine="text-curie-001",
    prompt=prompt,
    temperature=0.4,
    max_tokens=256,
    top_p=0.9,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
    await ctx.send(response['choices'][0]['text'])
       
if __name__ == "__main__":
    bot.run(TOKEN)
