# high_scores.py

import os

HIGH_SCORE_FILE = 'highscores.txt'

def load_high_scores():
    scores = []
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, 'r') as file:
            for line in file:
                try:
                    name, score = line.strip().split(',')
                    scores.append((name.strip(), int(score)))
                except ValueError:
                    print(f"Skipping line due to ValueError: {line.strip()}")
    return sorted(scores, key=lambda x: x[1], reverse=True)[:10]

def save_score(name, score):
    scores = load_high_scores()
    scores.append((name.strip(), score))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[:10]
    with open(HIGH_SCORE_FILE, 'w') as file:
        for name, score in scores:
            file.write(f'{name},{score}\n')
