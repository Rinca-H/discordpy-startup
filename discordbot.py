import discord
import random
import json
import os

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    if client.user != message.author:    # 送り主がBotだった場合反応したくないから
        if message.content.startswith('おはよう'):    # どんな言葉で始まるか調べる
            m = 'おはよう！' + message.author.name + 'さん！'    # メッセージを変数に詰め込む
            await message.channel.send(m)    # メッセージが送られてきたチャンネルへメッセージを送る
        
        
        elif message.content.startswith('おやすみ'):
            m = 'おやすみ！' + message.author.name + 'さん！'
            await message.channel.send(m)
        
        
        elif message.content.startswith('/say'):
            m = message.content[5:]    # 5文字目以降を取得
            await message.delete()    #1つ前のメッセージを消す
            await message.channel.send(m)
        
        
        elif message.content.startswith('/help'):   # 改行コード使用例↓ と、代入するのはmじゃなくてもいい証明
            desc1 = '\n・おはよう\n・おやすみ\n(・かわいい)\n・生きてる\n・おみくじ\n(・今日の格言)\n・鈴花'
            embed = discord.Embed(title="反応する言葉",description=desc1, color=0x64ec86)
            embed.add_field(name="/say",value="何かを言わせられるよ",inline=False)
            embed.add_field(name="/termux",value="termuxの使い方を教えるよ",inline=False)
            embed.add_field(name="/howtocheck",value="termuxでのpythonのチェックのしかたを教えるよ",inline=False)
            embed.add_field(name="/logout",value="ログアウトするよ(使わないで！)",inline=False)
            embed.add_field(name="/slot",value="スロットをプレイするよ",inline=False)
            await message.channel.send(embed=embed)
        
        
        elif message.content.startswith('/termux'):
            a = 'termuxで、\n「`$cd /storage/emulated/0/bot`」\n「`$python 〇〇.py`」\nと入力するとそのpythonファイルを起動できるよ'
            await message.channel.send(a)
        
        
        elif message.content.startswith('/howtocheck'):
            a = '「`$pep8 〇〇.py`」：通常\n「`$pep8 --statistics -qq 〇〇.py`」：簡潔に\n「`$pep8 --show-source 〇〇.py`」：詳しく'
            await message.channel.send(a)
        
        
        elif message.content.startswith('/logout'):
            m = 'じゃあね'
            await message.delete()
            await message.channel.send(m)
            await client.logout()    # ログアウト
            await sys.exit()    # シャットダウン
        
        
        elif message.content.startswith('生きてる'):
            m = '生きてるよ～笑'
            await message.channel.send(m)
        
        
        elif '鈴花' in message.content:   # 「鈴花」が含まれてるだけで反応する
            m = 'なに〜？？よんだ〜？'
            await message.channel.send(m)
        
        
        elif message.content.startswith('おみくじ'):
            x = random.randint(1, 6)
            if x == 6:
                m = 'すごい！あたり！！'
                await message.channel.send(m)
            elif x != 6:   # notはこう
                m = 'ざんねん……はずれ……'
                await message.channel.send(m)
        
        
        
        elif message.content.startswith('/slot'):
            x = str(random.randint(1, 9))
            y = str(random.randint(1, 9))
            z = str(random.randint(1, 9))
            m = '| ' + x + ' | ' + y + ' | ' + z + ' |'
            await message.channel.send(m)
            if x == '7' and y == '7' and z == '7':
                n = 'あたり！！！'
                await message.channel.send(n)
        


client.run(token)