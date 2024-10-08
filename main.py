"""main page"""
import pygame
import pygame.locals

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
start_button = pygame.image.load("images/start_button_test.png")
setting_button = pygame.image.load("images/setting_button_test.png")
quit_button = pygame.image.load("images/quit_button_test.png")
background = pygame.image.load("images/background_first_page.png")
logo = pygame.image.load("images/logo_test.png")

new_start = pygame.transform.scale(start_button, (350, 150))
new_setting = pygame.transform.scale(setting_button, (300, 170))
new_quit = pygame.transform.scale(quit_button, (350, 150))
new_background = pygame.transform.scale(background, (900, 600))
new_logo = pygame.transform.scale(logo, (500, 300))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("pink")
    screen.blit(new_start, (50, 300))
    screen.blit(new_setting, (70, 400))
    screen.blit(new_quit, (50, 510))
    screen.blit(new_background, (370, 130))
    screen.blit(new_logo, (5, 5))

    # pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
