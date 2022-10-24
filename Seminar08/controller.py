import UI
import view
import functions

database = ["id,FirstName,LastName,DateofBirth,EmploymentDate,Department,Post,Salary\n"]


def start():
    global database
    view.options()
    mode = UI.choose_option()
    match mode:
        case 1:
            file_name = UI.ask_load()
            database = functions.load_file(file_name)
            view.load_success()
            start()
        case 2:
            view.show_data(database)
            start()
        case 3:
            data = UI.ask_add()
            functions.add_data(data, database)
            view.add_success()
            start()
        case 4:
            data = UI.ask_change()
            functions.change_data(data, database)
            view.change_success()
            start()
        case 5:
            id = UI.ask_delete()
            functions.delete_data(id, database)
            view.delete_success()
            start()
        case 6:
            file_name = UI.ask_save()
            functions.save_file(file_name, database)
            view.save_success()
            start()
        case 7:
            view.end_program()
        case _:
            view.warning()
            start()
