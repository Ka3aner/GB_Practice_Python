# Создайте программу для игры в ""Крестики-нолики"".
import tkinter.font
from tkinter import *
import random

root = Tk()
root.title("Крестики-нолики")
turn = 1
field = []
game_run = True


def new_game(mode_chosed=0):
    global mode
    mode = mode_chosed
    global game_run
    game_run = True
    global turn
    turn = 1
    for line in field:
        for item in line:
            item["text"] = ""
            item["background"] = "white"


def click(row, column):
    if not field[row][column]["text"] and game_run:
        global turn
        if turn % 2:
            field[row][column]["text"] = "X"
        else:
            field[row][column]["text"] = 'O'
        turn += 1
        check_win()
        if game_run:
            global mode
            if mode and turn != 10:
                bot_move()
                turn += 1
                check_win()


def check_win():
    for i in range(3):
        check_line(field[i][0], field[i][1], field[i][2])
        check_line(field[0][i], field[1][i], field[2][i])
    check_line(field[0][0], field[1][1], field[2][2])
    check_line(field[0][2], field[1][1], field[2][0])
    global game_run
    if game_run and turn == 10:
        for line in field:
            for button in line:
                button["background"] = "orange"


def check_line(a, b, c):
    if a["text"] == b["text"] == c["text"] != "":
        global game_run
        game_run = False
        global turn, mode
        if turn % 2 and mode in range(1, 3):
            a["background"] = b["background"] = c["background"] = "red"
        else:
            a["background"] = b["background"] = c["background"] = "green"


def bot_move():
    if mode == 2:
        for i in range(3):
            if best_turn(field[i][0], field[i][1], field[i][2], 'O'):
                return
            if best_turn(field[0][i], field[1][i], field[2][i], 'O'):
                return
        if best_turn(field[0][0], field[1][1], field[2][2], 'O'):
            return
        if best_turn(field[2][0], field[1][1], field[0][2], 'O'):
            return
        for i in range(3):
            if best_turn(field[i][0], field[i][1], field[i][2], "X"):
                return
            if best_turn(field[0][i], field[1][i], field[2][i], "X"):
                return
        if best_turn(field[0][0], field[1][1], field[2][2], "X"):
            return
        if best_turn(field[2][0], field[1][1], field[0][2], "X"):
            return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == '':
            field[row][col]['text'] = 'O'
            break


def best_turn(a1, a2, a3, smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == '':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == '' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == '' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res


for row in range(3):
    line = []
    for column in range(3):
        button = Button(root, text="", width=10, height=5,
                        font=('Verdana', 20, 'bold'),
                        command=lambda row=row, column=column: click(row, column),
                        background="white")
        button.grid(column=column, row=row)
        line.append(button)
    field.append(line)

    mode = 0
    multiplayer = Button(root, text='multiplayer', font=('Verdana', 15), command=lambda x=mode: new_game(x))
    multiplayer.grid(row=3, column=0, sticky='nsew')
    mode = 1
    bot = Button(root, text='bot', font=('Verdana', 15), command=lambda x=mode: new_game(x))
    bot.grid(row=3, column=1, sticky='nsew')
    mode = 2
    clever_bot = Button(root, text='clever bot', font=('Verdana', 15), command=lambda x=mode: new_game(x))
    clever_bot.grid(row=3, column=2, sticky='nsew')

root.mainloop()
