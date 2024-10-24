import pygame
import sys
from pygame.locals import *
from vocab import *
from player_profile import profile
from turn_player import turn_player
from button import text_object
from winner import *
pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
grey = (211, 211, 211)
black = (0, 0, 0)
green = (0, 255, 0)
red = 255,0,0

small = pygame.font.Font("fonts/Pixelify.ttf", 30)
font = pygame.font.Font("fonts/Pixelify.ttf", 40)
big_font = pygame.font.Font("fonts/Pixelify.ttf", 60)

def check_guess(turns, word, user_guess, screen):
    """function for check the word that player guess and return win or not"""
    guess_color_code = [grey for _ in range(len(word))]
    point = 0
    word_checklist = list(word)

    for x in range(len(word)):
        if user_guess[x] == word[x]:
            guess_color_code[x] = green
            point += 2
            word_checklist[x] = None

    for x in range(len(word)):
        if guess_color_code[x] != green and user_guess[x] in word_checklist:
            guess_color_code[x] = yellow
            point += 1
            word_checklist[word_checklist.index(user_guess[x])] = None

    spacing = 0
    for x in range(len(word)):
        rendered_char = font.render(user_guess[x], True, black)
        pygame.draw.rect(screen, guess_color_code[x], pygame.Rect(280 + spacing, 130 + (turns * 70), 50, 50))
        screen.blit(rendered_char, (290 + spacing, 130 + (turns * 70)))
        spacing += 70

    return guess_color_code == [green for _ in range(len(word))], point

