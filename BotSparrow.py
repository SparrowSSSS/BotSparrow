import discord
from discord.ext import commands
import sqlite3
from discord_components import DiscordComponents, Button, ButtonStyle
from playin21 import *
from tictactoe import *
from config import *
from RPS import *
from fight import *

client=commands.Bot(command_prefix='!')

@client.event

async def on_ready():
        DiscordComponents(client)
        print(f'Бот под профилем {client.user} начал свою работу.')

@client.command(pass_context = True)

async def bot(ctx):
  if ctx.author == client.user:
        return
  else:
     regMHB_data(ctx)
     delay = await check_delay(ctx)
     if delay == True:
        dopdelay = await check_dopdelay(ctx)
        await dd(dopdelay, ctx)
     emb = discord.Embed(title = "MyHUBBot", colour = discord.Colour.orange())
     emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
     emb.add_field(name = "Дрaтyти!", value = "Я игровoй бот, созданный, чтобы вы игpaли в меня.\nСписок всех доступных команд найдёте по команде '!bothelp'.\nИспользуя меня, вы автоматически соглашаетесь с правилами моего использования, которые можно нати по команде '!botrules'.")
     msg = await ctx.send(embed = emb)
     await DeleteMessage(ctx, msg, 10)
     delay_false(ctx)

@client.command(pass_context = True)

async def bothelp(ctx):
  if ctx.author == client.user:
        return
  else:
     regMHB_data(ctx)
     delay = await check_delay(ctx)
     if delay == True:
        dopdelay = await check_dopdelay(ctx)
        await dd(dopdelay, ctx)
     emb = discord.Embed(title = "Список доступных команд", colour = discord.Colour.orange())
     emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
     emb.add_field(name = "Команды:", value = "!gamelist - выводит список игр.\n!botrules - выводит правила использования бота(рекомендую ознакомиться!).\n!gameinfo - выводит различную информацию по играм.\n!card - выводит информацию о пользователе.")
     msg = await ctx.send(embed = emb)
     await DeleteMessage(ctx, msg, 10)
     delay_false(ctx)

@client.command(pass_context = True)

async def gamelist(ctx):
  if ctx.author == client.user:
        return
  else:
     regMHB_data(ctx)
     delay = await check_delay(ctx)
     if delay == True:
        dopdelay = await check_dopdelay(ctx)
        await dd(dopdelay, ctx)
     emb = discord.Embed(title = "Список игр", colour = discord.Colour.orange())
     emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
     emb.add_field(name = "Игры:", value = "!playin21(21 очко)\n!tictactoe(крестики-нолики)\nRPS(камень,ножницы,бумага)\n!fight")
     msg = await ctx.send(embed = emb)
     await DeleteMessage(ctx, msg, 10)
     delay_false(ctx)

@client.command(pass_context = True)

async def gameinfo(ctx):
  if ctx.author == client.user:
        return
  else:
     regMHB_data(ctx)
     delay = await check_delay(ctx)
     if delay == True:
        dopdelay = await check_dopdelay(ctx)
        await dd(dopdelay, ctx)
     emb = discord.Embed(title = "Список команд, которые предоставят вам информацию о интересующих вас играх.", colour = discord.Colour.orange())
     emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
     emb.add_field(name = "Информация:", value = "!info21(21 очко)\n!infottt(крестики-нолики)\n!infoRPS(камень,ножницы,бумага)\n!infofight")
     msg = await ctx.send(embed = emb)
     await DeleteMessage(ctx, msg, 10)
     delay_false(ctx)

@client.command(pass_context = True)

async def botrules(ctx):
  if ctx.author == client.user:
        return
  else:
     regMHB_data(ctx)
     delay = await check_delay(ctx)
     if delay == True:
        dopdelay = await check_dopdelay(ctx)
        await dd(dopdelay, ctx)
     emb = discord.Embed(title = "Правила использования бота", colour = discord.Colour.orange())
     emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
     emb.add_field(name = "Правила:", value = "1.При разработке бота считалось, что игры будут проходить в отдельных чатах, поэтому, чтобы бот не засорял сообщениями важные чаты, рекомендую создать для игр отдельные.\n2.В работе бота могут присутсвовать ошибки, поэтому, если вы их заметите, прошу сообщить о них в дискорд по следующей ссылке - https://discord.gg/m8Q7BG9Dh3 \
     \n3.Разработчик не несёт ответственности за совершённые ботом критические ошибки.\n4.Бота можно спокойно распространять.\n5.Используя бота, вы автоматически соглашаетесь с правилами его использования.\n6.Если вы хотите поделиться своими идеями по улучшению бота, то вам сюда - https://discord.gg/m8Q7BG9Dh3 \n7.Данные правила могут быть в любой момент изменены разработчиком.")
     emb.set_thumbnail(url = "https://www.ccsd.ngo/ar/wp-content/uploads/2017/09/w87.jpg")
     msg = await ctx.send(embed = emb)
     await DeleteMessage(ctx, msg, 10)
     delay_false(ctx)

@client.command(pass_context = True)

