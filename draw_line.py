"""selecting game mode"""
import pygame
screen = pygame.display.set_mode((1280, 720))
running = True

# map
map_game = pygame.image.load("images/game_map.png")
map_game = pygame.transform.scale(map_game, (1290, 730))
# 900 420, 980 460
clock = pygame.time.Clock()
fps = 60

brown = 95, 65, 22
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(map_game, (0, 0))

    click = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()

    if click[0] == 1:
        print(pos[0], pos[1])
    pygame.draw.line(screen, brown, (900, 420), (980, 460), 5)
    pygame.draw.line(screen, brown, (980, 380), (1060, 420), 5)
    pygame.draw.line(screen, brown, (1060, 340), (1140, 380), 5)
    pygame.draw.line(screen, brown, (1151, 292), (1233, 335), 5)
    pygame.draw.line(screen, brown, (1150, 290), (1216, 251), 5)
    pygame.draw.line(screen, brown, (1080, 250), (1140, 217), 5)
    pygame.draw.line(screen, brown, (1010, 219), (1080, 180), 5)
    pygame.draw.line(screen, brown, (1010, 218), (950, 188), 5)
    pygame.draw.line(screen, brown, (939, 259), (877, 225), 5)
    pygame.draw.line(screen, brown, (819, 258), (880, 294), 5)
    pygame.draw.line(screen, brown, (819, 257), (760, 290), 5)
    pygame.draw.line(screen, brown, (763, 232), (709, 263), 5)
    

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
