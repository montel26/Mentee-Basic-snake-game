# main.py

import pygame
import random
from display import initialize_display, show_high_scores, final_score, create_snake, display_message
from HighScore import load_high_scores, save_score
from InputHandler import get_name

pygame.init()

# Constants
FIELD_LEN = 800
FIELD_HEIGHT = 600
SNAKE_SIZE = 10
SNAKE_SPEED = 15

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize
caption = initialize_display(FIELD_LEN, FIELD_HEIGHT)
timer = pygame.time.Clock()

def game():
    play = False
    game_close = False
    val_x1 = FIELD_LEN / 2
    val_y1 = FIELD_HEIGHT / 2
    new_x1 = 0
    new_y1 = 0
    snake_list = []
    snake_len = 1

    foodx_pos = round(random.randrange(0, FIELD_LEN - SNAKE_SIZE) / 10) * 10
    foody_pos = round(random.randrange(0, FIELD_HEIGHT - SNAKE_SIZE) / 10) * 10

    while not play:
        while game_close:
            caption.fill(RED)
            display_message(caption, 'You lose! Press R to play again or Q to quit', (0, 0, 0), FIELD_LEN, FIELD_HEIGHT)
            final_score(caption, snake_len - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        player_name = get_name(caption, pygame.font.SysFont('impact', 24), FIELD_LEN, FIELD_HEIGHT)
                        save_score(player_name, snake_len - 1)
                        play = True
                        game_close = False
                    if event.key == pygame.K_r:
                        player_name = get_name(caption, pygame.font.SysFont('impact', 24), FIELD_LEN, FIELD_HEIGHT)
                        save_score(player_name, snake_len - 1)
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_x1 = -SNAKE_SIZE
                    new_y1 = 0
                elif event.key == pygame.K_RIGHT:
                    new_x1 = SNAKE_SIZE
                    new_y1 = 0
                elif event.key == pygame.K_UP:
                    new_y1 = -SNAKE_SIZE
                    new_x1 = 0
                elif event.key == pygame.K_DOWN:
                    new_y1 = SNAKE_SIZE
                    new_x1 = 0

        if val_x1 >= FIELD_LEN or val_x1 < 0 or val_y1 >= FIELD_HEIGHT or val_y1 < 0:
            game_close = True

        val_x1 += new_x1
        val_y1 += new_y1
        caption.fill(GREEN)

        pygame.draw.rect(caption, RED, [foodx_pos, foody_pos, SNAKE_SIZE, SNAKE_SIZE])

        snake_head = [val_x1, val_y1]
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_len:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True

        create_snake(caption, SNAKE_SIZE, snake_list)
        final_score(caption, snake_len - 1)

        pygame.display.update()

        if val_x1 == foodx_pos and val_y1 == foody_pos:
            foodx_pos = round(random.randrange(0, FIELD_LEN - SNAKE_SIZE) / 10) * 10
            foody_pos = round(random.randrange(0, FIELD_HEIGHT - SNAKE_SIZE) / 10) * 10
            snake_len += 1

        timer.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

if __name__ == '__main__':
    game()
