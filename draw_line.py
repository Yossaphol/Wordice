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
    pygame.draw.line(screen, brown, (896, 426), (966, 468), 5)
    pygame.draw.line(screen, brown, (962, 390), (1034, 434), 5)
    pygame.draw.line(screen, brown, (1027, 358), (1101, 401), 5)
    pygame.draw.line(screen, brown, (1088, 324), (1168, 370), 5)
    pygame.draw.line(screen, brown, (1151, 292), (1233, 335), 5)
    pygame.draw.line(screen, brown, (1150, 290), (1216, 251), 5)
    pygame.draw.line(screen, brown, (1080, 250), (1140, 217), 5)
    pygame.draw.line(screen, brown, (1010, 219), (1080, 180), 5)
    pygame.draw.line(screen, brown, (1010, 218), (950, 188), 5)
    pygame.draw.line(screen, brown, (939, 259), (877, 225), 5)
    pygame.draw.line(screen, brown, (819, 258), (880, 294), 5)
    pygame.draw.line(screen, brown, (819, 257), (760, 290), 5)
    pygame.draw.line(screen, brown, (763, 233), (706, 264), 5)
    pygame.draw.line(screen, brown, (650, 232), (706, 264), 5)
    pygame.draw.line(screen, brown, (557, 349), (490, 310), 5)
    pygame.draw.line(screen, brown, (566, 273), (628, 310), 5)
    pygame.draw.line(screen, brown, (558, 349), (491, 385), 5)
    pygame.draw.line(screen, brown, (561, 429), (490, 387), 5)
    pygame.draw.line(screen, brown, (383, 442), (450, 481), 5)
    pygame.draw.line(screen, brown, (435, 414), (510, 458), 5)
    pygame.draw.line(screen, brown, (383, 440), (323, 475), 5)
    pygame.draw.line(screen, brown, (305, 407), (254, 437), 5)
    pygame.draw.line(screen, brown, (239, 371), (183, 406), 5)
    pygame.draw.line(screen, brown, (170, 341), (118, 371), 5)
    pygame.draw.line(screen, brown, (108, 308), (64, 334), 5)
    pygame.draw.line(screen, brown, (110, 306), (55, 272), 5)
    pygame.draw.line(screen, brown, (232, 248), (174, 214), 5)
    pygame.draw.line(screen, brown, (122, 243), (171, 274), 5)
    pygame.draw.line(screen, brown, (304, 231), (255, 260), 5)
    pygame.draw.line(screen, brown, (309, 229), (362, 261), 5)
    pygame.draw.line(screen, brown, (380, 195), (433, 227), 5)
    pygame.draw.line(screen, brown, (453, 158), (506, 191), 5)
    pygame.draw.line(screen, brown, (524, 122), (581, 157), 5)
    pygame.draw.line(screen, brown, (597, 89), (648, 122), 5)


    pygame.display.update()
    clock.tick(fps)

pygame.quit()
