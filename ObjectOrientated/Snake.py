from ObjectOrientated.SetUp import BLACK, SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_SIZE


class Snake:
    """Manages snake properties and behaviors."""

    def __init__(self):
        self.body = [[SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]]
        self.direction = [0, 0]
        self.length = 1

    def move(self):
        new_head = [self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1]]
        self.body.insert(0, new_head)
        if len(self.body) > self.length:
            self.body.pop()

    def change_direction(self, x, y):
        self.direction = [x, y]

    def grow(self):
        self.length += 1

    def check_collision(self):
        head = self.body[0]
        return (
            head[0] >= SCREEN_WIDTH or head[0] < 0 or head[1] >= SCREEN_HEIGHT or head[1] < 0 or
            any(segment == head for segment in self.body[1:])
        )

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, BLACK, [segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE])
