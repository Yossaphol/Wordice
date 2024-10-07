"""This is a button and text Function"""
import pygame

screen = pygame.display.set_mode((1280, 720))
dark_brown = 73, 56, 41

def radio_button(x, y, r, init_color, action_color):
    """This is a button Function"""
    lst = [0]
    click = pygame.mouse.get_pressed()

    pygame.draw.circle(screen, init_color, (x,y), r)

    if click[0] == 1:
        lst[0] = 1
    if lst[0] == 1:
        pygame.draw.circle(screen, action_color, (x,y), r)
