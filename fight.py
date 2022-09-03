import discord
import asyncio
import random
from rewards import *
from discord_components import DiscordComponents, Button, ButtonStyle

async def msg_delete(ctx,msg):
    await ctx.message.delete()
    await msg.delete()

async def info_fight(ctx, client):
    DiscordComponents(client)
    emb1 = discord.Embed(title = "Основное(fight).", colour = discord.Colour.orange())
    emb1.set_footer(text = f"{ctx.author.name}\n1 из 6", icon_url = ctx.author.avatar_url)
    emb1.set_thumbnail(url = "https://banner2.cleanpng.com/20180512/vke/kisspng-battles-and-castles-free-starship-battles-conde-de-5af75eff7866c7.2122020415261611514932.jpg")
    emb1.add_field(name = "Информация:", value = "1.Выносливость увеличивается с каждым ходом на 15 единиц.\n2.Критический урон происходит либо из-за навыка, либо из-за обычной или усиленной атаки с шансом 25%\n3.Сначала оба игрока находятся на расстоянии\
    для того, чтобы его убрать нужно, чтобы кто-то подошёл и потратил из-за этого 1 ход.\n4.Игра заканчивается ничьёй на после 50 хода(1 ход заканчивается после того, как оба игрока походили).\n5.Оба игрока могут попытаться сбить противника с ног на близком расстоянии(если противник в тяжёлой броне, то шанс = 25%, если в лёгкой, то 50%)(требует 25 выносливости);\
    Быть сбитым с ног - значит пропустить свой ход.\nЛюбое оружие,кроме лука, может с 10% шансом вызвать кровотечение(отнимает 5 здоровья и 5 выносливости в течении 3 ходов).")
    emb2 = discord.Embed(title = "Оружие(1)(fight).", colour = discord.Colour.orange())
    emb2.set_footer(text = f"{ctx.author.name}\n2 из 6", icon_url = ctx.author.avatar_url)
    emb2.set_thumbnail(url = "https://banner2.cleanpng.com/20180512/vke/kisspng-battles-and-castles-free-starship-battles-conde-de-5af75eff7866c7.2122020415261611514932.jpg")
    emb2.add_field(name = "Информация:", value = "1.Щит с мечём.\n1)Обычный урон = 5 - 15; Критический урон = 20.\
    \n1)Доступен 'таран' - быстрое сокращение дистанции с возможностью сбить противника с ног и нанести ему урон(30 единиц), требует 30 единиц выносливости\
    (100% сработает и нанесёт урон и 50% собьёт с ног врага в тяжёлой броне; 50% сработает и нанесёт урон и, если сработает, 100% собьёт с ног врага в лёгкой броне).\
    \n1)Доступно 'поднять щит', который на один ход добавляет 25 единиц к защите, после этого может походить ещё раз(перезарядка в 3 хода)(требует 25 выносливости).\n1)Способность отбить удар с 30% шансом;Возможно с 80% шансом принять стрелу щитом без получения урона.")
    emb3 = discord.Embed(title = "Оружие(2)(fight).", colour = discord.Colour.orange())
    emb3.set_footer(text = f"{ctx.author.name}\n3 из 6", icon_url = ctx.author.avatar_url)
    emb3.set_thumbnail(url = "https://banner2.cleanpng.com/20180512/vke/kisspng-battles-and-castles-free-starship-battles-conde-de-5af75eff7866c7.2122020415261611514932.jpg")
    emb3.add_field(name = "Информация:", value = "2.Двуручный меч.\n2)Обычный урон = 10 - 15;Критический урон = 35;Усиленный удар, наносящий 15 - 30 единиц урона(50% урона игнорирует защиту, возможно спарировать, нельзя отбить)(требует 25 выносливости).\
    \n2)Есть возможность парировать удары с 25% шансом(наносит 15 урона, отменяет удар оружием врага и работает при наличии 20 выносливости)\n2)Способность встать в защитную стойку, которая добавит 20 единиц защиты\
    (требует 30 выносливости)(перезарядка в 3 хода);Способность отбить удар с 30% шансом.")
    emb4 = discord.Embed(title = "Оружие(3)(fight).", colour = discord.Colour.orange())
    emb4.set_footer(text = f"{ctx.author.name}\n4 из 6", icon_url = ctx.author.avatar_url)
    emb4.set_thumbnail(url = "https://banner2.cleanpng.com/20180512/vke/kisspng-battles-and-castles-free-starship-battles-conde-de-5af75eff7866c7.2122020415261611514932.jpg")
    emb4.add_field(name = "Информация:", value = "3.Алебарда.\n3)Обычный урон = 5 - 20;Критический урон = 30;Усиленный удар, наносящий 20 - 25 урона(60% урона игнорирует защиту, нельзя спарировать, можно отбить)(требует 30 выносливости).\
    \n3)Можно исполизовать 'таран алебардой' - быстрое сокращение дистанции с возможностью сбить противника с ног и нанести ему урон(35 единиц), требует 30 единиц выносливости(100% сработает и нанесёт урон и 50% собьёт с ног врага в тяжёлой броне; 50% сработает и нанесёт урон и, если сработает, 100% собьёт с ног врага в лёгкой броне).\
    \n3)Можно использовать 'стену копий' - как только противник попытается атаковать, вы с 80% шансом прервёте его атаку и нанесёте урон в 15 единиц(действует 1 ход)(требует 25 выносливости)\n3)Есть возможность отбить удар с 25% шансом.")
    emb5 = discord.Embed(title = "Оружие(4 - 5)(fight).", colour = discord.Colour.orange())
    emb5.set_footer(text = f"{ctx.author.name}\n5 из 6", icon_url = ctx.author.avatar_url)
    emb5.set_thumbnail(url = "https://banner2.cleanpng.com/20180512/vke/kisspng-battles-and-castles-free-starship-battles-conde-de-5af75eff7866c7.2122020415261611514932.jpg")
    emb5.add_field(name = "Информация:", value = "4.Лук и парные клинки\n4)Способность выстрелить на расстоянии от противника и с 80% шансом попасть по нему(наносит 25-40 обычного урона и 50 единиц крита)\n4)Чтобы отойти от противника на расстояние и выстрелить нужно потратить всю выносливость, но не меньше 50 единиц(есть вероятность в 25%, что не получится и протиник нанесёт урон в 15 ед.).\
    \n4)В ближнем бою используются парные клинки;Обычный урон = 10 - 20;Критический урон = 25;Клинки не могут ни отбить, ни парировать удары\n4)В ближнем бою можно уклонится(если тяжёлая броня - 10% шанс, если лёгкая - 20% шанс).\
    \n4)В ближнем бою можно сделать выпад и нанести клинками критический урон(требует 30 единиц выносливости)(вызывает кровотечение).\n5.Парные мечи.\n5)Обычный урон = 15 - 30;Критический урон = 35\n5)Можно встать в защитную стойку и добавить 30 единиц к защите, требует 40 единиц выносливости(перезарядка в 3 хода)\
    ;Способность отбить удар с 30% шансом\n5)Спозобность использовать 'множество игл' - многократные удары мечами по противнику(сработает с 70% шансом, если не сработает, то персонаж получает 20 единиц урона)(требует 40 выносливости)(наносит 40 единиц урона).")
    emb6 = discord.Embed(title = "Броня(fight).", colour = discord.Colour.orange())
    emb6.set_footer(text = f"{ctx.author.name}\n6 из 6", icon_url = ctx.author.avatar_url)
    emb6.set_thumbnail(url = "https://banner2.cleanpng.com/20180512/vke/kisspng-battles-and-castles-free-starship-battles-conde-de-5af75eff7866c7.2122020415261611514932.jpg")
    emb6.add_field(name = "Информация:", value = "1.Лёгкая броня.\n1)hp = 100\n1)Выносливость = 100(максимум 100)\n1)Защита от оружия = 25\n2.Тяжёлая броня.\n2)hp = 150\n2)Выносливость = 50(максимум 50)\n2)Защита от оружия = 25")
    embed = [emb1, emb2, emb3, emb4, emb5, emb6]
    number = 0
    msg = await ctx.send(embed = embed[number])
    status = True
    while status == True:
        await msg.edit(embed = embed[number],
                 components = [
                     [Button(style = ButtonStyle.blue, label = "⬅️"),
                      Button(style = ButtonStyle.blue, label = "➡️"),
                      Button(style = ButtonStyle.red, label = "🚫")]            
                 ]       
         )
         
        try:
           response = await client.wait_for("button_click", timeout = 60)
        except asyncio.TimeoutError:
           await msg_delete(ctx,msg)
           return
        while response.author != ctx.author:
                  try:
                    response = await client.wait_for("button_click", timeout = 60)
                  except asyncio.TimeoutError:
                    await msg_delete(ctx,msg)
                    return
        if response.component.label == "🚫":
            await msg_delete(ctx,msg)
            return
        elif response.component.label == "⬅️":
         if number == 0:
            number = 5
         else:
            number -= 1
        else:
            if number == 5:
               number = 0
            else:
               number += 1

