from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def on_message(message):
    if bot.user != message.author:   # 送り主がBotだった場合反応したくないから
        if message.content.startswith('おはよう'):   # どんな言葉で始まるか調べる
            m = 'おはよう！' + message.author.name + 'さん！'   # メッセージを変数に詰め込む
            await message.channel.send(m)   # メッセージが送られてきたチャンネルへメッセージを送る

bot.run(token)
