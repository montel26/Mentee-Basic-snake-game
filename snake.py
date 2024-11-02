import random
import pygame
import time

pygame.init()

# Colors
colour_1 = (255, 255, 255)
colour_2 = (255, 255, 102)
colour_3 = (0, 0, 0)
colour_4 = (213, 200, 80)
colour_5 = (0, 255, 0)
colour_6 = (255, 0, 0)


field_len = 800
field_height = 600
caption = pygame.display.set_mode((field_len, field_height))
pygame.display.set_caption('Snake')
timer = pygame.time.Clock()
snake_size = 10
snake_speed = 10
display_style = pygame.font.SysFont('impact', 24)
score_font = pygame.font.SysFont('impact', 30)

def final_score(score):
    val = score_font.render('SNAKE!!     Current Score: ' + str(score), True, colour_2)
    caption.blit(val, [0, 0])

def create_snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(caption, colour_3, [i[0], i[1], snake_block, snake_block])

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
            caption.fill(colour_6)
            display_message('You lose! Press C to play again or Q to quit', colour_3)
            final_score(snake_len - 1)
            pygame.display.update()

            for i in pygame.event.get():
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_q:
                        play = True
                        game_close = False
                    if i.key == pygame.K_c:
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
        caption.fill(colour_1)

        
        pygame.draw.rect(caption, colour_5, [foodx_pos, foody_pos, snake_size, snake_size])

        
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
