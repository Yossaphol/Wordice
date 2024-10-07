"""selecting game mode"""
import pygame
from button import *

def select_size():
    """return screen for selecting game mode"""
    screen = pygame.display.set_mode((1280, 720))
    running = True

    brown = 185, 156, 107
    bright_brown = 169, 161, 140
    dark_brown = 73, 56, 41
    bright_circle = 241, 222, 132
    brown_circle = 77, 52, 13

    font = pygame.font.Font("fonts/Pixelify_Sans/PixelifySans-Medium.ttf", 50)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        background = pygame.image.load("images/background_selecting_page.jpg")

        background = pygame.transform.scale(background, (1280, 720))

        screen.blit(background, (0, 0))

        # text
        text1 = font.render("WHAT SIZE THAT YOU WANT", True, dark_brown)

        button("5 X 5", 45, 140, 200, 1000, 80, brown, bright_brown, )
        button("6 X 6", 45, 140, 300, 1000, 80, brown, bright_brown, )
        button("7 X 7", 45, 140, 400, 1000, 80, brown, bright_brown, )

        screen.blit(text1, (340, 100))

        pygame.display.update()

    pygame.quit()
