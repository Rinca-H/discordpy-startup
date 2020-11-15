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
        memory = "まだ何もないよ"
        if message.content.startswith('おはよう'):   # どんな言葉で始まるか調べる
            m = 'おはよう！' + message.author.name + 'さん！'   # メッセージを変数に詰め込む
            await message.channel.send(m)   # メッセージが送られてきたチャンネルへメッセージを送る
        elif message.content.startswith('おやすみ'):
            m = 'おやすみ！' + message.author.name + 'さん！'
            await message.channel.send(m)
        elif message.content.startswith('/say'):
            m = message.content[5:]
            await message.delete()
            await message.channel.send(m)
        elif message.content.startswith('/help'):   # 改行コード使用例↓ と、代入するのはmじゃなくてもいい証明
            a = 'わたしが反応する言葉は、\n・おはよう\n・おやすみ\n・かわいい\n・生きてる\n・おみくじ\n・今日の格言\nだよ！(今のところ)'
            await message.channel.send(a)
        elif message.content.startswith('/termux'):
            a = 'termuxで、\n「`$cd /storage/emulated/0/bot`」\n「`$python 〇〇.py`」\nと入力するとそのpythonファイルを起動できるよ'
            await message.channel.send(a)
        elif message.content.startswith('/howtocheck'):
            a = '「`$pep8 〇〇.py`」：通常\n「`$pep8 --statistics -qq 〇〇.py`」：簡潔に\n「`$pep8 --show-source 〇〇.py`」：詳しく'
            await message.channel.send(a)
        elif message.content.startswith('/delate '):
            if discord.utils.get(message.author.roles, name='admin'):   # 役職比較
                delcmd = message.content       # メッセージを格納
                delcmd_ = delcmd.split()       # 入力メッセージのリスト化
                delcmd_int = int(delcmd_[1])   # 入力メッセージのint化
                delcmd_c = len(delcmd_)        # 入力メッセージの単語数
                if delcmd_c == 2 and delcmd_int <= 50 and delcmd_int > 1:
                    msgs = [msg async for msg in client.logs_from(message.channel, limit=(delcmd_int+1))]   # メッセージ取得↓
                    await client.delete_messages(msgs)
                    delmsg = await client.send_message(message.channel, '削除が完了しました')
                    await sleep(5)
                    await client.delete_message(delmsg)                                                     # メッセージ取得↑
                else:   # エラーメッセージを送る
                    await message.channel.send('コマンドが間違っています。[/delate *] *:2～50')
            else:   # エラーメッセージを送る
                await message.channel.send('admin権限がありません。')
        elif message.content.startswith('/logout'):
            m = 'じゃあね'
            await message.delete()
            await message.channel.send(m)
            await client.logout()
            await sys.exit()
        elif message.content.startswith('かわいい'):
            json_file = open('/storage/emulated/0/bot/list/rinca.json')
            json_loaded = json.load(json_file)
            json_peeled = json_loaded["startswithかわいい"]
            list = [e.get("word") for e in json_peeled]
            list_shuffled = random.sample(list, 1)
            await message.channel.send(list_shuffled[0])
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
        elif message.content.startswith('今日の格言'):
            json_file = open('/storage/emulated/0/bot/list/rinca.json')
            json_loaded = json.load(json_file)
            json_peeled = json_loaded["startswith今日の格言"]
            list = [e.get("word") for e in json_peeled]
            list_shuffled = random.sample(list, 1)
            await message.channel.send(list_shuffled[0])
        elif message.content.startswith('/slot'):
            x = str(random.randint(1, 9))
            y = str(random.randint(1, 9))
            z = str(random.randint(1, 9))
            m = '| ' + x + ' | ' + y + ' | ' + z + ' |'
            await message.channel.send(m)
            if x == '7' and y == '7' and z == '7':
                n = 'あたり！！！'
                await message.channel.send(n)
        elif message.content.startswith('/let'):
            allword = message.content
            word = allword[5:]
            opened_json = open('/storage/emulated/0/bot/list/memory.json')
            loaded_json = json.load(opened_json)
            peeled_json = loaded_json["main"] 
            dic = peeled_json[0]    # 辞書型化
            dic["a"] = str(word)    # a の値を変える
            changed_json = { "main": peeled_json }    # json の形に戻す
            opening = open('/storage/emulated/0/bot/list/memory.json', 'w')    # 'w'は書きますよという宣言
            json.dump(changed_json, opening, indent = 2)    # インデント2でjsonを上書き
            await message.channel.send('ん、覚えといた')
        elif message.content.startswith('/recall'):
            opened_json = open('/storage/emulated/0/bot/list/memory.json')
            loaded_json = json.load(opened_json)
            peeled_json = loaded_json["main"] 
            dic = peeled_json[0]    # 辞書型化
            await message.channel.send(str(dic["a"]))
        elif message.content.startswith('/embed '):
            channel_id = 659621491775635507
            channel = client.get_channel(channel_id)
            command = message.content
            splited = command.split()
            a = splited[1]
            b = splited[2]
            c = splited[3]
            embed = discord.Embed(title = str(a), color = 0x64ec86)
            embed.add_field(name = str(b), value = str(c), inline = False)
            await channel.send(embed = embed)
        elif message.content.startswith('/history'):
            channel_id = 659621491775635507
            channel = client.get_channel(channel_id)
            messages = await channel.history(limit=5).flatten() 
            await message.channel.send(messages)
        elif message.content.startswith('/target'):
            word = message.content
            splited = word.split()
            x = int(splited[1])
            y = int(splited[2]) 
            if x > 200 or x < 1:
                await message.channel.send('1つ目の値の範囲は1から1861までだよ\n(もしくは未実装😢)')
            elif y > 200 or y < 1:
                await message.channel.send('2つ目の値の範囲は40から1900までだよ\n(もしくは未実装😢)')
            elif y - x + 1 < 40:
                await message.channel.send('範囲がせますぎる><')
            else:
                json_file = open('/storage/emulated/0/bot/list/target.json')   # jsonを開く
                json_loaded = json.load(json_file)
                json_peeled = json_loaded["q_and_a"]   # 一番外側の{}を外してpythonのリストみたいにする
                # [ { "q" : "問題", "a": "答え" },…… ]の状態
                list = []
                count = 0
                for e in json_peeled:   # 中身のリストを作って外側のリスト(list)に込める
                    list_contents = [e.get("num"), e.get("q"), e.get("a")]   # jsonの"q"と"a"に込められている要素を取得
                    # ["問題", "答え"]の状態
                    if int(list_contents[0]) >= x and int(list_contents[0]) <= y:   # 範囲を満たすなら格納
                        list.append(list_contents)
                        # [["問題", "答え"]]の状態
                # [[ "問題", "答え" ],……]の状態
                shuffled_list = random.sample(list, 40)   # 中身のリストをシャッフル
                linked_list_q = '>>>**ターゲット模試**<<<\n'
                linked_list_a = '>>>**答え**<<<\n||'
                for i, j in enumerate(shuffled_list):   # 1文にするため文字列としてズラっと繋げていく
                    count = count + 1 
                    q_jp = j[1]   # 中身のリストの1つ目の要素 ["問題(ｺｯﾁ)", "答え"]
                    ans = j[2]   # 中身のリストの2つ目の要素 ["問題", "答え(ｺｯﾁ)"]
                    q_initial = ans[:1]   # 頭文字
                    linked_list_q = linked_list_q + '(' + str(count) + ')' + q_jp + '   ' + q_initial + '\n'
                    linked_list_a = linked_list_a + '(' + str(count) + ')' + ans + '\n'
                await message.channel.send(linked_list_q)
                await message.channel.send(linked_list_a + '||')
        elif message.content.startswith('/dragonenglish'):
            word = message.content
            splited = word.split()
            x = int(splited[1])
            y = int(splited[2]) 
            if x > 32 or x < 1:
                await message.channel.send('1つ目の値の範囲は1から91までだよ\n(もしくは未実装😢)')
            elif y > 32 or y < 1:
                await message.channel.send('2つ目の値の範囲は10から100までだよ\n(もしくは未実装😢)')
            elif y - x + 1 < 10:
                await message.channel.send('範囲がせますぎる><')
            else:
                json_file = open('/storage/emulated/0/bot/list/dragon_english.json')   # jsonを開く
                json_loaded = json.load(json_file)
                json_peeled = json_loaded["q_and_a"]   # 一番外側の{}を外してpythonのリストみたいにする
                # [ { "q" : "問題", "a": "答え" },…… ]の状態
                list = []
                count = 0
                for e in json_peeled:   # 中身のリストを作って外側のリスト(list)に込める
                    list_contents = [e.get("num"), e.get("q"), e.get("a")]   # jsonの"q"と"a"に込められている要素を取得
                    # ["問題", "答え"]の状態
                    if int(list_contents[0]) >= x and int(list_contents[0]) <= y:   # 範囲を満たすなら格納
                        list.append(list_contents)
                        # [["問題", "答え"]]の状態
                # [[ "問題", "答え" ],……]の状態
                shuffled_list = random.sample(list, 10)   # 中身のリストをシャッフル
                linked_list_q = '>>>**ドラゴンイングリッシュ模試**<<<\n'
                linked_list_a = '>>>**答え**<<<\n||'
                for i, j in enumerate(shuffled_list):   # 1文にするため文字列としてズラっと繋げていく
                    count = count + 1 
                    q_jp = j[1]   # 中身のリストの1つ目の要素 ["問題(ｺｯﾁ)", "答え"]
                    ans = j[2]   # 中身のリストの2つ目の要素 ["問題", "答え(ｺｯﾁ)"]
                    linked_list_q = linked_list_q + '(' + str(count) + ')' + q_jp + '\n'
                    linked_list_a = linked_list_a + '(' + str(count) + ')' + ans + ' [' + j[0] + ']\n'
                await message.channel.send(linked_list_q)
                await message.channel.send(linked_list_a + '||')

bot.run(token)
