import time
import keyboard as keyb

print("Добро пожаловать в Speed typing test!")

#Блокировка клавишны ctrl
def _block():
    block_ctrl = ['ctrl']
    for key in block_ctrl:
        keyb.block_key(key)

#
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
            return None
        elif choice_users in ('1', '2', '3', '4'):
            file_path = f'Text\\{choice_users}_level.txt'
            print("\n")
            try:
                with open(file_path, encoding='utf-8') as file:
                    print(file.read())
                engine = False
                # Возвращаем путь к выбранному файлу
                return file_path
            except FileNotFoundError as e:
                print("Файл не найден", e)
            except Exception as a:
                print("Произошла ошибка чтения файла")
                print(a)
        else:
            print("Некорректный ввод.")
    return None


# Функция расчитывающая точность набора текста
def compare_files(source_file, user_file):
    try:
        with open(source_file, 'r', encoding='utf-8') as f_source:
            source_text = f_source.read()
        with open(user_file, 'r', encoding='utf-8') as f_user:
            user_text = f_user.read()

        source_text = source_text.replace('\n', '').replace(' ', '')
        user_text = user_text.replace('\n', '').replace(' ', '')

        total_chars = len(source_text)
        common_chars = sum(a == b for a, b in zip(source_text, user_text))

        similarity_percentage = (common_chars / total_chars) * 100
        return similarity_percentage
    except FileNotFoundError:
        print("Один из файлов не найден.")
        return None
    except Exception as e:
        print("Произошла ошибка при сравнении файлов.")
        print(e)
        return None


# Вывод результатов набора
def _results(file_path):
    if file_path:
        # --start_time отвечает за начало отчета секундомера
        start_time = time.time()

        print("Начните печатать. ")

        Text_input = input("-- ")
        try:
            with open("enter.txt", "w", encoding="utf-8") as file:
                file.write(Text_input)
        except Exception as b:
            print("Ошибка работы с файлом", b)

        # Время для расчета минут затраченное на написания текса
        end_time = time.time()
        time_taken = end_time - start_time
        delta_time = (end_time - start_time) / 60

        # Знаков написанных во время теста
        typing_speed = time_typing_test(Text_input, time_taken)
        print("Скорость печати:", round(typing_speed), "знаков в минуту")

        print(f"Длительность {round(delta_time, 2)} минут.")

        # Проверка точности сравнения с одним файлом
        user_file_path = "enter.txt"
        similarity = compare_files(file_path, user_file_path)
        if similarity is not None:
            print(f"Процент точности: {similarity:.2f}%")
    else:
        print("Некорректный путь к файлу.")


_block()
file_path = list_text()
_results(file_path)
