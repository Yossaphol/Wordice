"""selecting game mode"""
import pygame
screen = pygame.display.set_mode((1280, 720))
running = True

# map
map_game = pygame.image.load("images/game_map.png")
map_game = pygame.transform.scale(map_game, (1290, 730))

clock = pygame.time.Clock()
fps = 30

f = 0
g = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            g -= 10
        if keys[pygame.K_s]:
            g += 10
        if keys[pygame.K_a]:
            f -= 10
        if keys[pygame.K_d]:
            f += 10
    screen.blit(map_game, (0, 0))

    pygame.draw.circle(screen, (240,128,128), (f,g), 10)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()

