import random
import pygame
import time
import os
pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)


field_len = 800
field_height = 600
caption = pygame.display.set_mode((field_len, field_height))
pygame.display.set_caption('Snake')
timer = pygame.time.Clock()
snake_size = 10
snake_speed = 15
display_style = pygame.font.SysFont('impact', 24)
score_font = pygame.font.SysFont('impact', 30)
high_score_file = 'highscores.txt'
def load_high_score():
    scores = []
    if os.path.exists(high_score_file):
        with open(high_score_file, 'r') as file:
            for line in file:
                try:
                    name, score = line.strip().split(',')
                    scores.append((name.strip(), int(score)))  
                except ValueError:
                    print(f"Skipping line due to ValueError: {line.strip()}")
    return sorted(scores, key=lambda x: x[1], reverse=True)[:10]

def save_score(name,score):
    scores = load_high_score()  
    scores.append((name.strip(), score))  
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[:10]  
    with open(high_score_file, 'w') as file:
        for name, score in scores:  
            file.write(f'{name},{score}\n')
def show_high_scores():
    caption.fill(white)
    high_scores = load_high_score()
    title = display_style.render('High scores', True, green)
    caption.blit(title, [field_len / 3, field_height / 6])
    for i, (name,score) in enumerate(high_scores, 1):
        score_text = score_font.render(f'{i}. {name}: {score}', True, black)
        caption.blit = (score_text, [field_len/3 , field_height/6 + i* 30])
        pygame.display.update()
        pygame.time.delay(7000)
def get_name():
    entering_name = True
    name = ''
    while entering_name:
        caption.fill(white)
        prompt = display_style.render("Enter your name and press Enter:", True, black)
        name_text = display_style.render(name, True, black)
        caption.blit(prompt, [field_len / 4, field_height / 3])
        caption.blit(name_text, [field_len / 4, field_height / 3 + 50])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key
                    entering_name = False
                elif event.key == pygame.K_BACKSPACE:  # Backspace key
                    name = name[:-1]
                else:
                    name += event.unicode  # Add character to name
    return name.strip() or "Anonymous"  # Use "Anonymous" if no name is entered
def final_score(score):
    val = score_font.render(f'SNAKE!!Current Score: {score}', True, yellow)
    caption.blit(val, [0, 0])

def create_snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(caption, black, [i[0], i[1], snake_block, snake_block])

def display_message(msg, colour):
    message = display_style.render(msg, True, colour)
    caption.blit(message, [field_len / 5, field_height / 3])

def game():
    play = False
    game_close = False
    val_x1 = field_len / 2
    val_y1 = field_height / 2
    new_x1 = 0
    new_y1 = 0
    snake_list = []
    snake_len = 1

    
    foodx_pos = round(random.randrange(0, field_len - snake_size) / 10) * 10
    foody_pos = round(random.randrange(0, field_height - snake_size) / 10) * 10

    while not play:
        while game_close:
            caption.fill(red)
            display_message('You lose! Press R to play again or Q to quit', black)
            final_score(snake_len - 1)
            pygame.display.update()

            for i in pygame.event.get():
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_q:
                        player_name = get_name()
                        save_score(player_name,snake_len - 1)
                        play = True
                        game_close = False
                    if i.key == pygame.K_r:
                        player_name = get_name()
                        save_score(player_name,snake_len - 1)
                        game()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_x1 = -snake_size
                    new_y1 = 0
                elif event.key == pygame.K_RIGHT:
                    new_x1 = snake_size
                    new_y1 = 0
                elif event.key == pygame.K_UP:
                    new_y1 = -snake_size
                    new_x1 = 0
                elif event.key == pygame.K_DOWN:
                    new_y1 = snake_size
                    new_x1 = 0

        if val_x1 >= field_len or val_x1 < 0 or val_y1 >= field_height or val_y1 < 0:
            game_close = True

        val_x1 += new_x1
        val_y1 += new_y1
        caption.fill(green)

        
        pygame.draw.rect(caption, red, [foodx_pos, foody_pos, snake_size, snake_size])

        
        snake_head = [val_x1, val_y1]
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_len:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True

        create_snake(snake_size, snake_list)
        final_score(snake_len - 1)

        pygame.display.update()


        if val_x1 == foodx_pos and val_y1 == foody_pos:
            foodx_pos = round(random.randrange(0, field_len - snake_size) / 10) * 10
            foody_pos = round(random.randrange(0, field_height - snake_size) / 10) * 10
            snake_len += 1

        timer.tick(snake_speed)

    pygame.quit()
    quit()

game()
