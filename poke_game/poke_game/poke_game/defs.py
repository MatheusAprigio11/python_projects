from time import sleep
from objects import *
from classes import *
import os

def choose_pokemon():
    import inquirer
    poke_selected = inquirer.prompt([
        inquirer.List('pokes',
                      message="||SELECT YOUR POKEMON BRO||",
                      choices=[*name_pokemons],
                      ),
    ])
    print(f"\nYOU SELECTED THE POKEMON: {poke_selected['pokes']} ")
    match poke_selected['pokes']:
        case "Treeko":
            poke = treeko
            return poke
        case "Moltres":
            poke = moltres
            return poke
        case "Lapras":
            poke = lapras
            return poke
    sleep(3)

def poke_bot():
    pok_bot = random.choice(name_pokemons)
    print("BOT IS SELECTING...")
    sleep(3)
    print("...")
    sleep(3)
    print(f"\nBOT SELECTED THE POKEMON: {pok_bot}")
    sleep(3)
    if pok_bot == treeko.name:
        pok_bot = treeko
    elif pok_bot == moltres.name:
        pok_bot = moltres
    elif pok_bot == lapras.name:
        pok_bot = lapras
    return pok_bot

def bot_loose_hp(player_one, player_bot):
    print(f"{player_one.name} used {player_one.mov}")
    atk = player_one.advantage(player_bot.type, player_one.damage)
    attack_dmg = atk
    print(f"DAMAGE: {round(attack_dmg, 2)}")
    loose_hp_bot = player_bot.life - attack_dmg
    player_bot.life = loose_hp_bot
    print(f"{player_bot.name} HP: {round(loose_hp_bot,2)}\n")


def me_loose_hp(player_bot, player_one):
    print(f"{player_bot.name} used {player_bot.mov}")
    atk = player_bot.advantage(player_one.type, player_bot.damage)
    attack_dmg = atk
    print(f"BOT DAMAGE: {round(atk, 2)}")
    loose_hp_me = player_one.life - attack_dmg
    player_one.life = loose_hp_me
    print(f"{player_one.name} HP: {round(loose_hp_me, 2)}\n")

    return loose_hp_me


def gameplay():
    os.system('cls')

    player_one = choose_pokemon()
    player_bot = poke_bot()

    while player_one.life > 0 or player_bot.life > 0:
        print(f"{player_one.name} HP: {round(player_one.life,2)}\n")
        print(f"{player_bot.name} HP: {round(player_bot.life,2)}")

        if player_one.velocity > player_bot.velocity:
            player_one.choose_mov()
            bot_loose_hp(player_one, player_bot)
            sleep(2)
            me_loose_hp(player_bot, player_one)
            sleep(2)

        elif player_one.velocity < player_bot.velocity:
            me_loose_hp(player_bot, player_one)
            sleep(2)
            player_one.choose_mov()
            bot_loose_hp(player_one, player_bot)
            sleep(2)

        else:
            list_players = [player_one, player_bot]
            who_starts = random.choice(list_players)

            if who_starts == player_one:
                print("PLAYER ONE STARTS!")
                player_one.choose_mov()
                bot_loose_hp(player_one, player_bot)
                sleep(2)
                me_loose_hp(player_bot, player_one)
                sleep(2)
            else:
                print("PLAYER TWO STARTS")
                me_loose_hp(player_bot, player_one)
                sleep(2)
                player_one.choose_mov()
                bot_loose_hp(player_one, player_bot)
                sleep(2)
        os.system('cls')
        if player_one.life <= 0 or player_bot.life <= 0:
            break