import telebot
import functions
from tabulate import tabulate

bot = telebot.TeleBot('Token')

database = []
last = ""


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я твой справочник.\nЯ могу читать и выводить справочник из файла, "
                                      "добавлять, удалять, изменять и сохранять изменения.\n"
                                      "Нажми /help, чтобы узнать мои команды")


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Список доступных действий:\n"
                                      "Отправь мне файл формата csv, чтобы загрузить справочник\n"
                                      "/show - показать справочник\n"
                                      "/add - добавить строку в справочник\n"
                                      "/change - изменить строку в справочнике\n"
                                      "/delete - удалить строку из справочника\n"
                                      "/save - отправлю тебе справочник со всеми изменениями")


@bot.message_handler(content_types=["document"])
def load_data(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(str(message.chat.id) + '.csv', "wb") as new_file:
        new_file.write(downloaded_file)
    with open(str(message.chat.id) + '.csv', "r", encoding="utf-8") as new_file:
        global database
        database = new_file.readlines()


@bot.message_handler(commands=["show"])
def show(message):
    database_write = []
    if database:
        for i in range(len(database)):
            database_write.append(database[i].replace('\n', "").split(","))
        bot.send_message(message.chat.id, "\n" + tabulate(database_write[1:], headers=database_write[0]) + "\n")
    else:
        bot.send_message(message.chat.id, "Пока нечего показывать")


@bot.message_handler(commands=["add"])
def add(message):
    global last
    last = "add"
    bot.send_message(message.chat.id, "Запишите данные в формате:\n"
                                      "<Имя>\n"
                                      "<Фамилия>\n"
                                      "<Дата рождения>\n"
                                      "<Дата приёма на работу>\n"
                                      "<Отдел>\n"
                                      "<Должность>\n")


@bot.message_handler(commands=["change"])
def add(message):
    global last
    last = "change"
    bot.send_message(message.chat.id, "Запишите данные в формате:\n"
                                      "<id>\n"
                                      "<Имя>\n"
                                      "<Фамилия>\n"
                                      "<Дата рождения>\n"
                                      "<Дата приёма на работу>\n"
                                      "<Отдел>\n"
                                      "<Должность>\n")


@bot.message_handler(commands=["delete"])
def add(message):
    global last
    last = "delete"
    bot.send_message(message.chat.id, "Запишите id для удаления")


@bot.message_handler(commands=["save"])
def save(message):
    if database:
        file_name = str(message.chat.id) + ".csv"
        functions.save_file(file_name, database)
        bot.send_document(message.chat.id, open(file_name, "r", encoding="utf-8"))
    else:
        bot.send_message(message.chat.id, "Нечего сохранять:(")


@bot.message_handler(commands=["admin"])
def admin(message):
    global last
    last = 'admin'
    bot.send_message(message.chat.id, "Введите пароль")


@bot.message_handler(content_types=["text"])
def actions(message):
    if last == "add":
        data = message.text.replace("\n", ",")
        functions.add_data(data, database)
        bot.send_message(message.chat.id, "Записано!")
    elif last == "change":
        data = message.text.replace("\n", ",")
        functions.change_data(data, database)
        bot.send_message(message.chat.id, "Изменено!")
    elif last == "delete":
        id = message.text
        functions.delete_data(id, database)
        bot.send_message(message.chat.id, "Удалено!")
    elif last == "admin":
        if message.text == "Пасхалка для Данила":
            bot.send_document(message.chat.id, open("log.csv", "rb"))
        else:
            bot.send_message(message.chat.id, "Пароль указан неверно, повторите попытку")
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю, выберите нужную команду или воспользуйтесь /help")


bot.polling()
