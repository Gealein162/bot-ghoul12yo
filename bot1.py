import discord
from discord.ext import commands
import os
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('привет'):
        await message.channel.send('нахуя вы что-то в чат высираете бездари')
  if message.content.startswith('дед инсайд'):
        await message.channel.send(f'{ message.author.mention }' ' че звал сларк')
        
token = os.environ.get('BOT_TOKEN')
