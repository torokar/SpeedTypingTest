import pygame
import sys
from main import Button
import random
import time

#Размер окна и добавления количества кадров в секнду
WIDTH, HEIGHT = 750, 500
FRAME_RATE = 60
pygame.init()



window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")

#изначальная кнопка пуск
start_button = Button(WIDTH/2-(250/2), 200, 300, 100, "",
                      "image/green_button.png","image/green_button_hover.png", "button.mp3")


def reset_test():
    # Сброс на исходные значения
    user_text = ""
    symbols_enter = 0
    time_start = time.time()

#Функция которая загружает изображения иконки и заднего фона
def load_image():
    icon = pygame.image.load("image/icon1.png")
    pygame.display.set_icon(icon)
    background = pygame.image.load("image/background.jpg")
    return background

#Функция ввода пользователя и вывод заголовочного и названия приложения
def setup_users_inter(font, input_font):
    text_ = font.render("Тест на скорость печати", True, "Yellow")
    pygame.display.set_caption("Скорость печати")
    input_rect = pygame.Rect(50, 200, 140, 32)
    color_active = pygame.Color('Yellow') #цвет поля ввода, активированного
    color_passive = pygame.Color('White') #цвет поля ввода, неактивированного
    return text_, input_rect, color_active, color_passive



#Сам запуск теста
def start_test():
    background = pygame.image.load("image/background.jpg")
    font = pygame.font.Font(None, 60)
    input_font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    user_text = "" #сюды помещается текст который вводит пользователь

    text_files = ["text1.txt", "text2.txt", "text3.txt", "text4.txt"] #Загрузка текстовых файлов для вывода
    selected_file = random.choice(text_files)
    with open(selected_file, "r", encoding='utf-8') as file:  #открытия и закрытия файла в кодировке utf-8
        file_text = file.read()

    file_surf = input_font.render(file_text, True, ('White')) #вывод текста
    text_, input_rect, color_active, color_passive = setup_users_inter(font, input_font)

    active = False
    # time_start = None
    users_time = None
    symbols_enter = 0
    game_end = True

    """Начала отсчета времени для расчета времени который пользователь 
    затратил на прохождения теста и расчета введеных количество символов в минуту"""
    time_start = time.time()

    while True:



        window.blit(background, (0, 0))
        window.blit(file_surf, (50, 100))
        window.blit(text_, (150, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #Вызов функции reset_test(), которая обнуляет все значения введеное в прошлом тесте
                #И сразу вызов функции start_test() для отображения нового текста
                if event.key == pygame.K_ESCAPE:
                    reset_test()
                    start_test()

            """Обработка события нажатия на клавишу мыши и 
            нажатия на кнопку удаления BACKSPACE"""
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                    #
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        #user_text удаляет последний сивол из строки
                        user_text = user_text[:-1]
                        symbols_enter -= 1
                    elif event.key == pygame.K_RETURN:
                        if time_start is not None:

                            """Расчет времени затраченное на тест,
                            время от начала эпохи отнимаем от текущего времени"""
                            total_time = time.time() - time_start
                            typing_speed = symbols_enter / total_time
                            time_start = None


                            users_time = input_font.render(f"Время: {round(total_time, 2)} секунд", True,
                                                           (255, 255, 255))

                            """Расчет количества сиволов в минуту расчитывается количество введенных символов 
                            делится на затраченное временя на тест"""
                            characters_minute = input_font.render(
                                f"Скорость печати: {round(typing_speed, 2)} знаков в минуту", True,
                                pygame.Color('White'))
                            # game_end = True




                    else:
                        user_text += event.unicode
                        symbols_enter += 1


        if active:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(window, color, input_rect, 2)
        text_surf = input_font.render(user_text, True, (255, 255, 255))
        window.blit(text_surf, (input_rect.x + 5, input_rect.y + 5))


        input_rect.w = max(10, text_surf.get_width() + 10)

        if users_time is not None:
            #Вывод результатов
            window.blit(users_time, (10, 300))
            window.blit(characters_minute, (10, 350))


        pygame.display.flip()
        pygame.display.set_caption("Скорость печати")
        clock.tick(FRAME_RATE)

#Основная функция запуска приложения




def main_menu():
    run = True
    icon = pygame.image.load("image/icon1.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Скорость печати")
    while run:
        background_start_window = pygame.image.load("image/background2.jpg")
        window.blit(background_start_window, (0, 0))


        font = pygame.font.Font(None, 72)

        text_surf = font.render("ТЕСТ НА СКОРОСТЬ ПЕЧАТИ", True, ('Yellow'))
        text_rect = text_surf.get_rect(center=(380, 50))
        window.blit(text_surf, text_rect)

        #Отображения кнопки начать
        start_button.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button.rect.collidepoint(event.pos):
                    start_test()

        start_button.check_hover(pygame.mouse.get_pos())
        pygame.display.flip()

main_menu()

