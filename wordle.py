import pygame
from vocab import *
from turn_player import turn_player
from player_profile import profile

# Initialize Pygame
pygame.init()

# import random vocab
eng_word, description = vocab_random()
print(eng_word)
print(description)

# Constants
WIDTH, HEIGHT = 1280, 720
ROWS, COLS = 6, len(eng_word)
CELL_SIZE = 70
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

wordle_turn = "player1"

# Functions
def draw_grid(guesses, colors, current_guess, guess_count):
    """draw grid"""

    dark_brown = 73, 56, 41
    burly_wood = 222,184,135
    light_steel_blue  = 176,196,222
    silver = 192,192,192
    grey = 128,128,128

    pygame.draw.rect(screen, grey, (243, 113, 803, 503), 0, 0, 20, 20, 20, 20)
    pygame.draw.rect(screen, burly_wood, (240, 110, 800, 500), 0, 0, 20, 20, 20, 20)

    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * (CELL_SIZE + MARGIN) + 250,
                               row * (CELL_SIZE + MARGIN) + 130,
                               CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, colors[row][col], rect)

            if row < guess_count and guesses[row][col]:
                letter = FONT.render(guesses[row][col], True, BLACK)
                screen.blit(letter, (rect.x + 20, rect.y + 5))

            if row == guess_count and col < len(current_guess):
                letter = FONT.render(current_guess[col], True, BLACK)
                screen.blit(letter, (rect.x + 20, rect.y + 5))

    pygame.display.flip()

def check_word(guess, target):
    """check the word"""
    result = ['gray'] * len(target)
    target_chars = list(target)
    point = 0

    # First pass: Check for correct positions
    for i in range(len(target)):
        if guess[i] == target[i]:
            result[i] = 'green'
            point += 2
            target_chars[i] = None

    # Second pass: Check for correct letters in wrong positions
    for i in range(len(target)):
        if result[i] == 'green':
            continue
        if guess[i] in target_chars:
            result[i] = 'yellow'
            point += 1
            target_chars[target_chars.index(guess[i])] = None

    return result, point

def get_color(code):
    """change color"""
    return GREEN if code == 'green' else YELLOW if code == 'yellow' else GRAY

def wordle():
    """wordle"""
    guesses = [[''] * COLS for _ in range(ROWS)]
    colors = [[GRAY] * COLS for _ in range(ROWS)]
    current_guess = ""
    guess_count = 0
    running = True
    turn = wordle_turn

    brown = 185, 156, 107

    player_1 = pygame.image.load("images/player_1.png")
    player_2 = pygame.image.load("images/player_2.png")
    player_1 = pygame.transform.scale(player_1, (230, 230))
    player_2 = pygame.transform.scale(player_2, (230, 230))

    point_player1 = 0
    point_player2 = 0
    add = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(current_guess) == COLS:
                        feedback, add = check_word(current_guess, target_word)
                        for i, code in enumerate(feedback):
                            colors[guess_count][i] = get_color(code)

                        guesses[guess_count] = list(current_guess)
                        guess_count += 1

                        # สวิตช์เทิร์นหลังจากเช็คคำ
                        if turn == "player1":
                            point_player1 += add
                            turn = "player2"
                        else:
                            point_player2 += add
                            turn = "player1"

                    # Win or lose conditions
                    if current_guess == target_word:
                        return False
                    elif guess_count == ROWS:
                        return True

                    current_guess = ""

                elif event.key == pygame.K_BACKSPACE:
                    current_guess = current_guess[:-1]

                elif event.unicode.isalpha() and len(current_guess) < COLS:
                    current_guess += event.unicode.upper()


        profile(130, 630, 110, 30, 70, brown, "PLAYER 1", player_1)
        profile(1150, 120, 110, 30, 70, brown, "PLAYER 2", player_2)

        # Draw the grid with current guesses and current_guess
        if turn == "player1":
            turn_player(90, 640)
        elif turn == "player2":
            turn_player(1120, 130)

        draw_grid(guesses, colors, current_guess, guess_count)

        pygame.display.update()
    pygame.quit()
    
    return True
