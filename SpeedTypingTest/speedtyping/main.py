import pygame
import sys
import random
import time

window = pygame.display.set_mode([750, 500])

def main():
    pygame.init()
    icon = pygame.image.load("image/icon1.png")
    pygame.display.set_icon(icon)
    background = pygame.image.load("image/background.jpg")
    pygame.display.set_caption("Скорость печати")
    font = pygame.font.Font(None, 60)
    Input_font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    user_text = ""


    text_files = ["text1.txt", "text2.txt", "text3.txt", "text4.txt"]
    # Выбор случайного файла из списка
    selected_file = random.choice(text_files)

    # Открытие текстового файла
    with open(selected_file, "r", encoding='utf-8') as file:
        file_text = file.read()

    text_ = font.render("Тест на скорость печати", True, "Yellow")
    file_surf = Input_font.render(file_text, True, ('White'))

    input_rect = pygame.Rect(50, 200, 140, 32)
    color_active = pygame.Color('Yellow')
    color_passive = pygame.Color('White')
    color = color_passive
    active = False
    time_start = None
    users_time = None
    symbols_enter = 0
    #начала подсчета времени
    time_start = time.time()

    while True:
        window.blit(background, (0, 0))
        window.blit(file_surf, (50, 100))

        window.blit(text_, (150, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            elif event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                        symbols_enter -= 1
                    elif event.key == pygame.K_RETURN:
                        if time_start is not None:
                            #расчет времени
                            total_time = time.time() - time_start
                            

                            typing_speed = symbols_enter / total_time

                            time_start = None
                            users_time = Input_font.render(f"Время: {round(total_time, 2)} секунд", True, (255, 255, 255))

                            characters_minute = Input_font.render(f"Скорость печати: {round(typing_speed, 2)} знаков в минуту", True, pygame.Color('White'))

                    else:

                        user_text += event.unicode
                        symbols_enter += 1
        if active:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(window, color, input_rect, 2)
        text_surf = Input_font.render(user_text, True, (255, 255, 255))
        window.blit(text_surf, (input_rect.x + 5, input_rect.y + 5))
        pygame.display.set_caption("Скорость печати")


        input_rect.w = max(10, text_surf.get_width() + 10)

        if users_time is not None:
            window.blit(users_time, (10, 300))
            window.blit(characters_minute, (10, 350))


        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
    pygame.quit()

