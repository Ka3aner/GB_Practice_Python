# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
import tkinter


def rle_zip():
    output = ""
    for lines in FileWorks("Восстановленный.txt", "r").split("\n"):
        if lines:
            current_char = lines[0]
            counter = 1
            for i in range(1, len(lines)):
                if lines[i] == current_char:
                    counter += 1
                else:
                    output += current_char + str(counter)
                    current_char = lines[i]
                    counter = 1
            output += current_char + str(counter)
            output += "\n"
    FileWorks("Сжатый.txt", "w", output[:-1])

    lb = tkinter.Label(root, text='Сжатие успешно произведено!\nПроверь файл "Сжатый.txt"', font=40)
    lb.place(x=0, y=0, width=500, height=150)


def rle_unzip():
    output = ""
    for lines in FileWorks("Сжатый.txt", "r").split("\n"):
        if lines:
            for i in range(1, len(lines), 2):
                output += lines[i - 1] * int(lines[i])
            output += "\n"
    FileWorks("Восстановленный.txt", "w", output[:-1])

    lb = tkinter.Label(root, text='Восстановление успешно произведено!\nПроверь файл "Восстановленный.txt"', font=40)
    lb.place(x=0, y=0, width=500, height=150)


def FileWorks(file_name, method, output=""):
    if method == "r":
        with open(file_name, method, encoding="utf-8") as file:
            return file.read()
    elif method == "w":
        with open(file_name, method, encoding="utf-8") as file:
            file.write(output)


def quit():
    root.quit()


root = tkinter.Tk()
root.title("RLE")
root.geometry("500x150")
btn1 = tkinter.Button(root, text="Сжать", command=rle_zip)
btn1.place(x=100, y=50, width=100, height=50)
btn2 = tkinter.Button(root, text="Восстановить", command=rle_unzip)
btn2.place(x=300, y=50, width=100, height=50)
root.mainloop()
