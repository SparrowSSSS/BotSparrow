import discord
import asyncio
import random
from rewards import *
from discord_components import DiscordComponents, Button, ButtonStyle
from config import DeleteMessage

async def search_player2(ctx, res, player1, bet, client, msg):
    DiscordComponents(client)
    emb = discord.Embed(title = f"Отлично, теперь ожидаем 2 игрока!Ставка == {bet} hub bucks!", colour = discord.Colour.orange())
    emb.add_field(name = "Информация о сессии:", value = f"PLAYER1 - {player1}\nИгра - RPS\nРежим - {res}")
    emb.set_thumbnail(url = "https://i.postimg.cc/JhhCy1SR/png-RPS.png")
    msg1 = await ctx.send(
                    embed = emb,
                    components = [
                        Button(style = ButtonStyle.red, label = "PLAYER2")
                    ]
          )
    try:
        response = await client.wait_for("button_click", timeout = 15)
    except asyncio.TimeoutError:
                    await msg_delete(ctx,msg)
                    await msg1.delete()
                    msg = await ctx.send(f"{ctx.author.mention} Никто не согласился с вами играть.")
                    await asyncio.sleep(5)
                    msg.delete()
                    return
    while response.author == player1:
                    try:
                       response = await client.wait_for("button_click", timeout = 15)
                    except asyncio.TimeoutError:
                      await msg_delete(ctx,msg)
                      await msg1.delete()
                      msg = await ctx.send(f"{ctx.author.mention} Никто не согласился с вами играть.")
                      await asyncio.sleep(5)
                      msg.delete()
    await msg1.delete()
    return response.author

async def msg_delete(ctx,msg):
    await ctx.message.delete()
    await msg.delete()

async def t_msg_delete(msg, msg1, msg2, msg3):
    await asyncio.sleep(5)
    await msg.delete()
    await msg1.delete()
    await msg2.delete()
    await msg3.delete()

async def info_RPS(ctx):
    emb = discord.Embed(title = "Информация о игре камень, ножницы, бумага.", colour = discord.Colour.orange())
    emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
    emb.set_thumbnail(url = "https://i.postimg.cc/JhhCy1SR/png-RPS.png")
    emb.add_field(name = "Информация:", value = "1.Это стандартная игра 'камень, ножницы, бумага'.\n2.Чтобы сделать свой выбор, нажмите на нужную кнопку под сообщением.\n3.Есть 2 режима: до 1 победы и до 3 побед.\n3.На выбор действия вам отводится время(30 секунд), не успели, считается, что вы сдались.\
    \n4.Можно сделать ставку через пробел.\n5.🚫 означает 'сдаться'.\n6.За игру до 3 побед вы получите больше опыта.")
    msg = await ctx.send(embed = emb)
    await DeleteMessage(ctx, msg, 10)

