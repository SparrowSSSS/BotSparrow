import discord
import sqlite3
import asyncio

async def DeleteMessage(ctx, msg, time):
    await asyncio.sleep(time)
    await ctx.message.delete()
    await msg.delete()

async def check_delay(ctx):
  delay = delay_true(ctx)
  if delay == 1:
      return True
  else:
      return False

async def check_dopdelay(ctx):
    db = OpenMHB_data()
    sql = db.cursor()
    sql.execute(f"SELECT dop_delay FROM delay WHERE user == '{ctx.author.name}' and server == '{ctx.message.guild.name}'")
    dop_delay = sql.fetchone()
    dop_delay = str(dop_delay)[1: -2]
    dop_delay = int(dop_delay)
    if dop_delay == 1:
      return True
    else:
      return False

async def dd(dopdelay, ctx):
    if dopdelay == True:
            await ctx.message.delete()
            msg = await ctx.send(f"{ctx.author.mention} Вам придётся подождать, пока не пропадёт предыдущий запрос!")
            await asyncio.sleep(5)
            await msg.delete()
            return
    else:
            msg = await ctx.send(f"{ctx.author.mention} Вам придётся подождать 10 секунд до того, как появится сообщение!")
            dop_delay(ctx)
            await asyncio.sleep(10)
            dop_delay(ctx)
            await msg.delete()

def bet_(ctx):
    if len(ctx.message.content) > 10:
        bet = ctx.message.content[10: ]
        try:
          bet = int(bet)
        except:
          bet = 0
    else:
        bet = 0
    return bet

def check_bet(ctx):
    db = OpenMHB_data()
    sql = db.cursor()
    sql.execute(f"SELECT money FROM users_data WHERE user == '{ctx.author.name}' and server == '{ctx.message.guild.name}'")
    check = sql.fetchone()
    check = str(check)[1:-2]
    check = int(check)
    db.close()
    return check

def regMHB_data(ctx):
        db = OpenMHB_data()
        sql = db.cursor()
        sql.execute("SELECT user FROM users_data WHERE server == '{ctx.message.guild.name}'")
        if len(sql.fetchall()) == 0:
               sql.execute(f"INSERT INTO users_data VALUES ('{ctx.message.author.name}', {0}, {10000}, '{ctx.message.guild.name}', {0})")
               db.commit()
        else:
               pass
        sql.execute(f"SELECT delay, dop_delay FROM delay WHERE user == '{ctx.message.author.name}' and server == '{ctx.message.guild.name}'")
        if len(sql.fetchall()) == 0:
            sql.execute(f"INSERT INTO delay VALUES (0, 0, '{ctx.message.guild.name}', '{ctx.message.author.name}')")
            db.commit()
        else:
            pass
        db.close()

def OpenMHB_data():
    db = sqlite3.connect('MHB_data.db')
    return db

def delay_true(ctx):
    db = OpenMHB_data()
    sql = db.cursor()
    sql.execute(f"SELECT delay FROM delay WHERE user == '{ctx.author.name}' and server == '{ctx.message.guild.name}'")
    delay = sql.fetchone()
    delay = str(delay)[1: -2]
    delay = int(delay)
    if delay == 0:
        sql.execute(F"UPDATE delay SET delay = 1 WHERE user == '{ctx.author.name}' and server == '{ctx.message.guild.name}'")
        db.commit()
    else:
        pass
    db.close()
    return delay

def delay_false(ctx):
    db = OpenMHB_data()
    sql = db.cursor()
    sql.execute(F"UPDATE delay SET delay = 0 WHERE user == '{ctx.author.name}' and server == '{ctx.message.guild.name}'")
    db.commit()
    db.close()

def dop_delay(ctx):
    db = OpenMHB_data()
    sql = db.cursor()
    sql.execute(f"SELECT dop_delay FROM delay WHERE user == '{ctx.author.name}' and server == '{ctx.message.guild.name}'")
    dop_delay = sql.fetchone()
    dop_delay = str(dop_delay)[1: -2]
    dop_delay = int(dop_delay)
    if dop_delay == 0:
        sql.execute(f"UPDATE delay SET dop_delay = 1 WHERE user == '{ctx.author.name}' and server == '{ctx.message.guild.name}'")
        db.commit()
    else:
        sql.execute(f"UPDATE delay SET dop_delay = 0 WHERE user == '{ctx.author.name}' and server == '{ctx.message.guild.name}'")
        db.commit()
    db.close()