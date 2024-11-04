import os
from ObjectOrientated.SetUp import BLACK, GREEN, SCREEN_HEIGHT, SCREEN_WIDTH, WHITE


class ScoreManager:
    """Handles score loading, saving, and displaying high scores."""
    
    def __init__(self, high_score_file):
        self.high_score_file = high_score_file
        self.scores = self.load_high_scores()

    def load_high_scores(self):
        scores = []
        if os.path.exists(self.high_score_file):
            with open(self.high_score_file, 'r') as file:
                for line in file:
                    try:
                        name, score = line.strip().split(',')
                        scores.append((name.strip(), int(score)))
                    except ValueError:
                        print(f"Skipping line due to ValueError: {line.strip()}")
        return sorted(scores, key=lambda x: x[1], reverse=True)[:10]

    def save_score(self, name, score):
        self.scores.append((name.strip(), score))
        self.scores = sorted(self.scores, key=lambda x: x[1], reverse=True)[:10]
        with open(self.high_score_file, 'w') as file:
            for name, score in self.scores:
                file.write(f'{name},{score}\n')

    def display_high_scores(self):
        screen.fill(WHITE)
        title = display_font.render('High Scores', True, GREEN)
        screen.blit(title, [SCREEN_WIDTH / 3, SCREEN_HEIGHT / 6])
        for i, (name, score) in enumerate(self.scores, 1):
            score_text = score_font.render(f'{i}. {name}: {score}', True, BLACK)
            screen.blit(score_text, [SCREEN_WIDTH / 3, SCREEN_HEIGHT / 6 + i * 30])
        pygame.display.update()
        pygame.time.delay(7000)