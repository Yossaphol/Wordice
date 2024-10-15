"""selecting game mode"""
import pygame
screen = pygame.display.set_mode((1280, 720))
running = True

# map
map_game = pygame.image.load("images/game_map_2.png")
map_game = pygame.transform.scale(map_game, (1290, 730))
# 900 420, 980 460
clock = pygame.time.Clock()
fps = 60
brown = 95, 65, 22

duck = pygame.image.load("images/player_1.png")
duck = pygame.transform.scale(duck, (100, 100))
duck_flip = pygame.image.load("images/player_1_flip.png")
duck_flip = pygame.transform.scale(duck_flip, (100, 100))



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(map_game, (0, 0))
    screen.blit(duck, (825, 400))
    screen.blit(duck, (860, 420))

    click = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()

    if click[0] == 1:
        print(pos[0], pos[1])

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
