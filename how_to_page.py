"""selecting game mode"""
import pygame

def how_to_page():
    """return screen for selecting game mode"""
    pygame.display.set_caption("How to play")
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
        text_screen = text.render("This is screen for discribe How to play this game.", True, dark_brown)
        screen.blit(text_screen, (300, 300))

        pygame.display.update()

    pygame.quit()