async def DeleteMessages(msg, msg0, msg1):
    await msg0.delete()
    await msg1.delete()
    await asyncio.sleep(5)
    await msg.delete()

async def fight_game(ctx, client, timeout, bet):
    DiscordComponents(client)
    player1 = ctx.author
    emb = discord.Embed(title = f"Отлично, теперь ожидаем 2 игрока!Ставка == {bet} hub bucks!", colour = discord.Colour.orange())
    emb.add_field(name = "Информация о сессии:", value = f"PLAYER1 - {player1}\nИгра - fight")
    emb.set_thumbnail(url = "https://banner2.cleanpng.com/20180512/vke/kisspng-battles-and-castles-free-starship-battles-conde-de-5af75eff7866c7.2122020415261611514932.jpg")
    emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
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
            msg = await ctx.send(f"{player1.mention} vs {player2.mention}!")
            msg0 = await ctx.send(f"{player1.mention}, выберите себе броню!")
            first_emb = discord.Embed(title = "Список брони", colour = discord.Colour.orange())
            first_emb.set_footer(text = player1.name, icon_url = player1.avatar_url)
            first_emb.add_field(name = "Лёгкая броня", value = "hp = 100;\nВыносливость = 100;\nНачальная защита от оружия = 25;")
            first_emb.add_field(name = "Тяжёлая броня", value = "hp = 150;\nВыносливость = 50;\nНачальная защита от оружия = 25;")
            msg1 = await ctx.send(embed = first_emb)
            player = player1
            for i in range(2):
                await msg0.edit(f"{player.mention}, выберите себе броню!")
                new1_emb = discord.Embed(title = "Список брони", colour = discord.Colour.orange())
                new1_emb.set_footer(text = player.name, icon_url = player.avatar_url)
                new1_emb.add_field(name = "Лёгкая броня", value = "hp = 100;\nВыносливость = 100;\nНачальная защита от оружия = 25;")
                new1_emb.add_field(name = "Тяжёлая броня", value = "hp = 150;\nВыносливость = 50;\nНачальная защита от оружия = 25;")
                await msg1.edit(
                    embed = new1_emb,
                    components = [
                        [Button(style = ButtonStyle.blue, label = "ЛЁГКАЯ"),
                         Button(style = ButtonStyle.red, label = "ТЯЖЁЛАЯ")]
                    ]
                )
                message = f"{player.mention} Решил не продолжать игру!"
                try:
                   res = await client.wait_for("button_click", timeout = 30)
                except asyncio.TimeoutError:
                   await msg.edit(message)
                   await DeleteMessages(msg, msg0, msg1)
                   return
                while res.author != player:
                   try:
                      res = await client.wait_for("button_click", timeout = 30)
                      return res
                   except asyncio.TimeoutError:
                      await msg.edit(message)
                      await DeleteMessages(msg, msg0, msg1)
                      return
                player_def = 25
                if res.component.label == "ЛЁГКАЯ":
                    player_hp = 100
                    player_stamina = 100
                    player_max_stamina = 100
                    player_armor = "лёгкая броня"
                else:
                    player_hp = 150
                    player_stamina = 50
                    player_max_stamina = 50
                    player_armor = "тяжёлая броня"
                await msg0.edit(f"{player.mention}, теперь выберите оружие!")
                new2_emb = discord.Embed(title = "Выбор оружия", colour = discord.Colour.orange())
                new2_emb.set_footer(text = player.name, icon_url = player.avatar_url)
                new2_emb.add_field(name = "Информация:", value = "Описание каждого оружия найдёте по каманде '!infofight'!")
                await msg1.edit(
                    embed = new2_emb,
                    components = [
                        [Button(style = ButtonStyle.blue, label = "Щит с мечём"),
                         Button(style = ButtonStyle.blue, label = "Двуручный меч"),
                         Button(style = ButtonStyle.blue, label = "Алебарда"),
                         Button(style = ButtonStyle.blue, label = "Лук и парные клинки"),
                         Button(style = ButtonStyle.blue, label = "Парные мечи")]
                    ]
                )
                try:
                   res = await client.wait_for("button_click", timeout = 30)
                except asyncio.TimeoutError:
                   await msg.edit(message)
                   await DeleteMessages(msg, msg0, msg1)
                   return
                while res.author != player:
                   try:
                      res = await client.wait_for("button_click", timeout = 30)
                   except asyncio.TimeoutError:
                      await msg.edit(message)
                      await DeleteMessages(msg, msg0, msg1)
                      return
                if res.component.label == "Щит с мечём":
                    player_weapons = "щит с мечём"
                    player_cd = 20
                    player_fight_of = 30
                elif res.component.label == "Двуручный мечь":
                    player_weapons = "двуручный меч"
                    player_cd = 35
                    player_fight_of = 30
                elif res.component.label == "Алебарда":
                    player_weapons = "алебарда"
                    player_cd = 30
                    player_fight_of = 25
                elif res.component.label == "Лук и парные клинки":
                    player_weapons = "лук и парные клинки"
                    player_cd = 30
                    if player_armor == "лёгкая броня":
                        player_fight_of = 20
                    else:
                        player_fight_of = 10
                else:
                    player_weapons = "парные мечи"
                    player_cd = 35
                    player_fight_of = 30
                if player == player1:
                    p1_armor = player_armor
                    p1_hp = player_hp
                    p1_stamina = player_stamina
                    p1_max_s = player_max_stamina
                    p1_def = player_def
                    p1_weapons = player_weapons
                    if p1_weapons == "алебарда":
                       p1_sw = False
                    if p1_weapons == "щит с мечём":
                        p1_sb = False
                        p1_sb_rech = 0
                    if p1_weapons == "двуручный меч" or p1_weapons == "парные мечи":
                       p1_ps_rech = 0
                    p1_cd = player_cd
                    p1_f_o = player_fight_of
                else:
                    p2_armor = player_armor
                    p2_hp = player_hp
                    p2_stamina = player_stamina
                    p2_max_s = player_max_stamina
                    p2_def = player_def
                    p2_weapons = player_weapons
                    if p2_weapons == "алебарда":
                       p2_sw = False
                    if p2_weapons == "щит с мечём":
                       p2_sb = False
                       p2_sb_rech = 0
                    if p2_weapons == "двуручный меч" or p2_weapons == "парные мечи":
                       p2_ps_rech = 0
                    p2_cd = player_cd
                    p2_f_o = player_fight_of
                player = player2
            current_player = 1
            distance = True
            p1_bleeding = 0
            p2_bleeding = 0
            p1_stun = False
            p2_stun = False
            move = 1
            logs = ["0.Игра только началась."]
            while (p1_hp > 0 and p2_hp > 0) and move <= 100:
                p1_stamina += 15
                p2_stamina += 15
                if p1_stamina > p1_max_s:
                   p1_stamina -= (p1_stamina - p1_max_s)
                if p2_stamina > p2_max_s:
                   p2_stamina -= (p2_stamina - p2_max_s)
                if p1_bleeding > 0:
                    p1_hp -= 5
                    p1_stamina -= 5
                    p1_bleeding -= 1
                if p2_bleeding > 0:
                    p2_hp -= 5
                    p2_stamina -= 5
                    p2_bleeding -= 1
                if current_player % 2 != 0:
                    cp = player1
                    cp_bleeding = p1_bleeding
                    cp_stun = p1_stun
                    cp_weapons = str(p1_weapons)
                    if p1_weapons == "алебарда":
                       cp_sw = False
                    if p1_weapons == "щит с мечём":
                        if p1_sb == True:
                           p1_sb = False
                           cp_def -= 25
                        p1_sb_rech -= 1
                        cp_sb_rech = p1_sb_rech
                    if p1_weapons == "двуручный меч" or p1_weapons == "парные мечи":
                       p1_ps_rech -= 1
                       cp_ps_rech = p1_ps_rech
                    cp_armor = p1_armor
                    cp_hp = p1_hp
                    cp_def = p1_def
                    cp_stamina = p1_stamina
                    cp_max_s = p1_max_s
                    cp_cd = p1_cd
                    en = player2
                    en_bleeding = p2_bleeding
                    en_stun = p2_stun
                    en_hp = p2_hp
                    en_def = p2_def
                    en_stamina = p2_stamina
                    en_max_s = p2_max_s
                    en_weapons = str(p2_weapons)
                    if p2_weapons == "двуручный меч":
                       if en_stamina >= 20:
                          en_parry = True
                       else:
                          en_parry = False
                    if p2_weapons == "алебарда":
                       en_sw = p2_sw
                    en_armor = p2_armor
                    en_f_0 = p2_f_o
                else:
                    cp = player2
                    cp_bleeding = p2_bleeding
                    cp_stun = p2_stun
                    cp_weapons = str(p2_weapons)
                    if p2_weapons == "алебарда":
                       cp_sw = False
                    if p2_weapons == "щит с мечём":
                        if p2_sb == True:
                           p2_sb = False
                           cp_def -= 25
                        p2_sb_rech -= 1
                        cp_sb_rech = p2_sb_rech
                    if p2_weapons == "двуручный меч" or p2_weapons == "парные мечи":
                       p2_ps_rech -= 1
                       cp_ps_rech = p2_ps_rech
                    cp_armor = p2_armor
                    cp_hp = p2_hp
                    cp_def = p2_def
                    cp_stamina = p2_stamina
                    cp_max_s = p2_max_s
                    cp_cd = p2_cd
                    cp_f_o = p2_f_o
                    en = player1
                    en_bleeding = p1_bleeding
                    en_stun = p1_stun
                    en_hp = p1_hp
                    en_def = p1_def
                    en_stamina = p1_stamina
                    en_max_s = p1_max_s
                    en_weapons = str(p1_weapons)
                    if p1_weapons == "двуручный меч":
                       if en_stamina >= 20:
                          en_parry = True
                       else:
                          en_parry = False
                    if p1_weapons == "алебарда":
                       en_sw = p1_sw
                    en_armor = p1_armor
                    en_f_o = p1_f_o
                game_emb = discord.Embed(title = "Да победит же сильнейший!", colour = discord.Colour.orange())
                game_emb.add_field(name = f"{player1.name}", value = f"Броня - {p1_armor};\nОружие - {p1_weapons};\n❤️ {p1_hp};\nВыносливость - {p1_stamina}/{p1_max_s};\n⚔️ {p1_def};\nБудет терять кровь {p1_bleeding} ходов;")
                game_emb.add_field(name = f"{player2.name}", value = f"Броня - {p2_armor};\nОружие - {p2_weapons};\n❤️ {p2_hp};\nВыносливость - {p2_stamina}/{p2_max_s};\n⚔️ {p2_def};\nБудет терять кровь {p2_bleeding} ходов;")
                game_emb.set_thumbnail(url = "https://banner2.cleanpng.com/20180512/vke/kisspng-battles-and-castles-free-starship-battles-conde-de-5af75eff7866c7.2122020415261611514932.jpg")
                if distance == True:
                   game_emb.set_footer(text = f"Предыдущий ход: {logs[-1]}\nИгроки находятся на расстоянии!")
                else:
                   game_emb.set_footer(text = f"Предыдущий ход: {logs[-1]}")
                if cp_stun == True:
                   logs.append(f"{move}.{cp.name} пропустил свой ход, так как был сбит с ног.")
                   cp_stun = False
                else:
                    await msg0.edit(f"Сейчас ходит {cp.mention}!")
                    buttons = components_but(distance, cp_weapons)
                    await msg1.edit(
                          embed = game_emb,
                          components = buttons
                    )
                    response = 1
                    while response == 1:
                     try:
                        res = await client.wait_for("button_click", timeout = timeout)
                     except asyncio.TimeoutError:
                        logs.append(f"{move}.{cp.name} думал над своим ходом слишком долго, поэтому он его пропустил.")
                        break
                     while res.author != cp:
                        try:
                           res = await client.wait_for("button_click", timeout = timeout)
                        except asyncio.TimeoutError:
                           logs.append(f"{move}.{cp.name} думал над своим ходом слишком долго, поэтому он его пропустил.")
                           response = 0
                        if response == 0:
                           break
                     if res.component.label == "Атаковать":
                        if en_weapons == "алебарда":
                          check = check_chance(80)
                          if en_sw == True and check == True:
                                ret = cp_damage(15, cp_def, cp_hp, cp_bleeding)
                                cp_def = ret[0]
                                cp_hp = ret[1]
                                cp_bleeding = ret[2]
                                logs.append(f"{move}.{cp.name} попытался атаковать противника, но {en.name} прервал атаку ударом алебарды, нанеся 15 ед. урона.")
                                break
                        elif en_weapons == "двуручный меч":
                            check = check_chance(25)
                            if en_parry == True and check == True:
                                  en_stamina -= 20
                                  ret = cp_damage(15, cp_def, cp_hp, cp_bleeding)
                                  cp_def = ret[0]
                                  cp_hp = ret[1]
                                  cp_bleeding = ret[2]
                                  logs.append(f"{move}.{cp.name} попытался атаковать противника, но {en.name} парировал удар и нанёс ему 15 ед. урона.")
                                  break
                        check = check_chance(en_f_o)
                        if check == True:
                             logs.append(f"{move}.{cp.name} попытался атаковать противника, но {en.name} отбил удар.")
                             break
                        else:
                            check = check_chance(25)
                            if check == True:
                                ret = en_damage(cp_cd, en_def, en_hp, en_bleeding)
                                logs.append(f"{move}.{cp.name} атаковал противника и нанёс ему критический урон в {cp_cd} единиц.")
                            else:
                                damage = normal_damage(cp_weapons)
                                ret = en_damage(damage, en_def, en_hp, en_bleeding)
                                logs.append(f"{move}.{cp.name} атаковал противника и нанёс ему обычный урон в {damage} единиц.")
                            en_def = ret[0]
                            en_hp = ret[1]
                            en_bleeding = ret[2]
                            break
                     elif res.component.label == "Пнуть":
                        if cp_stamina >= 25:
                         if en_armor == "лёгкая броня":
                            chance = 50
                         else:
                            chance = 25
                         check = check_chance(chance)
                         if check == True:
                            en_stun = True
                            logs.append(f"{move}.{cp.name} пнул противника и сбил его с ног.")
                         else:
                            check = check_chance(50)
                            if check == True:
                               cp_stun = True
                               logs.append(f"{move}.{cp.name} попытался сбить с ног противника, но {en.name} сбил его в ответ.")
                            else:
                               logs.append(f"{move}.{cp.name} пнул противника, но это на него никак не подействовало.")
                         break
                         cp_stamina -= 25
                        else:
                          await msg.edit(f"{cp.mention}, вам не хватает 25 выносливости для пинка!")
                          continue
                     elif res.component.label == "Сдаться":
                         await msg.edit(f"{cp.mention} склонил голову перед {en.mention}, но тот одной атакой лишил его жизни!\nЗрители в шоке, {en.mention} WIN!")
                         await DeleteMessages(msg, msg0, msg1)
                         xp(ctx, en, 50)
                         money(en, cp, ctx)
                         return
                     elif res.component.label == "Логи":
                         message = ""
                         for i in range(len(logs)):
                             message += logs[i] + "\n"
                         await res.respond(content = message)
                         continue
                     elif res.component.label == "Приблизиться":
                          logs.append(f"{move}.{cp.name} приблизился к противнику.")
                          distance = False
                          break
                     elif res.component.label == "Защитная стойка":
                          if cp_weapons == "двуручный меч":
                              number = 20
                              stamina = 30
                          else:
                              number = 30
                              stamina = 40
                          if cp_ps_rech <= 0:
                            if cp_stamina >= stamina:
                              cp_stamina -= stamina
                              cp_def += number
                              if cp == player1:
                                 p1_sb_rech = 3
                              else:
                                 p2_sb_rech = 3
                              logs.append(f"{move}.{cp.name} встал в защитную стойку и прибавил себе {number} ед. защиты.")
                              break
                            else:
                              await msg.edit(f"{cp.mention}, у вас нету {stamina} выносливости для активации навыка!")
                              continue
                          else:
                              await msg.edit(f"{cp.mention}, у данного навыка перезарядка(ещё {cp_ps_rech} ходов), вы не можете его использовать!")
                              continue
                     elif res.component.label == "Поднять щит":
                      if cp_stamina >= 25:
                        if cp_sb_rech > 0:
                          await msg.edit(f"{cp.mention}, у данного навыка перезарядка(ещё {cp_sb_rech} ходов), вы не можете его использовать!")
                          continue
                        else:
                            if cp == player1:
                                p1_sb = True
                                p1_sb_rech = 3
                            else:
                                p2_sb = True
                                p2_sb_rech = 3
                            cp_def += 25
                            cp_stamina -= 25
                            logs.append(f"{move}.{cp.name} поднял щит и прибавил к себе 25 ед. защиты на 1 ход.")
                            game_emb1 = discord.Embed(title = "Да победит же сильнейший!", colour = discord.Colour.orange())
                            game_emb1.add_field(name = f"{cp.name}", value = f"Броня - {cp_armor};\nОружие - {cp_weapons};\n❤️ {cp_hp};\nВыносливость - {cp_stamina}/{cp_max_s};\n⚔️ {cp_def};\nБудет терять кровь {cp_bleeding} ходов;")
                            game_emb1.add_field(name = f"{en.name}", value = f"Броня - {en_armor};\nОружие - {en_weapons};\n❤️ {en_hp};\nВыносливость - {en_stamina}/{en_max_s};\n⚔️ {en_def};\nБудет терять кровь {en_bleeding} ходов;")
                            game_emb1.set_thumbnail(url = "https://banner2.cleanpng.com/20180512/vke/kisspng-battles-and-castles-free-starship-battles-conde-de-5af75eff7866c7.2122020415261611514932.jpg")
                            game_emb1.set_footer(text = f"Предыдущий ход: {logs[-1]}")
                            await msg1.edit(
                                  embed = game_emb1,
                                  components = buttons
                            )
                            continue
                      else:
                        await msg.edit(f"{cp.mention}, у вас нету 25 выносливости для этого!")
                        continue
                     elif res.component.label == "Таран":
                          if cp_stamina >= 30:
                             distance = False
                             cp_stamina -= 30
                             if en_armor == "лёгкая броня":
                                check = check_chance(50)
                                if check == True:
                                   en_stun = True
                                   ret = en_damage(30, en_def, en_hp, en_bleeding)
                                   en_def = ret[0]
                                   en_hp = ret[1]
                                   en_bleeding = ret[2]
                                   logs.append(f"{move}.{cp.name} протаранил противника, сбил его с ног и нанёс 30 ед. урона.")
                                else:
                                   logs.append(f"{move}.{cp.name} попытался протаранить противника, но тот успел увернуться.")
                                break
                             else:
                                check = check_chance(50)
                                if check == True:
                                   en_stun = True
                                   logs.append(f"{move}.{cp.name} протаранил противника, сбил его с ног и нанёс 30 ед. урона.")
                                else:
                                   logs.append(f"{move}.{cp.name} протаранил противника, нанёс ему урон в 30 ед., но не смог сбить с ног.")
                                ret = en_damage(30, en_def, en_hp, en_bleeding)
                                en_def = ret[0]
                                en_hp = ret[1]
                                en_bleeding = ret[2]
                                break
                          else:
                                await msg.edit(f"{cp.mention}, у вас нету 30 выносливости для этого!")
                                continue
                     elif res.component.label == "Усиленный удар":
                        if cp_weapons == "алебарда":
                            stamina = 30
                        else:
                            stamina = 25
                        if cp_stamina >= stamina:
                            cp_stamina -= stamina
                            if en_weapons == "алебарда":
                              check = check_chance(80)
                              if en_sw == True and check == True:
                                ret = cp_damage(15, cp_def, cp_hp, cp_bleeding)
                                cp_def = ret[0]
                                cp_hp = ret[1]
                                cp_bleeding = ret[2]
                                logs.append(f"{move}.{cp.name} усиленно атаковал, но {en.name} прервал атаку ударом алебарды, нанеся 15 ед. урона.")
                                break
                            elif en_weapons == "двуручный меч" and cp_weapons == "двуручный меч":
                                check = check_chance(25)
                                if en_parry == True and check == True:
                                  en_stamina -= 20
                                  ret = cp_damage(15, cp_def, cp_hp, cp_bleeding)
                                  cp_def = ret[0]
                                  cp_hp = ret[1]
                                  cp_bleeding = ret[2]
                                  logs.append(f"{move}.{cp.name} усиленно атаковал, но {en.name} парировал удар и нанёс ему 15 ед. урона.")
                                  break
                            if cp_weapons == "двуручный меч":
                               damage = emp_damage(cp_weapons)
                               logs.append(f"{move}.{cp.name} усиленно атаковал противника и нанёс ему урон в {damage} единиц.")
                               break
                            else:
                               check = check_chance(en_f_o)
                               if check == True:
                                 logs.append(f"{move}.{cp.name} усиленно атаковал, но {en.name} отбил удар.")
                               else:
                                 check = check_chance(25)
                                 if check == True:
                                   ret = en_damage(cp_cd, en_def, en_hp, en_bleeding)
                                   en_def = ret[0]
                                   en_hp = ret[1]
                                   en_bleeding = ret[2]
                                   logs.append(f"{move}.{cp.name} усиленно атаковал противника и нанёс ему критический урон в {cp_cd} единиц.")
                                 else:
                                   damage = emp_damage(cp_weapons)
                                   logs.append(f"{move}.{cp.name} усиленно атаковал противника и нанёс ему урон в {damage} единиц.")
                               break
                        else:
                            await msg.edit(f"{cp.mention}, у вас нету {stamina} выносливости для этого!")
                            continue
                     elif res.component.label == "Таран алебардой":
                            if cp_stamina >= 30:
                               distance = False
                               cp_stamina -= 30
                               if en_armor == "лёгкая броня":
                                check = check_chance(50)
                                if check == True:
                                   en_stun = True
                                   ret = en_damage(35, en_def, en_hp, en_bleeding)
                                   en_def = ret[0]
                                   en_hp = ret[1]
                                   en_bleeding = ret[2]
                                   logs.append(f"{move}.{cp.name} протаранил противника алебардой, сбил его с ног и нанёс 35 ед. урона.")
                                else:
                                   logs.append(f"{move}.{cp.name} попытался протаранить противника алебардой, но тот успел увернуться.")
                                break
                               else:
                                check = check_chance(50)
                                if check == True:
                                   en_stun = True
                                   logs.append(f"{move}.{cp.name} протаранил противника алебардой, сбил его с ног и нанёс 35 ед. урона.")
                                else:
                                   logs.append(f"{move}.{cp.name} протаранил противника алебардой, нанёс ему урон в 35 ед., но не смог сбить с ног.")
                                ret = en_damage(35, en_def, en_hp, en_bleeding)
                                en_def = ret[0]
                                en_hp = ret[1]
                                en_bleeding = ret[2]
                                break
                            else:
                                await msg.edit(f"{cp.mention}, у вас нету 30 выносливости для этого!")
                                continue
                     elif res.component.label == "Стена копий":
                        if cp_stamina >= 25:
                           cp_stamina -= 25
                           cp_sw = True
                           logs.append(f"{move}.{cp.name} использовал 'стену' копий.")
                        else:
                            await msg.edit(f"{cp.mention}, у вас нету 25 выносливости для этого!")
                            continue
                     elif res.component.label == "Выстрелить":
                        check = check_chance(80)
                        if check == True:
                            if en_weapons == "щит с мечём":
                              check = check_chance(80)
                              if check == True:
                                 logs.append(f"{move}.{cp.name} выстрелил в противника, но {en.name} поймал стрелу щитом.")
                                 break
                            check = check_chance(25)
                            if check == True:
                                ret = en_damage(cp_cd, en_def, en_hp, en_bleeding)
                                logs.append(f"{move}.{cp.name} выстрелил в противника и нанёс ему критический урон в {cp_cd} единиц.")
                            else:
                                damage = normal_damage(cp_weapons)
                                ret = en_damage(damage, en_def, en_hp, en_bleeding)
                                logs.append(f"{move}.{cp.name} выстрелил в противника и нанёс ему урон в {damage} единиц.")
                            en_def = ret[0]
                            en_hp = ret[1]
                            en_bleeding = ret[2]
                            break
                        else:
                            logs.append(f"{move}.{cp.name} выстрелил в противника, но не попал.")
                            break
                     elif res.component.label == "Выпад":
                        if cp_stamina >= 30:
                            cp_stamina -= 30
                            ret = en_damage(cp_cd, en_def, en_hp, en_bleeding)
                            en_def = ret[0]
                            en_hp = ret[1]
                            en_bleeding = ret[2]
                            if cp_bleeding < 0:
                               cp_bleeding = 3
                            logs.append(f"{move}.{cp.name} совершил выпад и нанёс противнику критический урон в {cp_cd} единиц, а также вызвал кровотечение.")
                            break
                        else:
                            await msg.edit(f"{cp.mention}, у вас нету 30 выносливости для этого!")
                            continue
                     elif res.component.label == "Отойти и выстрелить":
                        if cp_stamina >= 50:
                          check = check_chance(25)
                          if check == True:
                            ret = en_damage(15, en_def, en_hp, en_bleeding)
                            en_def = ret[0]
                            en_hp = ret[1]
                            en_bleeding = ret[2]
                            logs.append(f"{move}.{cp.name} попытался отойти и выстрелить, но {en.name} помешал ему и нанёс урон в 15 единиц.")
                            break
                          else:
                            cp_stamina = 0
                            distance = True
                            check = check_chance(80)
                            if check == True:
                                if en_weapons == "щит с мечём":
                                   check = check_chance(80)
                                   if check == True:
                                      logs.append(f"{move}.{cp.name} отошёл и выстрелил в противника, но {en.name} поймал стрелу щитом.")
                                      break
                                check = check_chance(25)
                                if check == True:
                                    ret = en_damage(cp_cd, en_def, en_hp, en_bleeding)
                                    logs.append(f"{move}.{cp.name} отошёл и выстрелил в противника, нанеся ему критический урон в {cp_cd} единиц.")
                                else:
                                    damage = normal_damage(cp_weapons)
                                    ret = en_damage(damage, en_def, en_hp, en_bleeding)
                                    logs.append(f"{move}.{cp.name} отошёл и выстрелил в противника, нанеся ему урон в {damage} единиц.")
                                en_def = ret[0]
                                en_hp = ret[1]
                                en_bleeding = ret[2]
                                break
                            else:
                                logs.append(f"{move}.{cp.name} отошёл и выстрелил в противника, но не попал.")
                                break
                        else:
                            await msg.edit(f"{cp.mention}, у вас нету 50 выносливости для этого!")
                            continue
                     elif res.component.label == "Множество игл":
                        if cp_stamina >= 40:
                            check = check_chance(70)
                            if check == True:
                                cp_stamina -= 40
                                ret = en_damage(40, en_def, en_hp, en_bleeding)
                                en_def = ret[0]
                                en_hp = ret[1]
                                en_bleeding = ret[2]
                                logs.append(f"{move}.{cp.name} провёл массовые атаки мечами по противнику, нанеся урон в 40 ед.")
                            else:
                                ret = cp_damage(20, cp_def, cp_hp, cp_bleeding)
                                cp_def = ret[0]
                                cp_hp = ret[1]
                                cp_bleeding = ret[2]
                                logs.append(f"{move}.{cp.name} попытался провести массовые атаки мечами по противнику, но {en.name} прервал его и нанёс урон в 20 ед.")
                            break
                        else:
                            await msg.edit(f"{cp.mention}, у вас нету 40 выносливости для этого!")
                            continue
                     elif res.component.label == "Пропустить ход":
                          logs.append(f"{move}.{cp.name} решил передохнуть и поэтому решил пропустить свой ход.")
                          break
                    if cp == player1:
                        p1_hp = cp_hp
                        p1_def = cp_def
                        p1_stamina = cp_stamina
                        p1_bleeding = cp_bleeding
                        p1_stun = cp_stun
                        if p1_weapons == "алебарда":
                            p1_sw = cp_sw
                        p2_hp = en_hp
                        p2_def = en_def
                        p2_stamina = en_stamina
                        p2_bleeding = en_bleeding
                        p2_stun = en_stun
                    else:
                        p2_hp = cp_hp
                        p2_def = cp_def
                        p2_stamina = cp_stamina
                        p2_bleeding = cp_bleeding
                        p2_stun = cp_stun
                        if p2_weapons == "алебарда":
                            p2_sw = cp_sw
                        p1_hp = en_hp
                        p1_def = en_def
                        p1_stamina = en_stamina
                        p1_bleeding = en_bleeding
                        p1_stun = en_stun
                    move += 1
                    current_player += 1
            if move > 100:
                winner = "None"
                await msg.edit(f"{p1.mention} vs {p2.mention}\nОба война храбро сражались, но в итоге выдохлись и не смогли продолжить свой бой на арене.\nЗрители разочарованы, DRAW!")
                await DeleteMessages(msg, msg0, msg1)
                xp(ctx, en, 50)
                xp(ctx, cp, 50)
                return
            elif p1_hp < 0:
                winner = player2
                enemy = player1
            else:
                winner = player1
                enemy = player2
            if winner != "None":
               await msg.edit(f"{winner.mention} своей последней атакой сносит {enemy.mention} голову и поднимает её вверх, кричя о своей победе.\nЗрители ликуют, {winner.mention} WIN!")
               await DeleteMessages(msg, msg0, msg1)
               xp(ctx, winner, 50)
               money(winner, enemy, ctx)
               return

