"""winner alert box"""
import pygame
import sys

screen = pygame.display.set_mode((1280, 720))

def winner(winner_name, a_point, b_point):
    """show when any player win"""

    pygame.init()

    dark_brown = 73, 56, 41
    burly_wood = 222,184,135
    light_steel_blue  = 176,196,222
    silver = 192,192,192
    grey = 128,128,128
    brown = 185, 156, 107
    golden_rod = 218,165,32

    pygame.draw.rect(screen, grey, (243, 113, 803, 503), 0, 0, 20, 20, 20, 20)
    pygame.draw.rect(screen, burly_wood, (240, 110, 800, 500), 0, 0, 20, 20, 20, 20)

    text = pygame.font.Font("fonts/Pixelify.ttf", 30)
    cong = text.render("WINNER IS", True, dark_brown,)
    name = text.render(winner_name, True, "RED")
    screen.blit(cong, (475, 150))
    screen.blit(name, (650, 150))
    a_point = text.render(str(a_point), True, dark_brown)

    b_point = text.render(str(b_point), True, dark_brown)
    screen.blit(a_point, (425, 460))
    screen.blit(b_point, (825, 460))

    pygame.draw.circle(screen, brown, (350, 500), 50)

    pygame.draw.circle(screen, brown, (750, 500), 50)

    pygame.draw.circle(screen, brown, (640, 320), 100)

    pygame.draw.rect(screen, "BLACK", (400, 500, 185, 45), 0, 0, 50, 50, 50, 50)
    pygame.draw.rect(screen, golden_rod, (400, 500, 100, 40), 0, 0, 50, 0, 50, 0)

    pygame.draw.rect(screen, "BLACK", (800, 500, 185, 45), 0, 0, 50, 50, 50, 50)
    pygame.draw.rect(screen, golden_rod, (800, 500, 100, 40), 0, 0, 50, 0, 50, 0)

    duck1 = pygame.image.load("images/player_1.png")
    duck1 = pygame.transform.scale(duck1, (150, 150))
    duck2 = pygame.image.load("images/player_2_flip.png")
    duck2 = pygame.transform.scale(duck2, (150, 150))

    if winner_name == "PLAYER1":
        win_duck = pygame.transform.scale(duck1, (250, 250))
    else:
        win_duck = pygame.transform.scale(duck2, (250, 250))

    screen.blit(duck1, (285, 425))
    screen.blit(duck2, (670, 425))
    screen.blit(win_duck, (500, 200))
