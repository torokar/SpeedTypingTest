import time


print("Добро пожаловать в Speed typing test!")


def time_typing_test(text, time_taken):
    num_char = len(text)
    typing_speed = num_char / (time_taken / 60)
    return typing_speed


def list_text():
    engine = True
    input("Нажмите Enter чтобы начать. ")
    while engine:
        choice_users = input("Введите уровень сложности от 1 до 4 (0 - выход): ")
        if choice_users == '0':
            print("Программа закрыта.")
            engine = False
        elif choice_users == '1':
            file_path = r'Text\\1_level.txt'
            print("\n")
            try:
                file = open(file_path, encoding='utf-8')
                print(file.read())
                file.close()
            except FileNotFoundError:
                print("Файл не найден")
            except Exception as a:
                print("Произошла ошибка чтения файла")
                print(a)
            break
        elif choice_users == '2':
            file_path = r'Text\\2_level.txt'
            print("\n")
            try:
                file = open(file_path, encoding='utf-8')
                print(file.read())
                file.close()
            except FileNotFoundError:
                print("Файл не найден")
            except Exception as a:
                print("Произошла ошибка чтения файла")
                print(a)
            break
        elif choice_users == '3':
            file_path = r'Text\\3_level.txt'
            print("\n")
            try:
                file = open(file_path, encoding='utf-8')
                print(file.read())
                file.close()
            except FileNotFoundError:
                print("Файл не найден")
            except Exception as a:
                print("Произошла ошибка чтения файла")
                print(a)
            break
        elif choice_users == '4':
            file_path = r'Text\\4_level.txt'
            print("\n")
            try:
                file = open(file_path, encoding='utf-8')
                print(file.read())
                file.close()
            except FileNotFoundError:
                print("Файл не найден")
            except Exception as a:
                print("Произошла ошибка чтения файла")
                print(a)
            break
        else:
            print("Некорректный ввод.")


def _results():
    # --start_time отвечает за начало отчета секундомера
    start_time = time.time()

    print("Начните печатать. ")

    Text_input = input("-- ")

    # Время для расчета минут затраченное на написания текса
    end_time = time.time()
    time_taken = end_time - start_time
    delta_time = (end_time - start_time) / 60

    # Знаков написанных во время теста
    typing_speed = time_typing_test(Text_input, time_taken)
    print("Скорость печати:", round(typing_speed), "знаков в минуту")

    print(f"Длительность {round(delta_time, 2)} минут.")


list_text()
_results()




