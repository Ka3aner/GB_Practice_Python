import telebot
import random
from telebot import types

bot = telebot.TeleBot('Token')
field = []
turn = 1
game_run = True


@bot.message_handler(commands=["start"])
def new_game(message):
    global game_run
    game_run = True
    global turn
    turn = 1
    k = 0
    item = {}
    markup = types.InlineKeyboardMarkup(row_width=3)
    for i in range(3):
        for j in range(3):
            field[i][j] = " "
            item[k] = types.InlineKeyboardButton(field[i][j], callback_data=str(k))
            k += 1

    markup.row(item[0], item[1], item[2])
    markup.row(item[3], item[4], item[5])
    markup.row(item[6], item[7], item[8])
    bot.send_message(message.chat.id, "Поиграем в крестики-нолики?")
    bot.send_message(message.chat.id, "Нажми кнопку, чтобы сделать ход!", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callbackInline(call):
    click = int(call.data)
    if click == 0 or click == 3 or click == 6:
        column = 0
    elif click == 1 or click == 4 or click == 7:
        column = 1
    else:
        column = 2
    if click == 0 or click == 1 or click == 2:
        row = 0
    elif click == 3 or click == 4 or click == 5:
        row = 1
    else:
        row = 2

    if field[row][column] == " " and game_run:
        global turn
        turn += 1
        field[row][column] = "X"
        check_win(call.message.chat.id)
        if game_run:
            bot_move()
            turn += 1
            check_win(call.message.chat.id)
        markup = types.InlineKeyboardMarkup(row_width=3)
        item = {}
        k = 0
        for i in range(3):
            for j in range(3):
                item[k] = types.InlineKeyboardButton(field[i][j], callback_data=str(k))
                k += 1

        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
        # bot.edit_message_text("Твой ход", call.message.chat.id, call.message.message_id, reply_markup=markup)
        # bot.send_message(call.message.chat.id, "Следующий ход", reply_markup=markup)


def check_win(id):
    for i in range(3):
        check_line(field[i][0], field[i][1], field[i][2], id)
        check_line(field[0][i], field[1][i], field[2][i], id)
    check_line(field[0][0], field[1][1], field[2][2], id)
    check_line(field[0][2], field[1][1], field[2][0], id)
    global game_run
    if game_run and turn == 10:
        bot.send_message(id, "Ничья! Нажми /start для новой игры")
        game_run = False


def check_line(a, b, c, id):
    if a == b == c != " ":
        global game_run
        game_run = False
        global turn, mode
        if turn % 2:
            bot.send_message(id, "Ты проиграл! Нажми /start для новой игры")
        else:
            bot.send_message(id, "Ты выиграл! Нажми /start для новой игры")


def bot_move():
    for i in range(3):
        if best_turn(i, 0, i, 1, i, 2, 'O'):
            return
        if best_turn(0, i, 1, i, 2, i, 'O'):
            return
    if best_turn(0, 0, 1, 1, 2, 2, 'O'):
        return
    if best_turn(2, 0, 1, 1, 0, 2, 'O'):
        return
    for i in range(3):
        if best_turn(i, 0, i, 1, i, 2, "X"):
            return
        if best_turn(0, i, 1, i, 2, i, "X"):
            return
    if best_turn(0, 0, 1, 1, 2, 2, "X"):
        return
    if best_turn(2, 0, 1, 1, 0, 2, "X"):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col] == ' ':
            field[row][col] = 'O'
            break


def best_turn(x1, y1, x2, y2, x3, y3, smb):
    res = False
    if field[x1][y1] == smb and field[x2][y2] == smb and field[x3][y3] == ' ':
        field[x3][y3] = 'O'
        res = True
    if field[x1][y1] == smb and field[x2][y2] == ' ' and field[x3][y3] == smb:
        field[x2][y2] = 'O'
        res = True
    if field[x1][y1] == ' ' and field[x2][y2] == smb and field[x3][y3] == smb:
        field[x1][y1] = 'O'
        res = True
    return res


for row in range(3):
    line = []
    for column in range(3):
        line.append(" ")
    field.append(line)

bot.polling()
