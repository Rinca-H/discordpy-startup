import discord
import asyncio
import random
import sys
import os

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
channel_id = 659621491775635507
channel = client.get_channel(channel_id)


@client.event
async def on_message(message):
    if client.user != message.author:   # 送り主がBotだった場合反応したくないから
        if message.content.startswith('おはよう'):   # どんな言葉で始まるか調べる
            m = 'おはよう！' + message.author.name + 'さん！'   # メッセージを変数に詰め込む
            await message.channel.send(m)   # メッセージが送られてきたチャンネルへメッセージを送る

bot.run(token)
