"""main page"""
import pygame
import pygame.locals
import sys
from setting_page import setting_page
from how_to_page import how_to_page
from menu import button_menu
from game_2_players import game_2_players

pygame.init()

def main_page():
    """return first page of exiting game"""
    running = True
    FPS = 30
    y = 100
    y_duck = 50
    x_cloud1 = 0
    x_cloud2 = 0
    down = True
    down_duck = True

    time = 0

    pygame.mixer.music.load("sounds/sound.mp3")
    pygame.mixer.music.play(-1)

    pygame.display.set_caption("Bordice")

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    # setup images
    background = pygame.image.load("images/background_test.jpg")
    logo = pygame.image.load("images/logo.png")
    duck = pygame.image.load("images/duck.png")
    cloud1 = pygame.image.load("images/cloud1.png")
    cloud2 = pygame.image.load("images/cloud2.png")
    cloud3 = pygame.image.load("images/cloud3.png")
    cloud4 = pygame.image.load("images/cloud4.png")
    dice = pygame.image.load("images/dice.png")

    start = pygame.image.load("images/play.gif")
    start_hover = pygame.image.load("images/start_hover.png")
    setting = pygame.image.load("images/setting.png")
    setting_hover = pygame.image.load("images/setting_hover.png")
    how = pygame.image.load("images/how.png")
    how_hover = pygame.image.load("images/how_hover.png")
    quit = pygame.image.load("images/quit.png")
    quit_hover = pygame.image.load("images/quit_hover.png")
    # images tranfrom
    duck = pygame.transform.scale(duck, (450, 700))
    logo = pygame.transform.scale(logo, (370, 280))
    background = pygame.transform.scale(background, (1280, 720))
    dice = pygame.transform.scale(dice, (200, 200))

    start = pygame.transform.scale(start, (200, 90))
    start_hover = pygame.transform.scale(start_hover, (200, 90))
    setting = pygame.transform.scale(setting, (250, 90))
    setting_hover = pygame.transform.scale(setting_hover, (250, 90))
    how = pygame.transform.scale(how, (450, 90))
    how_hover = pygame.transform.scale(how_hover, (450, 90))
    quit = pygame.transform.scale(quit, (200, 90))
    quit_hover = pygame.transform.scale(quit_hover, (200, 90))

    # width and height of button
    start_w = start.get_width()
    start_h = start.get_height()
    setting_w = setting.get_width()
    setting_h = setting.get_height()
    how_w = how.get_width()
    how_h = how.get_height()
    quit_w = quit.get_width()
    quit_h = quit.get_height()

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
        screen.blit(duck, (650, y_duck))
        screen.blit(dice, (850, y))

        # cloud transition
        if time < 3500:
            time += 1
            x_cloud1 += 1
            x_cloud2 += 2
        else:
            time = 0
            x_cloud1 = -1000
            x_cloud2 = -1000

        # duck transition
        if down_duck:
            y_duck += 0.5
            if y_duck >= 50:
                down_duck = False
        else:
            y_duck -= 0.5
            if y_duck < 40:
                down_duck = True

        if down:
            y += 1
            if y >= 140:
                down = False
        else:
            y -= 1
            if y < 110:
                down = True

        # button on screen
        button_menu(185, 280, start_w, start_h, start, start_hover, game_2_players)
        button_menu(155, 370,setting_w, setting_h, setting, setting_hover, setting_page)
        button_menu(60, 460, how_w, how_h, how, how_hover, how_to_page)
        button_menu(185, 550, quit_w, quit_h, quit, quit_hover, sys.exit)

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

main_page()
