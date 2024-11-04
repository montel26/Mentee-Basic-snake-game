import random
from ObjectOrientated.SetUp import RED, SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_SIZE


class Food:
    """Handles the spawning and rendering of food."""

    def __init__(self):
        self.position = self.spawn_food()

    def spawn_food(self):
        x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_SIZE) / 10) * 10
        y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_SIZE) / 10) * 10
        return [x, y]

    def draw(self):
        pygame.draw.rect(screen, RED, [self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE])

