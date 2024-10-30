"""This is a button and text Function"""
import pygame

dark_brown = 73, 56, 41
golden_rod = 218,165,32

screen = pygame.display.set_mode((1280, 720))


def profile(x, y, w, r, color, name, picture):
    """This is a button Function"""
    # draw a circle
    pygame.draw.circle(screen, "BLACK", (x,y), r+5)
    pygame.draw.circle(screen, color, (x,y), r)

    # picture
    screen.blit(picture, (x - 100, y - 130))

    # draw a point bar
    pygame.draw.rect(screen, "BLACK", (x - 93, y + 44, 180, 34), 0, 0, 50, 50, 50, 50)
    pygame.draw.rect(screen, golden_rod, (x - 88, y + 46, min(175 * (w/20), 175), 30), 0, 0, 50, 50, 50, 50)

    #name
    text = pygame.font.Font("fonts/Pixelify.ttf", 20)
    name = text.render(name, True, "WHITE")
    screen.blit(name, (x - 42, y + 48))

