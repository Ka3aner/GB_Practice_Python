import functions

def start_message():
    mode = int(input("Привет! Я твой менеджер справочника, выбери действие: \n"
                     "'1' - Сгенерировать новый справочник\n"
                     "'2' - Добавить новую строку в справочник\n"
                     "'3' - Изменить выбранную строку в справочнике\n"
                     "'4' - Удалить запись\n"
                     "'5' - Удалить справочник\n"
                     "Выбираю режим под номером: "))

    match mode:
        case 1:
            functions.generate_all(int(input("Введите количество строк в списке: ")))
        case 2:
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            dateofb = input("Введите дату рождения: ")
            work = input("Введите место работы: ")
            phone_number = input("Введите номера телефонов через пробел: ")
            functions.add_record(name, surname, dateofb, work, phone_number)
        case 3:
            record_id = int(input("Введите id строки для изменения: "))
            field = int(input("Введите номер поля для изменения:\n"
                              "'1' - Имя\n"
                              "'2' - Фамилия\n"
                              "'3' - День рождения\n"
                              "'4' - Место работы\n"
                              "'5' - Номера телефонов через пробел\n"
                              "Выбираю поле под номером: "))
            new_value = input(f"Новое значение поля для id {record_id}: ")
            functions.change_record(record_id, field, new_value)
        case 4:
            record_id = int(input("Введите id строки для удаления: "))
            functions.delete_record(record_id)
        case 5:
            functions.delete_all()