def wordle(turn, total_turn, point_player1, point_player2, final_point_a, final_point_b):
    """return wordle gameplay"""
    height = 720
    width = 1280
    dark_brown = 73, 56, 41

    burly_wood = 222,184,135
    light_steel_blue  = 176,196,222
    silver = 192,192,192
    grey = 128,128,128
    brown = 185, 156, 107
    dark_golden_rod = 184,134,11
    golden_rod = 218,165,32
    wheat = 245,222,179

    background = pygame.image.load("images/background_game.jpg")
    background = pygame.transform.scale(background, (1280, 720))

    map_game = pygame.image.load("images/game_map_2.png")
    map_game = pygame.transform.scale(map_game, (1290, 730))

    player_1 = pygame.image.load("images/player_1.png")
    player_2 = pygame.image.load("images/player_2.png")
    player_1 = pygame.transform.scale(player_1, (230, 230))
    player_2 = pygame.transform.scale(player_2, (230, 230))

    FPS = 30
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))

    screen.blit(background, (0, 0))

    word, description = vocab_random()
    word = word.upper()
    guess = ""
    turns = 0
    win = False
    all_guesses = []

    print(word)
    add = 0
    winner = turn

    while True:

        screen.blit(map_game, (0, 0))

        profile(130, 630, point_player1,  70, brown, "PLAYER 1", player_1)
        profile(1150, 120, point_player2, 70, brown, "PLAYER 2", player_2)

        pygame.draw.rect(screen, grey, (243, 113, 803, 503), 0, 0, 20, 20, 20, 20)
        pygame.draw.rect(screen, burly_wood, (240, 110, 800, 500), 0, 0, 20, 20, 20, 20)

        pygame.draw.rect(screen, wheat, (330, 30, 550, 60), 0, 0, 40, 40, 40, 40)
        describes = pygame.font.Font("fonts/Pixelify.ttf", 50)
        turn_remain = describes.render("TURN REMAINING : ", True, dark_brown)
        remain = describes.render(f"{20 - total_turn}", True, red)
        screen.blit(turn_remain, (350, 30))
        screen.blit(remain, (800, 30))


        for x in range(len(word)):
            for y in range(6):
                pygame.draw.rect(screen, grey, pygame.Rect(280 + (x * 70), 130 + (y * 70), 50, 50), 2)

        for i, g in enumerate(all_guesses):
            check_guess(i, word, g, screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            if turns < 6 and not win:  # Prevent input after 6 turns or if the player already won
                if event.type == pygame.KEYDOWN:
                    if event.key == K_BACKSPACE:
                        guess = guess[:-1]
                    elif event.key == K_RETURN:
                        if len(guess) == len(word):
                            all_guesses.append(guess)
                            win, add = check_guess(turns, word, guess, screen)
                            turns += 1
                            guess = ""

                            if turn == "player1":
                                point_player1 += add
                                final_point_a += add
                                add = 0
                                if not win:
                                    turn = "player2"
                            elif turn == "player2":
                                point_player2 += add
                                final_point_b += add
                                add = 0
                                if not win:
                                    turn = "player1"

                    elif event.unicode.isalpha() and len(guess) < len(word):
                        guess += event.unicode.upper()
        mini = pygame.font.Font("fonts/Pixelify.ttf", 20)
        your_text = small.render("GUESSING :", True, dark_golden_rod)
        render_guess = font.render(guess, True, dark_brown)
        meaning = mini.render(description, True, brown)
        screen.blit(your_text, (280, 550))
        screen.blit(render_guess, (440, 540))

        if turn == "player1":
            turn_player(90, 640)
        elif turn == "player2":
            turn_player(1120, 130)

        # out of turn remaining
        if total_turn == 20:
            return True, False, winner, total_turn, point_player1, point_player2, final_point_a, final_point_b

        # win and move
        elif win:
            winner = turn
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            sound = pygame.mixer.Sound("sounds/click.MP3")

            if 980 > mouse[0] > 780 and 490 > mouse[1] > 450:
                pygame.draw.rect(screen, "BLACK", (783, 453, 200,40), 0, 0, 30 ,30, 30, 30)
                pygame.draw.rect(screen, silver, (780,450,200,40), 0, 0, 30 ,30, 30, 30)

                if click[0] == 1:
                    sound.play()
                    total_turn += 1
                    if winner == "player1":
                        point_player1 = 0
                    else:
                        point_player2 = 0
                    return True, False, winner, total_turn, point_player1, point_player2, final_point_a, final_point_b

            else:
                pygame.draw.rect(screen, "BLACK", (783, 453, 200,40), 0, 0, 30 ,30, 30, 30)
                pygame.draw.rect(screen, light_steel_blue, (780,450,200,40), 0, 0, 30 ,30, 30, 30)

            win_text = big_font.render("You Win!", True, green)
            meaning_text = font.render("MEANING :", True, dark_brown)
            screen.blit(meaning_text, (800, 200))
            screen.blit(win_text, (760, 130))

            screen.blit(meaning, (720, 250))

            smallText = pygame.font.Font("fonts/Pixelify.ttf", 30)
            text_surface, text_rect = text_object("NEXT", smallText)
            text_rect.center = ((880), (470))
            screen.blit(text_surface, text_rect)

        # when not correct
        elif turns == 6 and not win:
            if winner == "player1":
                winner = "player2"
            else:
                winner = "player1"

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            sound = pygame.mixer.Sound("sounds/click.MP3")

            if 980 > mouse[0] > 780 and 490 > mouse[1] > 450:
                pygame.draw.rect(screen, "BLACK", (783, 453, 200,40), 0, 0, 30 ,30, 30, 30)
                pygame.draw.rect(screen, silver, (780,450,200,40), 0, 0, 30 ,30, 30, 30)

                if click[0] == 1:
                    sound.play()
                    total_turn += 1
                    return False, True, winner, total_turn, point_player1, point_player2, final_point_a, final_point_b

            else:
                pygame.draw.rect(screen, "BLACK", (783, 453, 200,40), 0, 0, 30 ,30, 30, 30)
                pygame.draw.rect(screen, light_steel_blue, (780,450,200,40), 0, 0, 30 ,30, 30, 30)

            win_text = big_font.render("You Lose!", True, red)
            meaning_text = font.render("THE WORD IS :", True, dark_brown)
            answer = font.render(word, True, dark_golden_rod)
            screen.blit(win_text, (760, 130))
            screen.blit(meaning_text, (780, 200))
            screen.blit(answer, (830, 250))

            screen.blit(meaning, (720, 300))

            smallText = pygame.font.Font("fonts/Pixelify.ttf", 30)
            text_surface, text_rect = text_object("NEXT", smallText)
            text_rect.center = ((880), (470))
            screen.blit(text_surface, text_rect)


        # bonus move
        elif point_player1 >= 20 or point_player2 >= 20:

            if turn == "player1":
                point_player1 = 0
            else:
                point_player2 = 0

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            sound = pygame.mixer.Sound("sounds/click.MP3")

            if 980 > mouse[0] > 780 and 490 > mouse[1] > 450:
                pygame.draw.rect(screen, "BLACK", (783, 453, 200,40), 0, 0, 30 ,30, 30, 30)
                pygame.draw.rect(screen, silver, (780,450,200,40), 0, 0, 30 ,30, 30, 30)

                if click[0] == 1:
                    sound.play()
                    total_turn += 1
                    return True, False, winner, total_turn, point_player1, point_player2, final_point_a, final_point_b

            else:
                pygame.draw.rect(screen, "BLACK", (783, 453, 200,40), 0, 0, 30 ,30, 30, 30)
                pygame.draw.rect(screen, light_steel_blue, (780,450,200,40), 0, 0, 30 ,30, 30, 30)

            win_text = big_font.render("Bonus", True, red)
            meaning_text = font.render("You can move free!!", True, dark_brown)
            answer = font.render(word, True, dark_golden_rod)
            screen.blit(win_text, (760, 130))
            screen.blit(meaning_text, (780, 200))
            screen.blit(answer, (830, 250))

            screen.blit(meaning, (720, 300))

            smallText = pygame.font.Font("fonts/Pixelify.ttf", 30)
            text_surface, text_rect = text_object("NEXT", smallText)
            text_rect.center = ((880), (470))
            screen.blit(text_surface, text_rect)

        pygame.display.update()
        clock.tick(FPS)
