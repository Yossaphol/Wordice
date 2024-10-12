import pygame
from vocab import *

# Initialize Pygame
pygame.init()

# import random vocab
eng_word, description = vocab_random()
print(eng_word)
print(description)

# Constants
WIDTH, HEIGHT = 1280, 720
ROWS, COLS = 6, len(eng_word)
CELL_SIZE = 100
MARGIN = 10
FONT = pygame.font.Font('fonts/Jersey20.ttf', 64)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (120, 124, 126)
YELLOW = (181, 159, 59)
GREEN = (83, 141, 78)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle")
target_word = eng_word.upper()

# Functions
def draw_grid(guesses, colors, current_guess, guess_count):
    screen.fill(WHITE)
    
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * (CELL_SIZE + MARGIN) + MARGIN, 
                               row * (CELL_SIZE + MARGIN) + MARGIN, 
                               CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, colors[row][col], rect)

            if row < guess_count and guesses[row][col]:
                letter = FONT.render(guesses[row][col], True, BLACK)
                screen.blit(letter, (rect.x + 30, rect.y + 20))

            if row == guess_count and col < len(current_guess):
                letter = FONT.render(current_guess[col], True, BLACK)
                screen.blit(letter, (rect.x + 30, rect.y + 20))

    pygame.display.flip()

def check_word(guess, target):
    result = ['gray'] * len(target)
    target_chars = list(target)
    
    # First pass: Check for correct positions
    for i in range(len(target)):
        if guess[i] == target[i]:
            result[i] = 'green'
            target_chars[i] = None

    # Second pass: Check for correct letters in wrong positions
    for i in range(len(target)):
        if result[i] == 'green':
            continue
        if guess[i] in target_chars:
            result[i] = 'yellow'
            target_chars[target_chars.index(guess[i])] = None

    return result

def get_color(code):
    return GREEN if code == 'green' else YELLOW if code == 'yellow' else GRAY

def main():
    guesses = [[''] * COLS for _ in range(ROWS)]
    colors = [[GRAY] * COLS for _ in range(ROWS)]
    current_guess = ''
    guess_count = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(current_guess) == COLS:
                        feedback = check_word(current_guess, target_word)
                        for i, code in enumerate(feedback):
                            colors[guess_count][i] = get_color(code)
                        
                        guesses[guess_count] = list(current_guess)
                        guess_count += 1
                        current_guess = ''
                    
                    # Win or lose conditions
                    if current_guess == target_word:
                        print("You win!")
                        running = False
                    elif guess_count == ROWS:
                        print(f"You lose! The word was {target_word}.")
                        running = False
                
                elif event.key == pygame.K_BACKSPACE:
                    current_guess = current_guess[:-1]
                
                elif event.unicode.isalpha() and len(current_guess) < COLS:
                    current_guess += event.unicode.upper()
        
        # Draw the grid with current guesses and current_guess
        draw_grid(guesses, colors, current_guess, guess_count)
    
    pygame.quit()

if __name__ == "__main__":
    main()
