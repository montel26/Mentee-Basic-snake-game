# display.py

import pygame
import random

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
DISPLAY_STYLE = pygame.font.SysFont('impact', 24)
SCORE_FONT = pygame.font.SysFont('impact', 30)

def initialize_display(field_len, field_height):
    caption = pygame.display.set_mode((field_len, field_height))
    pygame.display.set_caption('Snake')
    return caption

def show_high_scores(caption, field_len, field_height, scores):
    caption.fill(WHITE)
    title = DISPLAY_STYLE.render('High scores', True, GREEN)
    caption.blit(title, [field_len / 3, field_height / 6])
    for i, (name, score) in enumerate(scores, 1):
        score_text = SCORE_FONT.render(f'{i}. {name}: {score}', True, BLACK)
        caption.blit(score_text, [field_len / 3, field_height / 6 + i * 30])
    pygame.display.update()
    pygame.time.delay(7000)

def final_score(caption, score):
    val = SCORE_FONT.render(f'SNAKE!!Current Score: {score}', True, YELLOW)
    caption.blit(val, [0, 0])

def create_snake(caption, snake_block, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(caption, BLACK, [x, y, snake_block, snake_block])

def display_message(caption, msg, colour, field_len, field_height):
    message = DISPLAY_STYLE.render(msg, True, colour)
    caption.blit(message, [field_len / 5, field_height / 3])
