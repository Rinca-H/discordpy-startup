import discord
import random
import json
import os

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    if client.user != message.author:
        if message.content.startswith('おはよう'):
            m = 'おはよう！' + message.author.name + 'さん！'
            await message.channel.send(m)

client.run(token)