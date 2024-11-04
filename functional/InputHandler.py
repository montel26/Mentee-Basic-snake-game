# input_handler.py

import pygame

def get_name(caption, display_style, field_len, field_height):
    entering_name = True
    name = ''
    while entering_name:
        caption.fill((255, 255, 255))
        prompt = display_style.render("Enter your name and press Enter:", True, (0, 0, 0))
        name_text = display_style.render(name, True, (0, 0, 0))
        caption.blit(prompt, [field_len / 4, field_height / 3])
        caption.blit(name_text, [field_len / 4, field_height / 3 + 50])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    entering_name = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
    return name.strip() or "Anonymous"