async def card(ctx):
 if ctx.author == client.user:
        return
 else:
     regMHB_data(ctx)
     delay = await check_delay(ctx)
     if delay == True:
        dopdelay = await check_dopdelay(ctx)
        await dd(dopdelay, ctx)
     db = OpenMHB_data()
     sql = db.cursor()
     sql.execute(f"SELECT money FROM users_data WHERE user == '{ctx.author.name}' and server == '{ctx.message.guild.name}'")
     money = sql.fetchone()
     sql.execute(f"SELECT XP FROM users_data WHERE user == '{ctx.author.name}' and server == '{ctx.message.guild.name}'")
     XP = sql.fetchone()
     sql.execute(f"SELECT level FROM users_data WHERE user == '{ctx.author.name}' and server == '{ctx.message.guild.name}'")
     level = sql.fetchone()
     db.close()
     money = str(money)[1:-2]
     XP = str(XP)[1:-2]
     level = str(level)[1:-2]
     up = 1000 - int(XP)
     emb = discord.Embed(title = f"{ctx.author}", colour = discord.Colour.orange())
     emb.set_thumbnail(url = ctx.author.avatar_url)
     emb.add_field(name = "Информация:", value = f"1.Деньги - {money} hub bucks\n2.XP - {XP} xp\n3.Уровень - {level} level\n4.Опыта до следующего уровня - {up} xp")
     msg = await ctx.send(embed = emb)
     await DeleteMessage(ctx, msg, 10)
     delay_false(ctx)

@client.command(pass_context = True)

async def playin21(ctx):
  if ctx.author == client.user:
        return
  else:
    regMHB_data(ctx)
    delay = await check_delay(ctx)
    if delay == True:
        dopdelay = await check_dopdelay(ctx)
        await dd(dopdelay, ctx)
    bet = bet_(ctx)
    check = check_bet(ctx)
    if bet > check:
        msg = await ctx.send(f"{ctx.author.mention} Прошу прощения, у вас нет таких денег для ставки.")
        await ctx.message.delete()
        await asyncio.sleep(5)
        await msg.delete()
        return
    else:
        await game_21(ctx, client, 30, bet)
    delay_false(ctx)

@client.command(pass_context = True)

async def tictactoe(ctx):
 if ctx.author == client.user:
        return
 else:
    regMHB_data(ctx)
    delay = await check_delay(ctx)
    if delay == True:
        dopdelay = await check_dopdelay(ctx)
        await dd(dopdelay, ctx)
    bet = bet_(ctx)
    check = check_bet(ctx)
    if bet > check:
        msg = await ctx.send(f"{ctx.author.mention} Прошу прощения, у вас нет таких денег для ставки.")
        await ctx.message.delete()
        await asyncio.sleep(5)
        await msg.delete()
        return
    else:
         await ttt(ctx, client, 30, bet)
    delay_false(ctx)

@client.command(pass_context = True)

async def RPS(ctx):
 if ctx.author == client.user:
        return
 else:
    regMHB_data(ctx)
    delay = await check_delay(ctx)
    if delay == True:
        dopdelay = await check_dopdelay(ctx)
        await dd(dopdelay, ctx)
    bet = bet_(ctx)
    check = check_bet(ctx)
    if bet > check:
        msg = await ctx.send(f"{ctx.author.mention} Прошу прощения, у вас нет таких денег для ставки.")
        await ctx.message.delete()
        await asyncio.sleep(5)
        await msg.delete()
        return
    else:
         await RPS_game(ctx, client, 30, bet)
    delay_false(ctx)

@client.command(pass_context = True)

async def fight(ctx):
 if ctx.author == client.user:
        return
 else:
    regMHB_data(ctx)
    delay = await check_delay(ctx)
    if delay == True:
        dopdelay = await check_dopdelay(ctx)
        await dd(dopdelay, ctx)
    bet = bet_(ctx)
    check = check_bet(ctx)
    if bet > check:
        msg = await ctx.send(f"{ctx.author.mention} Прошу прощения, у вас нет таких денег для ставки.")
        await ctx.message.delete()
        await asyncio.sleep(5)
        await msg.delete()
        return
    else:
         await fight_game(ctx, client, 60, bet)
    delay_false(ctx)

@client.command(pass_context = True)

async def info21(ctx):
  if ctx.author == client.user:
        return
  else:
    regMHB_data(ctx)
    delay = await check_delay(ctx)
    if delay == True:
        dopdelay = await check_dopdelay(ctx)
        await dd(dopdelay, ctx)
    await info_21(ctx)
    delay_false(ctx)

@client.command(pass_context = True)

async def infottt(ctx):
  if ctx.author == client.user:
        return
  else:
    regMHB_data(ctx)
    delay = await check_delay(ctx)
    if delay == True:
        dopdelay = await check_dopdelay(ctx)
        await dd(dopdelay, ctx)
    await info_ttt(ctx)
    delay_false(ctx)

@client.command(pass_context = True)

async def infoRPS(ctx):
  if ctx.author == client.user:
        return
  else:
    regMHB_data(ctx)
    delay = await check_delay(ctx)
    if delay == True:
        dopdelay = await check_dopdelay(ctx)
        await dd(dopdelay, ctx)
    await info_RPS(ctx)
    delay_false(ctx)
   
@client.command(pass_context = True)

async def infofight(ctx):
  if ctx.author == client.user:
        return
  else:
    regMHB_data(ctx)
    delay = await check_delay(ctx)
    if delay == True:
        dopdelay = await check_dopdelay(ctx)
        await dd(dopdelay, ctx)
    await info_fight(ctx, client)
    delay_false(ctx)

client.run("OTgwNzQwMzM1NjAyOTA1MDk4.G_VGc0.4QOZsN9ej-vwoQJP87-cnwbeq4NNFJ1Ng1ESOg")