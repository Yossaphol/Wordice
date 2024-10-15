"""selecting game mode"""
import pygame
from button import *
from game_2_players import game_2_players
from menu import button_menu

def select_player():
    """return screen for selecting game mode"""
    from main import main_page
    pygame.display.set_caption("Select player")
    screen = pygame.display.set_mode((1280, 720))
    running = True

    brown = 185, 156, 107
    bright_brown = 169, 161, 140
    dark_brown = 73, 56, 41
    silver = 192,192,192
    gainsboro = 220,220,220

    font = pygame.font.Font("fonts/Pixelify_Sans/PixelifySans-Medium.ttf", 50)

    back = pygame.image.load("images/back.png")
    back_hover = pygame.image.load("images/back_hover.png")
    back = pygame.transform.scale(back, (80, 80))
    back_hover = pygame.transform.scale(back_hover, (80, 80))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        background = pygame.image.load("images/background_selecting_page.jpg")

        background = pygame.transform.scale(background, (1280, 720))

        screen.blit(background, (0, 0))

        # text
        text1 = font.render("HOW MANY PLAYERS??", True, dark_brown)

        button("2 PLAYER", 45, 140, 200, 1000, 80, brown, bright_brown, game_2_players)
        button("3 PLAYER", 45, 140, 300, 1000, 80, brown, bright_brown, )
        button("4 PLAYER", 45, 140, 400, 1000, 80, brown, bright_brown, )

        button_menu(30, 620, 150, 60, back, back_hover, main_page)
        screen.blit(text1, (380, 100))

        pygame.display.update()

    pygame.quit()
