from ObjectOrientated.SetUp import BLACK, GREEN, SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_SIZE, SNAKE_SPEED, WHITE, YELLOW


class Game:
    """Main game class that handles game flow and logic."""

    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score_manager = ScoreManager(HIGH_SCORE_FILE)
        self.game_over = False
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.change_direction(-SNAKE_SIZE, 0)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(SNAKE_SIZE, 0)
                elif event.key == pygame.K_UP:
                    self.snake.change_direction(0, -SNAKE_SIZE)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(0, SNAKE_SIZE)

    def update(self):
        self.snake.move()
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.spawn_food()
            self.snake.grow()
            self.score += 1
        if self.snake.check_collision():
            self.game_over = True

    def render(self):
        screen.fill(GREEN)
        self.snake.draw()
        self.food.draw()
        score_text = score_font.render(f"Score: {self.score}", True, YELLOW)
        screen.blit(score_text, [0, 0])
        pygame.display.update()

    def get_player_name(self):
        name = ''
        entering_name = True
        while entering_name:
            screen.fill(WHITE)
            prompt = display_font.render("Enter your name and press Enter:", True, BLACK)
            name_text = display_font.render(name, True, BLACK)
            screen.blit(prompt, [SCREEN_WIDTH / 4, SCREEN_HEIGHT / 3])
            screen.blit(name_text, [SCREEN_WIDTH / 4, SCREEN_HEIGHT / 3 + 50])
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
        return name or "Anonymous"

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.update()
            self.render()
            clock.tick(SNAKE_SPEED)

        player_name = self.get_player_name()
        self.score_manager.save_score(player_name, self.score)
        self.score_manager.display_high_scores()