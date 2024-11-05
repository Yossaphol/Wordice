"""selecting game mode"""
import pygame
from buttons.button import *
from buttons.menu import button_menu


pygame.init()

# initialize volume levels
master_percent = 100
sfx_percent = 100
music_percent = 100

def setting_page():
    """return screen for selecting game mode"""
    global master_percent, sfx_percent, music_percent

    from main import main_page
    pygame.display.set_caption("Setting")
    screen = pygame.display.set_mode((1280, 720))
    running = True

    brown = 185, 156, 107
    dark_brown = 73, 56, 41
    bright_brown = 169, 161, 140
    wheat = 245, 222, 179

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

    master_slider = pygame.Rect(450 + (master_percent / 100) * (1020 - 450), 185, 30, 30)
    sfx_slider = pygame.Rect(450 + (sfx_percent / 100) * (1020 - 450), 335, 30, 30)
    music_slider = pygame.Rect(450 + (music_percent / 100) * (1020 - 450), 485, 30, 30)

    dragging_master = False
    dragging_sfx = False
    dragging_music = False

    def calculate_percentage(x_position):
        return int((x_position - 450) / (1020 - 450) * 100)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if master_slider.collidepoint(mouse_pos):
                    dragging_master = True
                elif sfx_slider.collidepoint(mouse_pos):
                    dragging_sfx = True
                elif music_slider.collidepoint(mouse_pos):
                    dragging_music = True
                elif back.get_rect(topleft=(30, 620)).collidepoint(mouse_pos):
                    # Go back to main page if back button clicked
                    main_page()
                    return
                elif next.get_rect(topleft=(1170, 620)).collidepoint(mouse_pos):
                    # Go to next page if next button clicked
                    main_page()
                    return

            elif event.type == pygame.MOUSEBUTTONUP:
                if dragging_master:
                    master_percent = calculate_percentage(master_slider.x)
                    print("Master Volume:", master_percent, "%")
                if dragging_sfx:
                    sfx_percent = calculate_percentage(sfx_slider.x)
                    print("SFX Volume:", sfx_percent, "%")
                if dragging_music:
                    music_percent = calculate_percentage(music_slider.x)
                    print("Music Volume:", music_percent, "%")
                
                dragging_master = dragging_sfx = dragging_music = False

            elif event.type == pygame.MOUSEMOTION:
                if dragging_master:
                    master_slider.x = max(450, min(1020, event.pos[0]))
                if dragging_sfx:
                    sfx_slider.x = max(450, min(1020, event.pos[0]))
                if dragging_music:
                    music_slider.x = max(450, min(1020, event.pos[0]))
            
        pygame.mixer.music.set_volume(music_percent*0.01)


        # background and settings title
        screen.fill(brown)
        font = pygame.font.Font("fonts/Pixelify_Sans/PixelifySans-Medium.ttf", 30)
        title_text = font.render("Settings", True, dark_brown)
        screen.blit(title_text, (50, 50))

        # sliders and bars
        pygame.draw.polygon(screen, dark_brown, [(50, 100), (1230, 100), (1230, 110), (50, 110)])
        for y in (150, 300, 450):
            pygame.draw.rect(screen, wheat, pygame.Rect(175, y, 900, 100), border_radius=20)
            pygame.draw.rect(screen, dark_brown, pygame.Rect(450, y + 45, 600, 10), border_radius=20)

        # slider buttons
        pygame.draw.rect(screen, bright_brown, master_slider, border_radius=30)
        pygame.draw.rect(screen, bright_brown, sfx_slider, border_radius=30)
        pygame.draw.rect(screen, bright_brown, music_slider, border_radius=30)

        # volume labels
        screen.blit(font.render("Master Volume", True, dark_brown), (200, 180))
        screen.blit(font.render("SFX Volume", True, dark_brown), (200, 330))
        screen.blit(font.render("Music Volume", True, dark_brown), (200, 480))

        # navigation buttons
        screen.blit(back, (30, 620))
        screen.blit(next, (1170, 620))

        pygame.display.update()

    pygame.quit()
    return sfx_percent, music_percent, master_percent
