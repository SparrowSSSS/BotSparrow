import discord
import asyncio
import random
from rewards import *
from discord_components import DiscordComponents, Button, ButtonStyle
from config import DeleteMessage

async def msg_delete(ctx,msg):
    await ctx.message.delete()
    await msg.delete()

async def PVP_msg_delete(msg1, msg2, msg3, msg4):
    await asyncio.sleep(10)
    await msg1.delete()
    await msg2.delete()
    await msg3.delete()
    await msg4.delete()

async def info_21(ctx):
     emb = discord.Embed(title = "Информация о игре в 21 очко", colour = discord.Colour.orange())
     emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
     emb.add_field(name = "Информация:", value = "1.Сначала вам предстоит выбрать один из двух режимов, PVB или PVP. На этом этапе вы можете не беспокоясь отменить игру.\n2.Цель игры - набрать очков больше, чем противник, но при этом не набрать больше 21 очка.\n3.В начале обоим сторонам выдаются рандомные очки, максимум - 11.\
     \n4.Если выбрали PVB, то вы всегда ходите первым и берёте очки либо пока не пасанёте, либо пока не наберёте 21 очко или больше. Потом очки набирает бот, после определяется победитель(если игрок набрал 21 очко, то бот автоматически победитель).\n5.Если выбрали PVP, то сначала нужно, чтобы 2 игрок нажал на кнопку 'PLAYER2', потом определяется, кто набирает очки первым. Когда 1 игрок набрал очки, набирает 2, в конце определяется победитель.\n6.Выигрывает та сторона, которая набрала больше очков, если один игрок набрал больше 21, то второй автоматически победитель, если очки сторон равны, то ничья.\
     \n8.Пока вы берёте очки, можно сдаться, в этом случае выигрывает противник.\n9.На выбор действия вам отводится время(30 секунд), не успели, считается, что вы сдались.\n10.В PVP вы видите очки противника.\n11.За победу вам дают XP(за победу в PVP дают больше, чем в PVB).\n12.В PVP, побеждая сдавшегося противника, вы получаете меньше опыта.\n13.В PVP есть возможность играть на игровые деньги: '!playin21 (ставка через пробел)'.")
     emb.set_thumbnail(url = "https://prognoz-telegram.ru/wp-content/uploads/photo_2019-02-22_18-01-44.jpg")
     msg = await ctx.send(embed = emb)
     await DeleteMessage(ctx, msg, 20)

