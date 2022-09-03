import discord
import asyncio
import random
from rewards import *
from discord_components import DiscordComponents, Button, ButtonStyle
from config import DeleteMessage

async def msg_delete(ctx,msg):
    await ctx.message.delete()
    await msg.delete()

async def DeleteMessages(msg0, msg1, msg2, msg3):
    await asyncio.sleep(10)
    await msg0.delete()
    await msg1.delete()
    await msg2.delete()
    await msg3.delete()

async def info_ttt(ctx):
      emb = discord.Embed(title = "Информация о игре крестики-нолики", colour = discord.Colour.orange())
      emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
      emb.add_field(name = "Информация:", value = "1.Это стандартные 'крестики нолики'.\n2.Если хотите, то можете сделать ставку.\n3.Чтобы сделать ход, выберите реакцию под сообщением, номер реакции равен номеру \
      клетки. 🚫 - реакция для того, чтобы сдаться.\n4.На выбор действия вам отводится время(30 секунд), не успели, считается, что вы сдались.\n5.Можно сделать ставку через пробел.")
      emb.set_thumbnail(url = "https://e7.pngegg.com/pngimages/112/685/png-clipart-tictactoe-online-tic-tac-toe-ludo-online-mr-ludo-board-game-android-application-package-android-purple-game.png")
      msg = await ctx.send(embed = emb)
      await DeleteMessage(ctx, msg, 10)

async def ttt(ctx, client, timeout, bet):
        DiscordComponents(client)
        player1 = ctx.author
        emb = discord.Embed(title = f"Отлично, теперь ожидаем 2 игрока!Ставка == {bet} hub bucks!", colour = discord.Colour.orange())
        emb.set_thumbnail(url = "https://e7.pngegg.com/pngimages/112/685/png-clipart-tictactoe-online-tic-tac-toe-ludo-online-mr-ludo-board-game-android-application-package-android-purple-game.png")
        emb.add_field(name = "Информация о сессии:", value = f"PLAYER1 - {player1}\nИгра - tictactoe")
        msg = await ctx.send(
            embed = emb,
            components = [
              Button(style = ButtonStyle.blue, label = "PLAYER2")
            ]
        )
        try:
          response = await client.wait_for("button_click", timeout = 15)
        except asyncio.TimeoutError:
                  await msg_delete(ctx,msg)
                  msg = await ctx.send(content = f"{ctx.author.mention} Никто не захотел с вами играть.")
                  await asyncio.sleep(5)
                  await msg.delete()
                  return
        while response.author == ctx.author:
                 try:
                   response = await client.wait_for("button_click", timeout = 15)
                 except asyncio.TimeoutError:
                   await msg_delete(ctx,msg)
                   msg = await ctx.send(content = f"{ctx.author.mention} Никто не захотел с вами играть.")
                   await asyncio.sleep(5)
                   await msg.delete()
                   return
        await msg_delete(ctx,msg)
        if response.component.label == "PLAYER2":
            player2 = response.author
            queue = random.randint(1,2)
            if queue == 1:
              pass
            else:
               player1, player2 = player2, player1
            current_player = 1
            msg0 = await ctx.send(f"{player1.mention} vs {player2.mention}")
            p1_ej = "❌"
            p2_ej = "⭕"
            board = ["blank", "blank", "blank",
                     "blank", "blank", "blank",
                     "blank", "blank", "blank",]
            reaction_emoji = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🚫"]
            emoji_list = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🚫"]
            stage = 1
            msg1 = await ctx.send(f"Сейчас ходит {player1.mention}  {p1_ej}")
            msg2 = await ctx.send(print_board(p1_ej, p2_ej, board))
            for i in range(len(emoji_list)):
                    await msg2.add_reaction(emoji_list[i])
            while check_win(p1_ej, p2_ej, board) == "blank" and stage <= 9:
                if current_player%2 != 0:
                    c_p = player1
                    enemy = player2
                    c_p_e = p1_ej
                else:
                    c_p = player2
                    enemy = player1
                    c_p_e = p2_ej
                await msg1.edit(f"Сейчас ходит {c_p.mention}  {c_p_e}")
                await msg2.edit(print_board(p1_ej, p2_ej, board))
                try:
                    reaction, user = await client.wait_for("reaction_add", timeout = timeout)
                except asyncio.TimeoutError:
                                  msg3 = await ctx.send(f"{c_p.mention} сдался!\n{enemy.mention} WIN!")
                                  xp(ctx, c_p, 25)
                                  money(c_p, enemy, ctx)
                                  await DeleteMessages(msg0, msg1, msg2, msg3)
                                  return
                while bool(user == c_p) != True:
                    await msg2.remove_reaction(member = enemy, emoji = reaction.emoji)
                    try:
                       reaction, user = await client.wait_for("reaction_add", timeout = timeout)
                    except asyncio.TimeoutError:
                                  msg3 = await ctx.send(f"{c_p.mention} сдался!\n{enemy.mention} WIN!")
                                  xp(ctx, c_p, 25)
                                  money(c_p, enemy, ctx)
                                  await DeleteMessages(msg0, msg1, msg2, msg3)
                                  return
                if str(reaction.emoji) == "🚫":
                    msg3 = await ctx.send(f"{c_p.mention} сдался!\n{enemy.mention} WIN!")
                    xp(ctx, c_p, 25)
                    money(c_p, enemy, ctx)
                    await DeleteMessages(msg0, msg1, msg2, msg3)
                    return
                else:
                    for i in range(len(reaction_emoji)):
                        if reaction_emoji[i] == reaction.emoji:
                            board[i] = c_p_e
                            await msg2.remove_reaction(member = c_p, emoji = reaction.emoji)
                            await msg2.remove_reaction(member = client.user, emoji = reaction.emoji)
                            break
                current_player += 1
                stage += 1
            await msg1.edit(f"Сейчас ходит {c_p.mention}  {c_p_e}")
            await msg2.edit(print_board(p1_ej, p2_ej, board))
            winner = check_win(p1_ej,p2_ej,board)
            if winner == p1_ej:
                msg3 = await ctx.send(f"{player1.mention} выйграл!\n{player2.mention} проиграл!")
                xp(ctx, player1, 50)
                money(player1, player2, ctx)
            elif winner == p2_ej:
                msg3 = await ctx.send(f"{player2.mention} выйграл!\n{player1.mention} проиграл!")
                xp(ctx, player2, 50)
                money(player2, player1, ctx)
            elif stage>=9:
                msg3 = await ctx.send(f"{player1.mention} vs {player2.mention}\nDRAW!")
                xp(ctx, player1, 25)
                xp(ctx, player2, 25)
            await DeleteMessages(msg0, msg1, msg2, msg3)
        else:
            return 

