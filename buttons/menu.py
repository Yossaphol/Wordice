"""This is a button and text Function"""
import pygame

screen = pygame.display.set_mode((1280, 720))
dark_brown = 73, 56, 41

def button_menu(x, y, w, h, init_images, action_images, action = None):
    """This is a button Function"""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    sound = pygame.mixer.Sound("sounds/click.MP3")
    if x+w > mouse[0] > x and y+h > mouse[1] > y:

        screen.blit(action_images, (x, y, w, h))

        if click[0] == 1 and action != None:
            sound.play()
            action()


    else:
        screen.blit(init_images, (x, y, w, h))
