import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Constants
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SNAKE_SIZE = 10
SNAKE_SPEED = 15
HIGH_SCORE_FILE = 'highscores.txt'

# Fonts
display_font = pygame.font.SysFont('impact', 24)
score_font = pygame.font.SysFont('impact', 30)

# Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()