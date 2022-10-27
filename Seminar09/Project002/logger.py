from datetime import datetime


def LOG(func):
    def wrapper(*args):
        with open("log.csv", "a", encoding="utf-8") as log:
            log.write(f"{func.__doc__}: {datetime.now()}\n")
        return func(*args)

    return wrapper
