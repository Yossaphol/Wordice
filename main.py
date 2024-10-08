"""main page"""
import pygame
import pygame.locals
import sys
from button import *
from select_player import *
from setting_page import *
from how_to_page import *

pygame.init()

def main_page():
    """return first page of exiting game"""
    running = True
    FPS = 30
    y = 120
    x_cloud1 = 0
    x_cloud2 = 0
    down = True
    time = 0

    pygame.display.set_caption("Bordice")

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    # setup images
    background = pygame.image.load("images/background_test.jpg")
    logo = pygame.image.load("images/logo.png")
    superman  = pygame.image.load("images/superman.png")
    cloud1 = pygame.image.load("images/cloud1.png")
    cloud2 = pygame.image.load("images/cloud2.png")
    cloud3 = pygame.image.load("images/cloud3.png")
    cloud4 = pygame.image.load("images/cloud4.png")
    # images tranfrom
    logo = pygame.transform.scale(logo, (370, 280))
    background = pygame.transform.scale(background, (1280, 720))

    # setup color
    brown = 185, 156, 107
    bright_brown = 169, 161, 140

    # run page
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0,0))
        # cloud
        screen.blit(cloud1, (x_cloud1, 10))
        screen.blit(cloud2, (x_cloud2 + 800, 80))
        screen.blit(cloud3, (x_cloud2 - 400, 150))
        screen.blit(cloud4, (x_cloud1 + 500, -100))
        screen.blit(cloud1, (x_cloud2 - 1300, 200))
        screen.blit(cloud2, (x_cloud1 - 2100, 100))
        screen.blit(cloud3, (x_cloud1 - 1400, 150))
        screen.blit(cloud4, (x_cloud2 - 3000 , -100))

        screen.blit(logo, (75, 10))
        screen.blit(superman, (750, y))

        # cloud transition
        if time < 3500:
            time += 1
            x_cloud1 += 1
            x_cloud2 += 2
        else:
            time = 0
            x_cloud1 = -1000
            x_cloud2 = -1000

        # superman transition
        if down:
            y += 1
            if y >= 150:
                down = False
        else:
            y -= 1
            if y < 120:
                down = True

        # button on screen
        #      txt /font_size /x   /y    /w   /h  /init_color /action_color /action
        button("START", 50, 150, 300, 250, 80, brown, bright_brown, select_player)
        button("SETTING", 50, 125, 400, 300, 80, brown, bright_brown, setting_page)
        button("HOW TO PLAY", 50, 50, 500, 450, 80, brown, bright_brown, how_to_page)
        button("QUIT", 50, 150, 600, 250, 80, brown, bright_brown, sys.exit)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

main_page()
