def choose_option():
    return int(input("Выберите режим: "))


def ask_load():
    return input("Введите имя файла для загрузки: ")


def ask_add():
    data = ''
    data += input("Введите имя: ") + ","
    data += input("Введите фамилию: ") + ","
    data += input("Введите дату рождения: ") + ","
    data += input("Введите дату приема на работу: ") + ","
    data += input("Введите отдел: ") + ","
    data += input("Введите должность: ") + ","
    data += input("Введите зарплату: ")
    return data


def ask_change():
    data = input("Введите id пользователя для изменения: ")
    return data + "," + ask_add()


def ask_delete():
    return input("Введите id пользователя для удаления: ")


def ask_save():
    return input("Введите имя файла для сохранения: ")
