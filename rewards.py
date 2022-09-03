import sqlite3
from config import OpenMHB_data

def xp(ctx, player, up):
    db = OpenMHB_data()
    sql = db.cursor()
    player = str(player)[:-5]
    sql.execute(f"UPDATE users_data SET XP = XP + {up} WHERE user == '{player}' and server == '{ctx.message.guild.name}'")
    db.commit()
    sql.execute(f"SELECT XP FROM users_data WHERE user == '{player}' and server == '{ctx.message.guild.name}'")
    xp = sql.fetchone()
    xp = str(xp)[1:-2]
    xp = int(xp)
    if xp >= 1000:
       sql.execute(f"UPDATE users_data SET level = level + 1 WHERE user == '{player}' and server == '{ctx.message.guild.name}'")
       db.commit()
       sql.execute(f"UPDATE users_data SET XP = XP - 1000 WHERE user == '{player}' and server == '{ctx.message.guild.name}'")
       db.commit()
    else:
       pass
    db.close

def money(player1, player2, ctx):
    db = OpenMHB_data()
    sql = db.cursor()
    player1 = str(player1)[:-5]
    player2 = str(player2)[:-5]
    ex = len(ctx.message.content)
    if ex > 10:
        bet = ctx.message.content[10: ]
    else:
        return
    try:
        bet = int(bet)
    except:
        return
    sql.execute(f"UPDATE users_data SET money = money + {bet} WHERE user == '{player1}' and server == '{ctx.message.guild.name}'")
    db.commit()
    sql.execute(f"UPDATE users_data SET money = money - {bet} WHERE user == '{player2}' and server == '{ctx.message.guild.name}'")
    db.commit()
    db.close()