async def RPS_game(ctx,client, timeout, bet):
    DiscordComponents(client)
    emb = discord.Embed(title = "Игра в камень, ножницы, бумага.", colour = discord.Colour.orange())
    emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
    emb.set_thumbnail(url = "https://i.postimg.cc/JhhCy1SR/png-RPS.png")
    emb.add_field(name = "Выберите один из следующих режимов:", value = "1 WIN\n3 WINS")
    msg = await ctx.send(
        embed = emb,
        components = [
        [Button(style = ButtonStyle.blue, label = "1 WIN"),
        Button(style = ButtonStyle.blue, label = "3 WINS"),
        Button(style = ButtonStyle.red, label = "Отмена")]
        ]
    )
    try:
           response = await client.wait_for("button_click", timeout = 10)
    except asyncio.TimeoutError:
                  await msg_delete(ctx,msg)
                  msg = await ctx.send(content = f"{ctx.author.mention} Нет, так нет.")
                  await asyncio.sleep(5)
                  await msg.delete()
                  return
    while response.author != ctx.author:
                  try:
                    response = await client.wait_for("button_click", timeout = 10)
                  except asyncio.TimeoutError:
                    await msg_delete(ctx,msg)
                    msg = await ctx.send(content = f"{ctx.author.mention} Нет, так нет.")
                    await asyncio.sleep(5)
                    await msg.delete()
                    return
    res = response.component.label
    player1 = response.author
    player2 = await search_player2(ctx, res, player1, bet, client, msg)
    await msg_delete(ctx,msg)
    msg = await ctx.send(f"{player1.mention} vs {player2.mention}!")
    queue = random.randint(1,2)
    if queue == 1:
            pass
    else:
            player1, player2 = player2, player1
    current_player = player1
    enemy = player2
    msg1 = await ctx.send(f"Сейчас ходит {current_player.mention}!")
    first_emb = discord.Embed(title = f"Камень, ножницы, бумага({res})", colour = discord.Colour.orange())
    first_emb.set_footer(text = current_player.name, icon_url = current_player.avatar_url)
    first_emb.add_field(name = "Выберите предмет:", value = "💎  ✂️  🧻")
    msg2 = await ctx.send(embed = first_emb)   
    if res == "1 WIN":
       winner = "None"
       while winner == "None":
        for stage in range(2):
          new_emb = discord.Embed(title = "Камень, ножницы, бумага(1 WIN)", colour = discord.Colour.orange())
          new_emb.set_footer(text = current_player.name, icon_url = current_player.avatar_url)
          new_emb.add_field(name = "Выберите предмет:", value = "💎  ✂️  🧻")
          await msg1.edit(f"Сейчас ходит {current_player.mention}!")
          await msg2.edit(
                embed = new_emb,
                components = [
                [Button(style = ButtonStyle.blue, label = "💎"),
                 Button(style = ButtonStyle.blue, label = "✂️"),
                 Button(style = ButtonStyle.blue, label = "🧻"),
                 Button(style = ButtonStyle.red, label = "🚫")]
                ]
          )
          try:
             response = await client.wait_for("button_click", timeout = timeout)
          except asyncio.TimeoutError:
                msg3 = await ctx.send(f"{current_player.mention} сдался!\n{enemy.mention} WIN!")
                xp(ctx, current_player, 25)
                money(current_player, enemy, ctx)
                await t_msg_delete(msg, msg1, msg2, msg3)
                return
          while response.author != current_player:
               try:
                   response = await client.wait_for("button_click", timeout = timeout)
               except asyncio.TimeoutError:
                msg3 = await ctx.send(f"{current_player.mention} сдался!\n{enemy.mention} WIN!")
                xp(ctx, current_player, 25)
                money(current_player, enemy, ctx)
                await t_msg_delete(msg, msg1, msg2, msg3)
                return
          emoje = response.component.label
          if emoje == "🚫":
             msg3 = await ctx.send(f"{current_player.mention} сдался!\n{enemy.mention} WIN!")
             xp(ctx, current_player, 25)
             money(current_player, enemy, ctx)
             await t_msg_delete(msg, msg1, msg2, msg3)
             return
          else:
              if current_player == player1:
                  p1_emoje = emoje
              else:
                  p2_emoje = emoje
              current_player = player2
              enemy = player1
        winner = check_winner(player1, player2, p1_emoje, p2_emoje)
        if winner == "None":
            await msg.edit(f"{player1.mention} - {p1_emoje} and {player2.mention} - {p2_emoje}, игра завершилась ничьёй, поэтому она началась заного!")
            current_player = player1
            enemy = player2
       msg3 = await ctx.send(f"{player1.mention} - {p1_emoje} and {player2.mention} - {p2_emoje}\n{winner.mention} WIN!")
       xp(ctx, current_player, 50)
       money(current_player, enemy, ctx)
       await t_msg_delete(msg, msg1, msg2, msg3)
       return
    elif res == "3 WINS":
         p1_wins = 0
         p2_wins = 0
         for wins in range(3):
             winner = "None"
             while winner == "None":
                 for stage in range(2):
                     new_emb = discord.Embed(title = "Камень, ножницы, бумага(3 WINS)", colour = discord.Colour.orange())
                     new_emb.set_footer(text = current_player.name, icon_url = current_player.avatar_url)
                     new_emb.add_field(name = "Выберите предмет:", value = f"💎  ✂️  🧻\n{player1} - {p1_wins} wins\n{player2} - {p2_wins} wins")
                     await msg1.edit(f"Сейчас ходит {current_player.mention}!")
                     await msg2.edit(
                        embed = new_emb,
                        components = [
                        [Button(style = ButtonStyle.blue, label = "💎"),
                         Button(style = ButtonStyle.blue, label = "✂️"),
                         Button(style = ButtonStyle.blue, label = "🧻"),
                         Button(style = ButtonStyle.red, label = "🚫")]
                        ]
                     )
                     try:
                       response = await client.wait_for("button_click", timeout = timeout)
                     except asyncio.TimeoutError:
                       msg3 = await ctx.send(f"{current_player.mention} сдался!\n{enemy.mention} WIN!")
                       xp(ctx, current_player, 25)
                       money(current_player, enemy, ctx)
                       await t_msg_delete(msg, msg1, msg2, msg3)
                       return
                     while response.author != current_player:
                       try:
                          response = await client.wait_for("button_click", timeout = timeout)
                       except asyncio.TimeoutError:
                          msg3 = await ctx.send(f"{current_player.mention} сдался!\n{enemy.mention} WIN!")
                          xp(ctx, current_player, 25)
                          money(current_player, enemy, ctx)
                          await t_msg_delete(msg, msg1, msg2, msg3)
                          return
                     emoje = response.component.label
                     if emoje == "🚫":
                        msg3 = await ctx.send(f"{current_player.mention} сдался!\n{enemy.mention} WIN!")
                        xp(ctx, current_player, 25)
                        money(current_player, enemy, ctx)
                        await t_msg_delete(msg, msg1, msg2, msg3)
                        return
                     else:
                        if current_player == player1:
                          p1_emoje = emoje
                        else:
                          p2_emoje = emoje
                        current_player = player2
                        enemy = player1
                 winner = check_winner(player1, player2, p1_emoje, p2_emoje)
                 if winner == "None":
                    await msg.edit(f"{player1.mention} - {p1_emoje} and {player2.mention} - {p2_emoje}, {wins + 1} раунд завершился ничьёй, поэтому он началcя заного!")
                    current_player = player1
                    enemy = player2
             await msg.edit(f"{player1.mention} - {p1_emoje} and {player2.mention} - {p2_emoje}, в {wins + 1} раунде победил {winner.mention}!")
             if winner == player1:
                 p1_wins+=1
             else:
                 p2_wins+=1
             current_player = player1
             enemy = player2
         if p1_wins > p2_wins:
             winner = player1
             enemy = player2
         else:
             winner = player2
             enemy = player1
         msg3 = await ctx.send(f"{player1.mention} - {p1_wins} wins and {player2.mention} - {p2_wins} wins\n{winner.mention} WIN!")
         xp(ctx, winner, 60)
         money(winner, enemy, ctx)
         await t_msg_delete(msg, msg1, msg2, msg3)
         return
    else:
        msg = await ctx.send(content = f"{ctx.author.mention} Нет, так нет.")
        await asyncio.sleep(5)
        await msg.delete()
        return

def check_winner(player1, player2, p1_emoje, p2_emoje):
    if (p1_emoje == "✂️" and p2_emoje == "🧻") or (p1_emoje == "💎" and p2_emoje == "✂️") or (p1_emoje == "🧻" and p2_emoje == "💎"):
        return player1
    elif (p2_emoje == "✂️" and p1_emoje == "🧻") or (p2_emoje == "💎" and p1_emoje == "✂️") or (p2_emoje == "🧻" and p1_emoje == "💎"):
        return player2
    else:
        return "None"