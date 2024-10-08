"""selecting game mode"""
import pygame
from button import *

def setting_page():
    """return screen for selecting game mode"""
    
    from main import main_page
    pygame.display.set_caption("Setting")
    screen = pygame.display.set_mode((1280, 720))
    running = True

    brown = 185, 156, 107
    dark_brown = 73, 56, 41
    bright_brown = 169, 161, 140

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(brown)

        text = pygame.font.Font("fonts/Pixelify_Sans/PixelifySans-Medium.ttf", 30)
        text_screen = text.render("Settings", True, dark_brown)
        screen.blit(text_screen, (50, 50))

        pygame.draw.polygon(screen, dark_brown, [(50, 100), (1230, 100), (1230, 110), (50, 110)])
        pygame.draw.rect(screen, dark_brown, pygame.Rect(175, 150, 900, 100), border_radius=20)
        pygame.draw.rect(screen, dark_brown, pygame.Rect(175, 300, 900, 100), border_radius=20)
        pygame.draw.rect(screen, dark_brown, pygame.Rect(175, 450, 900, 100), border_radius=20)

        button("APPLY", 45, 540, 585, 200, 80, brown, bright_brown, main_page)

        pygame.display.update()

    pygame.quit()
