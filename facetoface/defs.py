from objects import *
from classes import *


def fruits_lose_game():
    if select_fruit.life == 0:
        print(f"YOU LOSE THE GAME BRO, THE FRUIT IS -> {select_fruit.name}")



def play_fruits(select_fruit):
    for i in range(select_fruit.life):
        print(f"\nTIP: {select_fruit.tips[i]}")
        print(f"LIFE: {select_fruit.life}")
        user_option = input("\ninput what u think>> ").title()
        if user_option != select_fruit.name:
            select_fruit.lose_life()
            print("\nYOU LOSE A LIFE!!")
            print("please try again\n")
        else:
            print("CONGRATS!! YOU TAKE IT BRO!")
            break
    fruits_lose_game()


def play_singer(select_singer):
    print("THE TIPS ARE THE NAME OF SONG THAT THE SINGER SING.")
    for i in range(select_singer.life):
        print(f"\nMUSIC: {select_singer.musics[i]}")
        print(f"LIFE: {select_singer.life}")
        user_option = input("\nWHO'S THE SINGER?>> ").title()
        if user_option != select_singer.name:
            select_singer.lose_life()
            print("\nYOU LOSE A LIFE!!")
            print("please try again\n")
        else:
            print("CONGRATS!! YOU TAKE IT BRO!")
            break


def game_mode():
    import inquirer
    questions = [
        inquirer.List('mode',
                      message="||Select the things that you want to play on FACE TO FACE||",
                      choices=['Singers', 'Fruits'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['mode']