def check_win(p1_ej,p2_ej,board):
    line1 = check_direction(0,1,2,p1_ej,p2_ej,board)
    if line1 != "blank":
        return line1
    line2 = check_direction(3,4,5,p1_ej,p2_ej,board)
    if line2 != "blank":
        return line2
    line3 = check_direction(6,7,8,p1_ej,p2_ej,board)
    if line3 != "blank":
        return line3
    line4 = check_direction(0,3,6,p1_ej,p2_ej,board)
    if line4 != "blank":
        return line4
    line5 = check_direction(1,4,7,p1_ej,p2_ej,board)
    if line5 != "blank":
        return line5
    line6 = check_direction(2,5,8,p1_ej,p2_ej,board)
    if line6 != "blank":
        return line6
    line7 = check_direction(0,4,8,p1_ej,p2_ej,board)
    if line7 != "blank":
        return line7
    line8 = check_direction(2,4,6,p1_ej,p2_ej,board)
    if line8 != "blank":
        return line8
    return "blank"

def check_direction(pos_1,pos_2,pos_3,p1_ej,p2_ej,board):
    if (board[pos_1] == board[pos_2] == board[pos_3]) and (board[pos_1] != "blank"):
        if board[pos_1] == p1_ej:
            return p1_ej
        elif board[pos_1] == p2_ej:
            return p2_ej
    else:
        return "blank"

def print_board(p1_ej, p2_ej, board):
    blank_char = "⬜"
    msg = ""
    series = 1
    for i in range(len(board)):
        if board[i] == "blank":
            if series % 3 == 0:
                msg += blank_char + "\n"
            else:
                msg += blank_char
        if board[i] == p1_ej:
            if series % 3 == 0:
                msg += p1_ej + "\n"
            else:
                msg += p1_ej
        if board[i] == p2_ej:
            if series % 3 == 0:
                msg += p2_ej + "\n"
            else:
                msg += p2_ej
        series += 1
    return msg