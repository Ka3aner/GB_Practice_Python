# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
general_output = ""


def FileWorks(file_name, method, output=""):
    if method == "r":
        with open(file_name, method, encoding="utf-8") as file:
            return file.read()
    elif method == "w":
        with open(file_name, method, encoding="utf-8") as file:
            file.write(output)


for lines in FileWorks("input1.txt", "r").split("\n"):
    if lines:
        lst = lines.split(" ")
        output = ""
        for item in lst:
            if "а" not in item and "б" not in item and "в" not in item \
                    and "А" not in item and "Б" not in item and "В" not in item:
                output += " " + item
            elif not item.isalpha():
                output += item[-1]

        general_output += output[1:]
        general_output += "\n"

FileWorks("output1.txt", "w", general_output[:-1])
