"""This is a button and text Function"""
import pygame

screen = pygame.display.set_mode((1280, 720))
dark_brown = 73, 56, 41

def text_object(txt, font):
    """return text"""
    text_surface = font.render(txt, True, dark_brown)
    return text_surface, text_surface.get_rect()

def button(txt, font_size, x, y, w, h, init_color, action_color, action = None):
    """This is a button Function"""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    sound = pygame.mixer.Sound("sounds/click.MP3")
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, "BLACK", (x + 3, y + 3,w,h), 0, 0, 30 ,30, 30, 30)
        pygame.draw.rect(screen, action_color, (x,y,w,h), 0, 0, 30 ,30, 30, 30)

        if click[0] == 1 and action != None:
            sound.play()
            action()


    else:
        pygame.draw.rect(screen, "BLACK", (x + 3, y + 3,w,h), 0, 0, 30 ,30, 30, 30)
        pygame.draw.rect(screen, init_color, (x,y,w,h), 0, 0, 30 ,30, 30, 30)

    smallText = pygame.font.Font("fonts/Pixelify_Sans/PixelifySans-Bold.ttf", font_size)
    text_surface, text_rect = text_object(txt, smallText)
    text_rect.center = ((x + w/2), (y + h/2))
    screen.blit(text_surface, text_rect)
