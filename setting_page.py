"""selecting game mode"""
import pygame
from button import *
from menu import button_menu

def setting_page():
    """return screen for selecting game mode"""
    
    from main import main_page
    pygame.display.set_caption("Setting")
    screen = pygame.display.set_mode((1280, 720))
    running = True

    brown = 185, 156, 107
    silver = 192,192,192
    gainsboro = 220,220,220
    brown = 185, 156, 107
    dark_brown = 73, 56, 41
    bright_brown = 169, 161, 140
    wheat = 245,222,179
    lemon = 255, 250, 205
    black = 0, 0, 0

    back = pygame.image.load("images/back.png")
    back_hover = pygame.image.load("images/back_hover.png")
    back = pygame.transform.scale(back, (80, 80))
    back_hover = pygame.transform.scale(back_hover, (80, 80))
    next = pygame.image.load("images/next.png")
    next_hover = pygame.image.load("images/next_hover.png")
    next = pygame.transform.scale(next, (80, 80))
    next_hover = pygame.transform.scale(next_hover, (80, 80))


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

        button_menu(30, 620, 150, 60, back, back_hover, main_page)
        button_menu(1170, 620, 150, 60, next, next_hover, main_page)
        pygame.display.update()

    pygame.quit()
