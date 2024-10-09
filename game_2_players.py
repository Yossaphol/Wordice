"""selecting game mode"""
import pygame
from player_profile import profile

def game_2_players():
    """return screen for selecting game mode"""
    pygame.display.set_caption("Bordice 1Vs1")
    screen = pygame.display.set_mode((1280, 720))
    sound = pygame.mixer.Sound("sounds/sound.mp3")
    sound.play()
    
    running = True

    brown = 185, 156, 107
    line_color = 95, 65, 22

    # cloud
    cloud1 = pygame.image.load("images/cloud1.png")
    cloud2 = pygame.image.load("images/cloud2.png")
    cloud3 = pygame.image.load("images/cloud3.png")
    cloud4 = pygame.image.load("images/cloud4.png")

    # map
    map_game = pygame.image.load("images/game_map.png")
    map_game = pygame.transform.scale(map_game, (1290, 730))

    # background
    background = pygame.image.load("images/background_game.jpg")
    background = pygame.transform.scale(background, (1280, 720))

    # player
    player_1 = pygame.image.load("images/player_1.png")
    player_2 = pygame.image.load("images/player_2.png")
    player_1 = pygame.transform.scale(player_1, (230, 230))
    player_2 = pygame.transform.scale(player_2, (230, 230))

    # cloud position
    x_cloud1 = 0
    x_cloud2 = 0

    time = 0

    clock = pygame.time.Clock()
    fps = 30

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))

        screen.blit(cloud1, (x_cloud1, 10))
        screen.blit(cloud2, (x_cloud2 + 800, 80))
        screen.blit(cloud3, (x_cloud2 - 400, 40))
        screen.blit(cloud4, (x_cloud1 + 500, 50))
        screen.blit(cloud1, (x_cloud2 - 1300, 600))
        screen.blit(cloud2, (x_cloud1 - 2100, 100))
        screen.blit(cloud3, (x_cloud1 - 1400, 150))
        screen.blit(cloud4, (x_cloud2 - 3000 , 700))


        if time < 3500:
            time += 1
            x_cloud1 += 1
            x_cloud2 += 2
        else:
            time = 0
            x_cloud1 = -1000
            x_cloud2 = -1000

        screen.blit(map_game, (0, 0))

        profile(130, 630, 110, 30, 70, brown, "PLAYER 1", player_1)
        profile(1150, 120, 110, 30, 70, brown, "PLAYER 2", player_2)

        # draw a box for move
        # pygame.draw.line(screen, line_color, (250,0), (250,500), 50)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