def cp_damage(damage, cp_def, cp_hp, cp_bleeding):
                        if damage > cp_def:
                           damage -= cp_def
                           сp_def = 0
                           cp_hp -= damage
                           check = check_chance(10)
                           if check == True and cp_bleeding == 0:
                              cp_bleeding = 3
                        else:
                            cp_def -= damage
                        return [cp_def, cp_hp, cp_bleeding]

def en_damage(damage, en_def, en_hp, en_bleeding):
                        if damage > en_def:
                           damage -= en_def
                           en_def = 0
                           en_hp -= damage
                           check = check_chance(10)
                           if check == True and en_bleeding == 0:
                              en_bleeding = 3
                        else:
                              en_def -= damage
                        return [en_def, en_hp, en_bleeding]

def emp_damage(cp_weapons, en_def, en_hp, en_bleeding):
                        if cp_weapons == "двуручный меч":
                           damage = random.randint(15, 30)
                           ignore = 0,5
                        else:
                           damage = random.randint(20, 25)
                           ignore = 0,6
                        if en_def < damage * (1 - ignore):
                           damage -= en_def
                           en_def = 0
                           en_hp -= damage
                        else:
                           en_def -= damage * (1 - ignore)
                           en_hp -= damage * ignore
                        check = check_chance(10)
                        if check == True and en_bleeding == 0:
                           en_bleeding = 3
                        return [damage, en_def, en_hp, en_bleeding]

