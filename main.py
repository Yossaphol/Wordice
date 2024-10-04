# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
font_wordle = pygame.font.Font('fonts/Jersey20.ttf',64)
font_main_text = pygame.font.Font('fonts/pixelifySans.ttf', 80)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#50495F")

    head_text = font_main_text.render('Wordice', True, (255, 255, 255))
    screen.blit(head_text, (30,60))
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()