async def game_21(ctx, client, timeout, bet):
        DiscordComponents(client)
        emb = discord.Embed(title = "Игра в 21 очко", colour = discord.Colour.orange())
        emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name = "Перед игрой рекомендую ознакомиться с информацией о ней по команде '!info21'\nЕсли уже ознакомились, то выберите режим:", value = "1.PVB(игра против бота)\n2.PVP(игра против другого игрока)")
        emb.set_thumbnail(url = "https://prognoz-telegram.ru/wp-content/uploads/photo_2019-02-22_18-01-44.jpg")
        msg = await ctx.send(
        embed = emb,
        components = [
            [Button(style = ButtonStyle.red, label = "PVB"),
            Button(style = ButtonStyle.blue, label = "PVP"),
            Button(style = ButtonStyle.green, label = "Отмена")]
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
        await msg_delete(ctx,msg)
        if response.component.label == "PVB":
                 player = response.author
                 go = 0
                 point=random.randint(1, 11)
                 emb = discord.Embed(title = "21 очко(PVB)", colour = discord.Colour.orange())
                 emb.set_footer(text = response.author.name, icon_url = response.author.avatar_url)
                 emb.add_field(name = f"Отлично! Игра началась.\nВаши действия?", value = f"Ваши начальные очки - {point}")
                 await response.respond(
                         embed = emb,
                         components = [
                           [Button(style = ButtonStyle.red, label = "Взять"),
                           Button(style = ButtonStyle.blue, label = "Пас"),
                           Button(style = ButtonStyle.green, label = "Сдаться")]
                         ]
                 )
                 try:
                  response = await client.wait_for("button_click", timeout = timeout)
                 except asyncio.TimeoutError:
                  await response.respond(content = f"{player.mention} сдался!\n{client.user.mention} WIN!")
                  return
                 while response.author != ctx.author:
                          try:
                              response = await client.wait_for("button_click", timeout = timeout)
                          except asyncio.TimeoutError:
                              await response.respond(content = f"{player.mention} сдался!\n{client.user.mention} WIN!")
                              return
                 if response.component.label == "Взять":
                    while response.component.label == "Взять":
                       point+=random.randint(1, 11)
                       if point >= 21:
                           await response.respond(content = f"{player.mention} набрал больше 21!\n{client.user.mention} WIN!")
                           return
                       else:
                         emb = discord.Embed(title = "21 очко(PVB)", colour = discord.Colour.orange())
                         emb.set_footer(text = response.author.name, icon_url = response.author.avatar_url)
                         emb.add_field(name = "Ваши действия?", value = f"Ваши очки - {point}")
                         await response.respond(
                             embed = emb,
                             components = [
                               [Button(style = ButtonStyle.red, label = "Взять"),
                               Button(style = ButtonStyle.blue, label = "Пас"),
                               Button(style = ButtonStyle.green, label = "Сдаться")]
                             ]
                         )
                         try:
                          response = await client.wait_for("button_click", timeout = timeout)
                         except asyncio.TimeoutError:
                          await response.respond(content = f"{player.mention} сдался!\n{client.user.mention} WIN!") 
                          return
                         while response.author != ctx.author:
                              try:
                                 response = await client.wait_for("button_click", timeout = timeout)
                              except asyncio.TimeoutError:
                                 await response.respond(content = f"{player.mention} сдался!\n{client.user.mention} WIN!")
                                 return
                         if response.component.label == "Пас":
                             botpoint = random.randint(1, 11)
                             while botpoint<point:
                               botpoint+=random.randint(1, 11)
                             if point == botpoint:
                               await response.respond(content = f"Итоговые очки бота - {botpoint}\nИтоговые очки игрока - {point}\nDRAW!")
                             elif botpoint>21:
                               await ctx.message.delete()
                               await response.respond(content = f"{client.user.mention} набрал больше 21!\n{player.mention} WIN!")
                               go = 1
                             elif botpoint>point:
                               await response.respond(content = f"Итоговые очки бота - {botpoint}\nИтоговые очки игрока - {point}\n{client.user.mention} WIN!")
                             elif point>botpoint:
                               await response.respond(content = f"Итоговые очки бота - {botpoint}\nИтоговые очки игрока - {point}\n{player.mention} WIN!")
                               go = 1
                             if go == 1:
                                xp(ctx, player, 25)
                             return
                         if response.component.label == "Сдаться":
                              await response.respond(content = f"{player.mention} сдался!\n{client.user.mention} WIN") 
                              return
                 elif response.component.label == "Пас":
                         botpoint = random.randint(1, 11)
                         while botpoint<point and botpoint < 21 and point <= 21:
                             botpoint+=random.randint(1, 11)
                         if point == botpoint:
                               await response.respond(content = f"Итоговые очки бота - {botpoint}\nИтоговые очки игрока - {point}\nDRAW!")
                         elif botpoint>21:
                               await response.respond(content = f"{client.user.mention} набрал больше 21!\n{player.mention} WIN!")
                               go = 1
                         elif botpoint>point:
                               await response.respond(content = f"Итоговые очки бота - {botpoint}\nИтоговые очки игрока - {point}\n{client.user.mention} WIN!")
                         elif point>botpoint:
                               await response.respond(content = f"Итоговые очки бота - {botpoint}\nИтоговые очки игрока - {point}\n{player.mention} WIN!")
                         if go == 1:
                                xp(ctx, player, 25)
                         return        
                 elif response.component.label == "Сдаться":
                         await response.respond(content = f"{player.mention} сдался!\n{client.user.mention} WIN")
                         return
        elif response.component.label == "PVP":
                player1 = response.author
                emb = discord.Embed(title = f"Отлично, теперь ожидаем 2 игрока!Ставка == {bet} hub bucks!", colour = discord.Colour.orange())
                emb.set_thumbnail(url = "https://prognoz-telegram.ru/wp-content/uploads/photo_2019-02-22_18-01-44.jpg")
                emb.add_field(name = "Информация о сессии", value = f"PLAYER1 - {player1}\nИгра - 21 point")
                msg0 = await ctx.send(
                    embed = emb,
                    components = [
                        Button(style = ButtonStyle.blue, label = "PLAYER2")
                    ]
                )
                try:
                   response = await client.wait_for("button_click", timeout = 15)
                except asyncio.TimeoutError:
                    await msg_delete(ctx,msg)
                    await msg0.delete()
                    msg = await ctx.send(f"{ctx.author.mention} Никто не согласился с вами играть.")
                    await asyncio.sleep(5)
                    msg.delete()
                    return
                while response.author == player1:
                    try:
                       response = await client.wait_for("button_click", timeout = 15)
                    except asyncio.TimeoutError:
                      await msg_delete(ctx,msg)
                      await msg0.delete()
                      msg = await ctx.send(f"{ctx.author.mention} Никто не согласился с вами играть.")
                      await asyncio.sleep(5)
                      msg.delete()
                      return
                if response.component.label == "PLAYER2":
                    await msg0.delete()
                    player2 = response.author
                    msg1 = await ctx.send(f"{player1.mention} vs {player2.mention}")
                    queue = random.randint(1, 2)
                    if queue == 1:
                       pass
                    else:
                        player1, player2 = player2, player1
                    current_player = 1
                    point1 = random.randint(1,11)
                    point2 = random.randint(1,11)
                    msg2 = await ctx.send(f"Сейчас ходит {player1.mention}")
                    first_emb = discord.Embed(title = "21 очко(PVP)", colour = discord.Colour.orange())
                    first_emb.set_footer(text = player1.name, icon_url = player1.avatar_url)
                    first_emb.add_field(name = f"Ваше действие?", value = f"Ваши очки - {point1}\nОчки противника - {point2}")
                    msg3 = await ctx.send(embed = first_emb)
                    while current_player <= 2:
                        if current_player == 1:
                            c_p = player1
                            enemy = player2
                            point = point1
                            e_p = point2
                        else:
                            c_p = player2
                            enemy = player1
                            point = point2
                            e_p = point1
                        new_emb = discord.Embed(title = "21 очко(PVP)", colour = discord.Colour.orange())
                        new_emb.set_footer(text = c_p.name, icon_url = c_p.avatar_url)
                        new_emb.add_field(name = f"Ваше действие?", value = f"Ваши очки - {point}\nОчки противника - {e_p}")
                        await msg2.edit(f"Сейчас ходит {c_p.mention}")
                        await msg3.edit(
                            embed = new_emb,
                            components = [
                               [Button(style = ButtonStyle.red, label = "Взять"),
                               Button(style = ButtonStyle.blue, label = "Пас"),
                               Button(style = ButtonStyle.green, label = "Сдаться")]   
                            ]
                        )
                        try:
                           response = await client.wait_for("button_click", timeout = timeout)
                        except asyncio.TimeoutError:
                          msg4 = await ctx.send(f"{c_p.mention} сдался!\n{enemy.mention} WIN!")
                          xp(ctx, c_p, 25)
                          money(c_p, enemy, ctx)
                          await PVP_msg_delete(msg1, msg2, msg3, msg4)
                          return
                        while response.author != c_p:
                            try:
                               response = await client.wait_for("button_click", timeout = timeout)
                            except asyncio.TimeoutError:
                               msg4 = await ctx.send(f"{c_p.mention} сдался!\n{enemy.mention} WIN!")
                               xp(ctx, c_p, 25)
                               money(c_p, enemy, ctx)
                               await PVP_msg_delete(msg1, msg2, msg3, msg4)
                               return
                        if response.component.label == "Взять":
                           point += random.randint(1,11)
                           if point > 21:
                             msg4 = await ctx.send(f"{c_p.mention} набрал больше 21!\n{enemy.mention} WIN!")
                             xp(ctx, c_p, 50)
                             money(c_p, enemy, ctx)
                             await PVP_msg_delete(msg1, msg2, msg3, msg4)
                             return
                           else:
                               if current_player == 1:
                                   point1 = point
                               else:
                                   point2 = point
                        elif response.component.label == "Пас":
                             current_player += 1
                        else:
                            msg4 = await ctx.send(f"{c_p.mention} сдался!\n{enemy.mention} WIN!")
                            xp(ctx, c_p, 25)
                            money(c_p, enemy, ctx)
                            await PVP_msg_delete(msg1, msg2, msg3, msg4)
                            return
                    if point1 == point2:
                        msg4 = await ctx.send(f"Итоговые очки {player1.mention} - {point1}\nИтоговые очки {player2.mention}  - {point2}\nDRAW!")
                        await PVP_msg_delete(msg1, msg2, msg3, msg4)
                        xp(ctx, player1, 25)
                        xp(ctx, player2, 25)
                        return
                    elif point1 > point2:
                        msg4 = await ctx.send(f"Итоговые очки {player1.mention} - {point1}\nИтоговые очки {player2.mention}  - {point2}\n{player1.mention} WIN!")
                        xp(ctx, player1, 50)
                        money(player1, player2, ctx)
                        await PVP_msg_delete(msg1, msg2, msg3, msg4)
                        return
                    elif point1 < point2:
                        msg4 = await ctx.send(f"Итоговые очки {player1.mention} - {point1}\nИтоговые очки {player2.mention}  - {point2}\n{player2.mention} WIN!")
                        xp(ctx, player2, 50)
                        money(player2, player1, ctx)
                        await PVP_msg_delete(msg1, msg2, msg3, msg4)
                        return
                else:
                    await ctx.message.delete()
                    await msg0.delete()
                    return
        else:
            msg = await ctx.send(content = f"{ctx.author.mention} Нет, так нет.")
            await asyncio.sleep(5)
            await msg.delete()
            return