def check_chance(chance):
    check = random.randint(1, 100)
    if check < chance:
        return True
    else:
        return False

def normal_damage(cp_weapons):
    if cp_weapons == "щит с мечём":
       damage = random.randint(5, 15)
    elif cp_weapons == "двуручный меч":
       damage = random.randint(10, 15)
    elif cp_weapons == "алебарда":
       damage = random.randint(5, 20)
    elif cp_weapons == "лук и парные клинки":
       damage = random.randint(10, 20)
    else:
       damage = random.randint(15, 30)
    return damage

def components_but(distance, cp_weapons):
    if cp_weapons == "щит с мечём":
       if distance == True:
         buttons = [[Button(style = ButtonStyle.blue, label = "Таран"),
                    Button(style = ButtonStyle.blue, label = "Поднять щит"),
                    Button(style = ButtonStyle.blue, label = "Приблизиться")],
                    [Button(style = ButtonStyle.red, label = "Пропустить ход"),
                    Button(style = ButtonStyle.red, label = "Сдаться"),
                    Button(style = ButtonStyle.red, label = "Логи")]
         ]
       else:
         buttons = [[Button(style = ButtonStyle.blue, label = "Атаковать"),
                    Button(style = ButtonStyle.blue, label = "Пнуть"),
                    Button(style = ButtonStyle.blue, label = "Таран"),
                    Button(style = ButtonStyle.blue, label = "Поднять щит")],
                    [Button(style = ButtonStyle.red, label = "Пропустить ход"),
                    Button(style = ButtonStyle.red, label = "Сдаться"),
                    Button(style = ButtonStyle.red, label = "Логи")]
         ]
    elif cp_weapons == "двуручный меч":
        if distance == True:
         buttons = [[Button(style = ButtonStyle.blue, label = "Защитная стойка"),
                    Button(style = ButtonStyle.blue, label = "Приблизиться")],
                    [Button(style = ButtonStyle.red, label = "Пропустить ход"),
                    Button(style = ButtonStyle.red, label = "Сдаться"),
                    Button(style = ButtonStyle.red, label = "Логи")]
         ]
        else:
         buttons = [[Button(style = ButtonStyle.blue, label = "Атаковать"),
                    Button(style = ButtonStyle.blue, label = "Пнуть"),
                    Button(style = ButtonStyle.blue, label = "Усиленный удар"),
                    Button(style = ButtonStyle.blue, label = "Защитная стойка")],
                    [Button(style = ButtonStyle.red, label = "Пропустить ход"),
                    Button(style = ButtonStyle.red, label = "Сдаться"),
                    Button(style = ButtonStyle.red, label = "Логи")]
         ]
    elif cp_weapons == "алебарда":
        if distance == True:
         buttons = [[Button(style = ButtonStyle.blue, label = "Таран алебардой"),
                    Button(style = ButtonStyle.blue, label = "Стена копий"),
                    Button(style = ButtonStyle.blue, label = "Приблизиться")],
                    [Button(style = ButtonStyle.red, label = "Пропустить ход"),
                    Button(style = ButtonStyle.red, label = "Сдаться"),
                    Button(style = ButtonStyle.red, label = "Логи")]
         ]
        else:
         buttons = [[Button(style = ButtonStyle.blue, label = "Атаковать"),
                    Button(style = ButtonStyle.blue, label = "Пнуть"),
                    Button(style = ButtonStyle.blue, label = "Усиленный удар"),
                    Button(style = ButtonStyle.blue, label = "Таран алебардой"),
                    Button(style = ButtonStyle.blue, label = "Стена копий")],
                    [Button(style = ButtonStyle.red, label = "Пропустить ход"),
                    Button(style = ButtonStyle.red, label = "Сдаться"),
                    Button(style = ButtonStyle.red, label = "Логи")]
         ]
    elif cp_weapons == "лук и парные клинки":
        if distance == True:
         buttons = [[Button(style = ButtonStyle.blue, label = "Выстрелить"),
                    Button(style = ButtonStyle.blue, label = "Приблизиться")],
                    [Button(style = ButtonStyle.red, label = "Пропустить ход"),
                    Button(style = ButtonStyle.red, label = "Сдаться"),
                    Button(style = ButtonStyle.red, label = "Логи")]
         ]
        else:
         buttons = [[Button(style = ButtonStyle.blue, label = "Атаковать"),
                    Button(style = ButtonStyle.blue, label = "Пнуть"),
                    Button(style = ButtonStyle.blue, label = "Выпад"),
                    Button(style = ButtonStyle.blue, label = "Отойти и выстрелить")],
                    [Button(style = ButtonStyle.red, label = "Пропустить ход"),
                    Button(style = ButtonStyle.red, label = "Сдаться"),
                    Button(style = ButtonStyle.red, label = "Логи")]
         ]
    elif cp_weapons == "парные мечи":
        if distance == True:
         buttons = [[Button(style = ButtonStyle.blue, label = "Защитная стойка"),
                    Button(style = ButtonStyle.blue, label = "Приблизиться")],
                    [Button(style = ButtonStyle.red, label = "Пропустить ход"),
                    Button(style = ButtonStyle.red, label = "Сдаться"),
                    Button(style = ButtonStyle.red, label = "Логи")]
         ]
        else:
         buttons = [[Button(style = ButtonStyle.blue, label = "Атаковать"),
                    Button(style = ButtonStyle.blue, label = "Пнуть"),
                    Button(style = ButtonStyle.blue, label = "Защитная стойка"),
                    Button(style = ButtonStyle.blue, label = "Множество игл")],
                    [Button(style = ButtonStyle.red, label = "Пропустить ход"),
                    Button(style = ButtonStyle.red, label = "Сдаться"),
                    Button(style = ButtonStyle.red, label = "Логи")]
         ]
    return buttons