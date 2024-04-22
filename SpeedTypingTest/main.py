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
                engine = False
            except FileNotFoundError:
                print("Файл не найден")
                #Вывод ошибки при не том кодировании текстового файла сохраняется в переменной а
            except Exception as a:
                print("Произошла ошибка чтения файла")
                print(a)

        elif choice_users == '2':
            file_path = r'Text\\2_level.txt'
            print("\n")
            try:
                file = open(file_path, encoding='utf-8')
                print(file.read())
                file.close()
                engine = False
            except FileNotFoundError:
                print("Файл не найден")
            except Exception as a:
                print("Произошла ошибка чтения файла")
                print(a)

        elif choice_users == '3':
            file_path = r'Text\\3_level.txt'
            print("\n")
            try:
                file = open(file_path, encoding='utf-8')
                print(file.read())
                file.close()
                engine = False
            except FileNotFoundError:
                print("Файл не найден")
            except Exception as a:
                print("Произошла ошибка чтения файла")
                print(a)

        elif choice_users == '4':
            file_path = r'Text\\4_level.txt'
            print("\n")
            try:
                file = open(file_path, encoding='utf-8')
                print(file.read())
                file.close()
                engine = False
            except FileNotFoundError:
                print("Файл не найден")
            except Exception as a:
                print("Произошла ошибка чтения файла")
                print(a)

        else:
            print("Некорректный ввод.")


def compare_files(source_files, user_file):
    similarities = []
    for source_file in source_files:
        try:
            with open(source_file, 'r', encoding='utf-8') as f_source:
                source_text = f_source.read()
            with open(user_file, 'r', encoding='utf-8') as f_user:
                user_text = f_user.read()

            # Удаление символов переноса строки и пробелов для более точного сравнения
            source_text = source_text.replace('\n', '').replace(' ', '')
            user_text = user_text.replace('\n', '').replace(' ', '')

            # Подсчет количества символов в каждом тексте
            total_chars = len(source_text)
            common_chars = sum(a == b for a, b in zip(source_text, user_text))

            # Вычисление процента совпадения
            similarity_percentage = (common_chars / total_chars) * 100
            similarities.append(similarity_percentage)

        except FileNotFoundError:
            print("Один из файлов не найден.")
            return None
        except Exception as e:
            print("Произошла ошибка при сравнении файлов.")
            print(e)
            return None

    return similarities

def _results():
    # --start_time отвечает за начало отчета секундомера
    start_time = time.time()

    print("Начните печатать. ")

    Text_input = input("-- ")
    try:
        with open("enter.txt", "w", encoding="utf-8") as file:
            file.write(Text_input)
    except:
        print("Ошибка работы с файлом")

    # Время для расчета минут затраченное на написания текса
    end_time = time.time()
    time_taken = end_time - start_time
    delta_time = (end_time - start_time) / 60

    # Знаков написанных во время теста
    typing_speed = time_typing_test(Text_input, time_taken)
    print("Скорость печати:", round(typing_speed), "знаков в минуту")

    print(f"Длительность {round(delta_time, 2)} минут.")
    # Проверка точности
    source_files = ["Text\\1_level.txt"]
    user_file_path = "enter.txt"
    similarities = compare_files(source_files, user_file_path)
    if similarities is not None:
        avg_similarity = sum(similarities) / len(similarities)
        print(f"Средний процент совпадения текстов: {avg_similarity:.2f}%")




list_text()
_results()


