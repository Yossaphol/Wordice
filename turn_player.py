"""Function for switch turn of player"""

import pygame

screen = pygame.display.set_mode((1280,720))

def turn_player(x, y):
    """player one turn"""
    red = 255,0,0
    img = pygame.image.load("images/marker.png")
    text = pygame.font.Font("fonts/Pixelify.ttf", 20)
    img = pygame.transform.scale(img, (20, 30))
    turn_mark = text.render("YOUR TURN", True, red)
    screen.blit(turn_mark, (x, y))
    screen.blit(img, (x - 28, y - 5))
