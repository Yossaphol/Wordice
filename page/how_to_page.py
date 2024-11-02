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
    lightblue = 205, 223, 255

    mouse = pygame.mouse.get_pressed()
    scrolls = 0

    pygame.mixer.music.load("sounds/sound.mp3")
    pygame.mixer.music.play(-1)

    #back / left button
    back = pygame.image.load("images/back.png")
    back_hover = pygame.image.load("images/back_hover.png")
    back = pygame.transform.scale(back, (80, 80))
    back_hover = pygame.transform.scale(back_hover, (80, 80))

    #next / right button
    next = pygame.image.load("images/next.png")
    next_hover = pygame.image.load("images/next_hover.png")
    next = pygame.transform.scale(next, (80, 80))
    next_hover = pygame.transform.scale(next_hover, (80, 80))

    #quit button
    quit = pygame.image.load("images/quit.png")
    quit_hover = pygame.image.load("images/quit_hover.png")
    quit = pygame.transform.scale(quit, (150, 70))
    quit_hover = pygame.transform.scale(quit_hover, (150, 70))


    howto_pic = [
        "images/hottoplay/How To Play.zip - 2.png",
        "images/hottoplay/How To Play.zip - 5.png",
        "images/hottoplay/How To Play.zip - 6.png",
        "images/hottoplay/How To Play.zip - 7.png",
        "images/hottoplay/How To Play.zip - 8.png",
        "images/hottoplay/How To Play.zip - 9.png"
    ]

    pic_index = 0

    current_pic = pygame.image.load(howto_pic[pic_index])
    current_pic = pygame.transform.scale(current_pic, (1290, 730))


    while running:

        screen.fill(lightblue)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                # quit button back to main page
                if quit.get_rect(topleft=(20, 620)).collidepoint(mouse_pos):
                    main_page()
                    return

                # right click button to change page
                elif next.get_rect(topleft=(1170, 320)).collidepoint(mouse_pos):
                    pic_index = (pic_index + 1) % len(howto_pic)
                    current_pic = pygame.image.load(howto_pic[pic_index])
                    current_pic = pygame.transform.scale(current_pic, (1290, 730))

                # left click button to change page (left side)
                elif back.get_rect(topleft=(30, 320)).collidepoint(mouse_pos):
                    pic_index = (pic_index - 1) % len(howto_pic)
                    current_pic = pygame.image.load(howto_pic[pic_index])
                    current_pic = pygame.transform.scale(current_pic, (1290, 730))

        #button position
        button_menu(20, 620, 150, 60, quit, quit_hover, main_page) # bttom left
        button_menu(30, 320, 150, 60, back, back_hover) #cent left
        button_menu(1170, 320, 150, 60, next, next_hover) #cent right

        screen.blit(current_pic, (0, 0))

        pygame.display.update()

    pygame.quit()
