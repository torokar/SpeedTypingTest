import pygame
import sys
import random

window = pygame.display.set_mode([750, 500])

def main():
    pygame.init()
    icon = pygame.image.load("image/icon1.png")
    pygame.display.set_icon(icon)
    background = pygame.image.load("image/background.jpg")
    font = pygame.font.Font(None, 60)
    Input_font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    user_text = ""

    # Список текстов
    text_files = ["text1.txt", "text2.txt", "text3.txt", "text4.txt"]
    # Выбор случайного файла из списка
    selected_file = random.choice(text_files)

    # Открытие текстового файла
    with open(selected_file, "r", encoding='utf-8') as file:
        file_text = file.read()

    text_surf = font.render("Speed Typing Test", True, "Yellow")  # Рендеринг надписи "Speed Typing Test"
    file_surf = Input_font.render(file_text, True, (255, 255, 255))  # Рендеринг текста из файла

    input_rect = pygame.Rect(10, 200, 140, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color(255, 255, 255)
    color = color_passive
    active = False

    while True:
        window.blit(background, (0, 0))
        window.blit(file_surf, (50, 100))  # Отображение текста из файла

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        if active:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(window, color, input_rect, 2)
        text_surf = Input_font.render(user_text, True, (255, 255, 255))
        window.blit(text_surf, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(10, text_surf.get_width() + 10)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
    pygame.quit()
