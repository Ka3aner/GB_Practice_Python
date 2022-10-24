from tabulate import tabulate


def options():
    print("\033[37m{}".format("Режимы:\n"
                              "[1] - Загрузить базу из файл\n"
                              "[2] - Показать данные\n"
                              "[3] - Добавить запись\n"
                              "[4] - Изменить запись\n"
                              "[5] - Удалить запись\n"
                              "[6] - Сохранить базу в файл\n"
                              "[7] - Закрыть"))


def load_success():
    print("\033[32m{}".format("\nБаза успешно загружена\n"))


def show_data(database):
    database_write = []
    if database:
        for i in range(len(database)):
            database_write.append(database[i].replace('\n', "").split(","))
        print("\n" + tabulate(database_write[1:], headers=database_write[0]) + "\n")
    else:
        print("Пока нечего показывать")


def add_success():
    print("\033[32m{}".format("\nЗапись успешно добавлена\n"))


def change_success():
    print("\033[32m{}".format("\nЗапись успешно изменена\n"))


def delete_success():
    print("\033[32m{}".format("\nЗапись успешно удалена\n"))


def save_success():
    print("\033[32m{}".format("\nБаза успешно сохранена\n"))


def end_program():
    print("\033[32m{}".format("\nПриходите ещё!\n"))


def warning():
    print("\033[31m{}".format("\nКажется что-то пошло не так, попробуйте ввод ещё раз\n"))
