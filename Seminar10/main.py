# Калькулятор многочленов и примеров

import telebot
import sympy
from sympy.core.sympify import SympifyError

bot = telebot.TeleBot('5610928733:AAFnO26zWeEuLjcMBSheiLLtObqH0hOIt_E')


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я твой калькулятор.\n"
                                      "Я могу считать обычные примеры или или примеры с многочленами\n"
                                      "Нажми /help, чтобы узнать мои команды")


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Список доступных действий:\n"
                                      "/calculate - вычислю пример или сумму многочленов\n")


@bot.message_handler(commands=["calculate"])
def calculate(message):
    bot.send_message(message.chat.id, "Введите пример, который необходимо посчитать")


@bot.message_handler(content_types=["text"])
def actions(message):
    text = message.text.replace("=", "")
    try:
        answer = eval(text)
    except (SyntaxError, NameError):
        try:
            answer = str(sympy.polys.polytools.poly_from_expr(text)[0].as_expr()).replace('**', '^')
        except (SyntaxError, SympifyError):
            answer = "Кажется в вашем примере ошибка. Пожалуйста, исправьте её и снова напишите мне пример."
    bot.send_message(message.chat.id, answer)


bot.polling()
