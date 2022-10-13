# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота#
# b) Подумайте как наделить бота ""интеллектом""
import random
from tkinter import *
from random import randint

root = Tk()
root.title("Candy Game")
game_run = True
candy_start = 2021
candy_in_stock = candy_start
player1 = "Said"
player2 = "Danil"
player_name = player1
candy_take_max = 28
candy_taken = 0


def bot_turn(candy_taken_player):
    global candy_taken
    global candy_in_stock
    global candy_take_max
    if mode == 1:
        if candy_in_stock < 29:
            candy_taken = randint(1, candy_in_stock)
        else:
            candy_taken = randint(1, candy_take_max)
    if mode == 2:
        candy_taken = candy_in_stock % (candy_take_max + 1)
        if candy_taken == 0:
            candy_taken = randint(1, candy_take_max)
    candy_label["text"] = f'{player_name} взял {candy_taken_player}, Бот взял кофет: {candy_taken}'


def new_game(mode_chosed):
    global mode
    mode = mode_chosed
    global game_run
    game_run = True
    global candy_start
    global candy_in_stock
    candy_in_stock = candy_start
    global player_name
    player_name = player1
    take_candy_label["text"] = f'Сколько конфеток вы хотите взять, {player_name}?'
    take_candy_label["background"] = "#e6e6fa"
    candies_left_labbel["text"] = f'На терелке осталось конфет: {candy_in_stock}'
    candy_taken_label.delete(0, END)
    candy_label["text"] = 'Пусть победит умнейший!'


def take_candy():
    global candy_take_max
    global player_name
    global player1
    global player2
    global candy_taken
    global candy_in_stock
    candy_taken = candy_taken_label.get()
    if game_run and candy_taken.isdigit():
        candy_taken = int(candy_taken)
        if 0 < candy_taken <= candy_take_max and candy_in_stock >= candy_taken:
            candy_taken_label.delete(0, END)
            candy_label["text"] = f'{player_name} взял {candy_taken} конфет'
            if not check_win():
                if mode:
                    bot_turn(candy_taken)
                    player_name = "Бот"
                    check_win()
                    player_name = player1
                else:
                    if player_name == player1:
                        player_name = player2
                        take_candy_label["text"] = f'Сколько конфеток вы хотите взять, {player_name}?'
                    else:
                        player_name = player1
                        take_candy_label["text"] = f'Сколько конфеток вы хотите взять, {player_name}?'


def check_win():
    global game_run
    global candy_in_stock
    result = False
    if candy_in_stock == candy_taken:
        candies_left_labbel["text"] = 'На терелке не осталось конфет'
        take_candy_label["text"] = f'Игрок {player_name} победил!'
        game_run = False
        result = True
        if player_name == "Бот":
            take_candy_label["background"] = "red"
        else:
            take_candy_label["background"] = "green"
    else:
        candy_in_stock -= candy_taken
        candies_left_labbel["text"] = f'На терелке осталось конфет: {candy_in_stock}'
    return result


take_candy_label = Label(root,
                         font=('Verdana', 15),
                         text=f'Сколько конфеток вы хотите взять, {player_name}?',
                         background="#e6e6fa")
take_candy_label.grid(row=0, column=0, columnspan=3, sticky='nsew', )

candies_left_labbel = Label(root,
                            font=('Verdana', 15),
                            text=f'На терелке осталось {candy_in_stock} конфет',
                            background="#e6e6fa")
candies_left_labbel.grid(row=3, column=0, columnspan=3, sticky='nsew', )

candy_taken_label = Entry(root,
                          font=('Verdana', 15),
                          background="#e6e6fa")
candy_taken_label.grid(row=1, column=0, sticky='nsew')

candy_label = Label(root,
                    font=('Verdana', 15),
                    text='Пусть победит умнейший!',
                    background="#e6e6fa")
candy_label.grid(row=2, column=0, columnspan=3, sticky='nsew', )

Button(root,
       text='Взять конфеты',
       font=('Verdana', 15),
       command=take_candy,
       background="#e6e6fa") \
    .grid(row=1, column=1, columnspan=2, sticky='nsew')

mode = 0
Button(root,
       text='multiplayer',
       font=('Verdana', 15),
       background="#e6e6fa",
       command=lambda x=mode: new_game(x)) \
    .grid(row=6, column=0, sticky='nsew')

mode = 1
Button(root,
       text='bot',
       font=('Verdana', 15),
       background="#e6e6fa",
       command=lambda x=mode: new_game(x)) \
    .grid(row=6, column=1, sticky='nsew')

mode = 2
Button(root,
       text='clever bot',
       font=('Verdana', 15),
       background="#e6e6fa",
       command=lambda x=mode: new_game(x)) \
    .grid(row=6, column=2, sticky='sew')

mode = 0

root.mainloop()
