"""selecting game mode"""
import pygame
from button import *
from menu import button_menu

def setting_page():
    """return screen for selecting game mode"""

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

    # slider positions default at 100%
    master_slider = pygame.Rect(1020, 185, 30, 30)
    sfx_slider = pygame.Rect(1020, 335, 30, 30)
    music_slider = pygame.Rect(1020, 485, 30, 30)

    # flags for dragging
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
                # start dragging if slider is clicked
                if master_slider.collidepoint(event.pos):
                    dragging_master = True
                elif sfx_slider.collidepoint(event.pos):
                    dragging_sfx = True
                elif music_slider.collidepoint(event.pos):
                    dragging_music = True

            elif event.type == pygame.MOUSEBUTTONUP:
                # stop dragging and print the percentage
                if dragging_master:
                    master_percent = calculate_percentage(master_slider.x)
                    print("Master Volume:", master_percent, "%")
                if dragging_sfx:
                    sfx_percent = calculate_percentage(sfx_slider.x)
                    print("SFX Volume:", sfx_percent, "%")
                if dragging_music:
                    music_percent = calculate_percentage(music_slider.x)
                    print("Music Volume:", music_percent, "%")

                # reset dragging flags
                dragging_master = dragging_sfx = dragging_music = False

            elif event.type == pygame.MOUSEMOTION:
                # update slider position while dragging
                if dragging_master:
                    master_slider.x = max(450, min(1020, event.pos[0]))
                if dragging_sfx:
                    sfx_slider.x = max(450, min(1020, event.pos[0]))
                if dragging_music:
                    music_slider.x = max(450, min(1020, event.pos[0]))

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
        button_menu(30, 620, 150, 60, back, back_hover, main_page)
        button_menu(1170, 620, 150, 60, next, next_hover, main_page)

        pygame.display.update()

    pygame.quit()
