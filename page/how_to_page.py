"""selecting game mode"""
import pygame
from buttons.menu import button_menu

def how_to_page():
    """return screen for selecting game mode"""
    from main import main_page
    pygame.display.set_caption("How to play")
    screen = pygame.display.set_mode((1280, 720))
    running = True

    brown = 185, 156, 107
    silver = 192,192,192
    gainsboro = 220,220,220

    mouse = pygame.mouse.get_pressed()
    scrolls = 0

    pygame.mixer.music.load("sounds/sound.mp3")
    pygame.mixer.music.play(-1)

    back = pygame.image.load("images/back.png")
    back_hover = pygame.image.load("images/back_hover.png")
    back = pygame.transform.scale(back, (80, 80))
    back_hover = pygame.transform.scale(back_hover, (80, 80))
    next = pygame.image.load("images/next.png")
    next_hover = pygame.image.load("images/next_hover.png")
    next = pygame.transform.scale(next, (80, 80))
    next_hover = pygame.transform.scale(next_hover, (80, 80))

    howtoplay = pygame.image.load("images/hottoplay/How To Play.zip - 2.png")
    howtoplay = pygame.transform.scale(howtoplay, (1290, 730))

    while running:

        screen.fill(brown)
        screen.blit(howtoplay, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        button_menu(30, 620, 150, 60, back, back_hover, main_page)
        button_menu(1170, 620, 150, 60, next, next_hover,main_page)
        
        pygame.display.update()

    pygame.quit()
