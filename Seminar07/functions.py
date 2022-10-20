from random import randint

with open("journal.csv", "r", encoding="utf-8") as journal:
    journal_counter = len(journal.readlines())


def generate_all(N: int):
    with open("Name.txt", "r", encoding="utf-8") as name:
        name = name.readlines()
    with open("Surname.txt", "r", encoding="utf-8") as surname:
        surname = surname.readlines()
    with open("Companies.txt", "r", encoding="utf-8") as companies:
        companies = companies.readlines()
    with open("journal.csv", "w", encoding="utf-8") as journal:
        for i in range(N):
            result = []
            result.append(str(i + 1))
            result.append(name[randint(0, len(name)-1)].replace("\n", ""))
            result.append(surname[randint(0, len(surname)-1)].replace("\n", ""))
            result.append(f"{randint(1, 30)}.{randint(1, 12)}.{randint(1970, 2012)}")
            result.append(companies[randint(0, len(companies)-1)].replace("\n", ""))
            numbers_count = randint(1, 9)
            numbers_lst = []
            for i in range(numbers_count):
                phone_number = "+79"
                for j in range(9):
                    phone_number += str(randint(0, 9))
                numbers_lst.append(phone_number)
            result.append(";".join(numbers_lst))
            journal.write(",".join(result) + "\n")


def add_record(name, surname, dateofb, work, phone_number):
    global journal_counter
    journal_counter += 1
    result = [str(journal_counter), name, surname, dateofb, work, phone_number.replace(" ", ";")]
    with open("journal.csv", "a", encoding="utf-8") as journal:
        journal.write(",".join(result) + "\n")


def change_record(record_id, field, new_value):
    with open("journal.csv", "r", encoding="utf-8") as journal:
        journal_lst = journal.readlines()
    with open("journal.csv", "w", encoding="utf-8") as journal:
        for i in range(len(journal_lst)):
            if i == record_id - 1:
                comma_places = [j for j in range(len(journal_lst[i])) if journal_lst[i].startswith(",", j)]
                start = comma_places[field-1]
                try:
                    finish = comma_places[field]
                except:
                    finish = len(journal_lst)-1
                if field != 5:
                    journal_lst[i] = journal_lst[i][:start+1] + new_value + journal_lst[i][finish:]
                else:
                    journal_lst[i] = journal_lst[i][:start + 1] + new_value.replace(" ", ";") + \
                                     journal_lst[i][finish:]+"\n"
                journal.write(journal_lst[i])
            else:
                journal.write(journal_lst[i])


def delete_record(id):
    with open("journal.csv", "r", encoding="utf-8") as journal:
        journal_lst = journal.readlines()
    with open("journal.csv", "w", encoding="utf-8") as journal:
        for i in range(len(journal_lst)):
            if i == id - 1:
                continue
            else:
                journal.write(journal_lst[i])

def delete_all():
    with open("journal.csv", "w", encoding="utf-8") as journal:
        journal.write("")



