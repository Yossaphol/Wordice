"""selecting game mode"""
import pygame
from button import button

def how_to_page():
    """return screen for selecting game mode"""
    pygame.display.set_caption("How to play")
    screen = pygame.display.set_mode((1280, 720))
    running = True

    brown = 185, 156, 107
    silver = 192,192,192
    gainsboro = 220,220,220

    mouse = pygame.mouse.get_pressed()
    scrolls = 0

    while running:

        screen.fill(brown)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
