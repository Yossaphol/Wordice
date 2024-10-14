"""selecting game mode"""
import pygame
from player_profile import profile
import random

def game_2_players():
    """return screen for selecting game mode"""
    pygame.display.set_caption("Bordice 1Vs1")
    screen = pygame.display.set_mode((1280, 720))
    sound = pygame.mixer.Sound("sounds/sound.mp3")
    sound.play()

    running = True

    bright_brown = 169, 161, 140
    wheat = 245,222,179
    brown = 185, 156, 107

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

    times = 0

    clock = pygame.time.Clock()
    fps = 30

    # dice rolling
    dice_images = [pygame.image.load(f"images/dice/{num}.png") for num in range(1, 7)]
    dice_rolling_images = [pygame.image.load(f"images/dice/{num}.png") for num in range(1, 7)]

    is_rolling = False
    rolling_img_cnt = 0
    dice_num_image = dice_images[0]

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


        if times < 3500:
            times += 1
            x_cloud1 += 1
            x_cloud2 += 2
        else:
            times = 0
            x_cloud1 = -1000
            x_cloud2 = -1000

        screen.blit(map_game, (0, 0))

        profile(130, 630, 110, 30, 70, brown, "PLAYER 1", player_1)
        profile(1150, 120, 110, 30, 70, brown, "PLAYER 2", player_2)

        # rolling
        if is_rolling:
            screen.blit(dice_rolling_images[rolling_img_cnt], (200, 200))
            rolling_img_cnt += 1
            if rolling_img_cnt >= len(dice_rolling_images):
                rolling_img_cnt = 0
                is_rolling = False
                dice_num_image = dice_images[random.randint(0, 5)]
        else:
            screen.blit(dice_num_image, (200, 200))

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not is_rolling:
            is_rolling = True
            rolling_img_cnt = 0

        pygame.display.update()
        pygame.time.delay(50)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
