"""selecting game mode"""
import pygame

def setting_page():
    """return screen for selecting game mode"""
    pygame.display.set_caption("Setting")
    screen = pygame.display.set_mode((1280, 720))
    running = True

    brown = 185, 156, 107
    dark_brown = 73, 56, 41

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(brown)

        text = pygame.font.Font("fonts/Pixelify_Sans/PixelifySans-Medium.ttf", 30)
        text_screen = text.render("This is screen for setting.", True, dark_brown)
        screen.blit(text_screen, (400, 300))

        pygame.display.update()

    pygame.quit()
