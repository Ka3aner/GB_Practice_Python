from logger import LOG


@LOG
def add_data(data, database):
    """Добавление записи"""
    database.append(str(len(database)) + "," + data + '\n')


@LOG
def change_data(data, database):
    """Изменение записи"""
    id = data.split(",")[0]
    database[int(id)] = data + "\n"


@LOG
def delete_data(id, database):
    """Удаление записи"""
    database.pop(int(id))
    for i in range(int(id), len(database)):
        newitem = database[i].split(",")
        newitem[0] = str(i)
        database[i] = ",".join(newitem)


@LOG
def save_file(file_name, database):
    """Сохранение файла"""
    with open(file_name, "w", encoding="utf-8") as file:
        file.writelines(database)
