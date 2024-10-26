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

def show_description(descript, x_start, y_start):
    """Show the multiline of word description"""

    brown = 185, 156, 107
    font = pygame.font.Font("fonts/Pixelify.ttf", 20)

    words = descript.split(" ")

    x = x_start
    y = y_start
    line_height = font.get_height() + 4

    for word in words:
        word_t = font.render(word, True, brown)
        word_width = word_t.get_width()

        if x + word_width <= 1000:
            screen.blit(word_t, (x, y))
            x += word_width + 2
        else:
            y += line_height
            x = x_start
            screen.blit(word_t, (x, y))
            x += word_width + 2

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

    if guess_color_code == [green for _ in range(len(word))]:
        point += 3

    spacing = 0
    for x in range(len(word)):
        rendered_char = font.render(user_guess[x], True, black)
        pygame.draw.rect(screen, guess_color_code[x], pygame.Rect(260 + spacing, 130 + (turns * 60), 50, 50))
        screen.blit(rendered_char, (270 + spacing, 130 + (turns * 60)))
        spacing += 60

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
    beige = 245,245,220
    powder_blue = 176,224,230

    background = pygame.image.load("images/background_game.jpg")
    background = pygame.transform.scale(background, (1280, 720))

    map_game = pygame.image.load("images/game_map_2.png")
    map_game = pygame.transform.scale(map_game, (1290, 730))

    player_1 = pygame.image.load("images/player_1.png")
    player_2 = pygame.image.load("images/player_2.png")
    player_1 = pygame.transform.scale(player_1, (230, 230))
    player_2 = pygame.transform.scale(player_2, (230, 230))

    bonus = pygame.image.load("images/bonus_duck.png")
    bonus = pygame.transform.scale(bonus, (250, 300))
    
    qeustion_mark = pygame.image.load("images/question.png")
    qeustion_mark = pygame.transform.scale(qeustion_mark, (180, 280))

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
                pygame.draw.rect(screen, grey, pygame.Rect(260 + (x * 60), 130 + (y * 60), 50, 50), 2)

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

        your_text = small.render("GUESSING :", True, dark_golden_rod)
        render_guess = font.render(guess, True, dark_brown)
        screen.blit(your_text, (280, 500))
        screen.blit(render_guess, (440, 490))
        
        txt_upper = small.render("type the word", True, dark_brown)
        txt_middle = small.render("that you think", True, dark_brown)
        txt_lower = small.render("it will be correct", True, dark_brown)
        screen.blit(txt_upper, (700, 440))
        screen.blit(txt_middle, (700, 480))
        screen.blit(txt_lower, (700, 520))
        
        screen.blit(qeustion_mark, (730, 150))

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

            pygame.draw.rect(screen, beige, (640, 120, 380, 480), 0, 0, 20, 20, 20, 20)
            pygame.draw.rect(screen, powder_blue, (660, 250, 343, 180), 0, 0, 20, 20, 20, 20)

            if 940 > mouse[0] > 740 and 490 > mouse[1] > 450:
                pygame.draw.rect(screen, "BLACK", (743, 453, 200,40), 0, 0, 30 ,30, 30, 30)
                pygame.draw.rect(screen, silver, (740,450,200,40), 0, 0, 30 ,30, 30, 30)

                if click[0] == 1:
                    sound.play()
                    total_turn += 1
                    if winner == "player1":
                        point_player1 = 0
                    else:
                        point_player2 = 0
                    return True, False, winner, total_turn, point_player1, point_player2, final_point_a, final_point_b

            else:
                pygame.draw.rect(screen, "BLACK", (743, 453, 200,40), 0, 0, 30 ,30, 30, 30)
                pygame.draw.rect(screen, light_steel_blue, (740,450,200,40), 0, 0, 30 ,30, 30, 30)

            win_text = big_font.render("You Win!", True, green)
            meaning_text = font.render("MEANING :", True, dark_brown)
            screen.blit(meaning_text, (750, 200))
            screen.blit(win_text, (720, 130))

            show_description(description, 690, 270)

            smallText = pygame.font.Font("fonts/Pixelify.ttf", 30)
            text_surface, text_rect = text_object("NEXT", smallText)
            text_rect.center = ((840), (470))
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

            pygame.draw.rect(screen, beige, (640, 120, 380, 480), 0, 0, 20, 20, 20, 20)
            pygame.draw.rect(screen, powder_blue, (660, 250, 343, 180), 0, 0, 20, 20, 20, 20)

            if 940 > mouse[0] > 740 and 490 > mouse[1] > 450:
                pygame.draw.rect(screen, "BLACK", (743, 453, 200,40), 0, 0, 30 ,30, 30, 30)
                pygame.draw.rect(screen, silver, (740,450,200,40), 0, 0, 30 ,30, 30, 30)

                if click[0] == 1:
                    sound.play()
                    total_turn += 1
                    return False, True, winner, total_turn, point_player1, point_player2, final_point_a, final_point_b

            else:
                pygame.draw.rect(screen, "BLACK", (743, 453, 200,40), 0, 0, 30 ,30, 30, 30)
                pygame.draw.rect(screen, light_steel_blue, (740,450,200,40), 0, 0, 30 ,30, 30, 30)

            win_text = big_font.render("You Lose!", True, red)
            meaning_text = font.render("THE WORD IS :", True, dark_brown)
            answer = font.render(word, True, dark_golden_rod)
            screen.blit(win_text, (700, 130))
            screen.blit(meaning_text, (715, 200))
            screen.blit(answer, (780, 250))

            show_description(description, 680, 300)

            smallText = pygame.font.Font("fonts/Pixelify.ttf", 30)
            text_surface, text_rect = text_object("NEXT", smallText)
            text_rect.center = ((840), (470))
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

            pygame.draw.rect(screen, beige, (640, 120, 380, 480), 0, 0, 20, 20, 20, 20)
            pygame.draw.rect(screen, powder_blue, (660, 250, 343, 180), 0, 0, 20, 20, 20, 20)
            screen.blit(bonus, (700, 200))

            if 940 > mouse[0] > 740 and 490 > mouse[1] > 450:
                pygame.draw.rect(screen, "BLACK", (743, 453, 200,40), 0, 0, 30 ,30, 30, 30)
                pygame.draw.rect(screen, silver, (740,450,200,40), 0, 0, 30 ,30, 30, 30)

                if click[0] == 1:
                    sound.play()
                    total_turn += 1
                    return True, False, winner, total_turn, point_player1, point_player2, final_point_a, final_point_b

            else:
                pygame.draw.rect(screen, "BLACK", (743, 453, 200,40), 0, 0, 30 ,30, 30, 30)
                pygame.draw.rect(screen, light_steel_blue, (740,450,200,40), 0, 0, 30 ,30, 30, 30)

            win_text = big_font.render("Bonus", True, red)
            meaning_text = small.render("You can move free!!", True, dark_brown)
            screen.blit(win_text, (750, 130))
            screen.blit(meaning_text, (690, 200))


            smallText = pygame.font.Font("fonts/Pixelify.ttf", 30)
            text_surface, text_rect = text_object("NEXT", smallText)
            text_rect.center = ((840), (470))
            screen.blit(text_surface, text_rect)

        pygame.display.update()
        clock.tick(FPS)
