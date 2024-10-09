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
    wheat = 245,222,179
    lemon = 255, 250, 205
    black = 0, 0, 0


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False                
        screen.fill(brown)

        text = pygame.font.Font("fonts/Pixelify_Sans/PixelifySans-Medium.ttf", 30)
        text_screen = text.render("Settings", True, dark_brown)
        screen.blit(text_screen, (50, 50))

        pygame.draw.polygon(screen, dark_brown, [(50, 100), (1230, 100), (1230, 110), (50, 110)])
        pygame.draw.rect(screen, wheat, pygame.Rect(175, 150, 900, 100), border_radius=20)
        pygame.draw.rect(screen, wheat, pygame.Rect(175, 300, 900, 100), border_radius=20)
        pygame.draw.rect(screen, wheat, pygame.Rect(175, 450, 900, 100), border_radius=20)
        # slide bar
        pygame.draw.rect(screen, dark_brown, pygame.Rect(450, 195, 600, 10), border_radius=20)
        pygame.draw.rect(screen, dark_brown, pygame.Rect(450, 345, 600, 10), border_radius=20)
        pygame.draw.rect(screen, dark_brown, pygame.Rect(450, 495, 600, 10), border_radius=20)
        # drag and drop in slide bar
        pygame.draw.rect(screen, bright_brown, pygame.Rect(450, 185, 30, 30), border_radius=30)
        pygame.draw.rect(screen, bright_brown, pygame.Rect(450, 335, 30, 30), border_radius=30)
        pygame.draw.rect(screen, bright_brown, pygame.Rect(450, 485, 30, 30), border_radius=30)


        master = text.render("Master Volume", True, dark_brown)
        sfx = text.render("SFX Volume", True, dark_brown)
        music = text.render("Music Volume", True, dark_brown)

        screen.blit(master, (200, 180))
        screen.blit(sfx, (200, 330))
        screen.blit(music, (200, 480))

        button("APPLY", 45, 540, 585, 200, 80, wheat, lemon, main_page)

        pygame.display.update()

    pygame.quit()
