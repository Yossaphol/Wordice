"""selecting game mode"""
import pygame
from player_profile import profile
import random
from turn_player import turn_player

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

    p1_pos = [(825, 400), (903, 347), (982, 316), (1051, 283), (1123, 251), (1188, 205), (1126, 164),
          (1050, 132), (977, 102), (910, 135), (845, 170), (785, 210), (720, 180),
          (660, 150), (580, 180), (520, 220), (447, 269), (519, 301), (430, 350),
          (340, 380), (270, 355), (210, 315), (135, 285), (65, 255), (12, 225),
          (53, 193), (125, 160), (184, 133), (268, 170), (325, 150), (394, 115),
          (460, 75), (515, 60), (560, 40), (602, 16), (663, 1)]

    p2_pos = [(860, 420), (913, 391), (966, 351), (1065, 316), (1136, 285), (1160, 240), (1100, 200),
          (1020, 165), (960, 135), (900, 165), (830, 200), (770, 235), (710, 200),
          (650, 175), (565, 210), (500, 260), (430, 295), (494, 333), (405, 380),
          (330, 415), (260, 379), (195, 346), (123, 310), (60, 280), (5, 240),
          (60, 210), (115, 180), (191, 160), (285, 200), (335, 170), (400, 140),
          (472, 100), (533, 70), (580, 50), (625, 30), (663, 1)]

    # cloud
    cloud1 = pygame.image.load("images/cloud1.png")
    cloud2 = pygame.image.load("images/cloud2.png")
    cloud3 = pygame.image.load("images/cloud3.png")
    cloud4 = pygame.image.load("images/cloud4.png")

    # map
    map_game = pygame.image.load("images/game_map_2.png")
    map_game = pygame.transform.scale(map_game, (1290, 730))

    # background
    background = pygame.image.load("images/background_game.jpg")
    background = pygame.transform.scale(background, (1280, 720))

    # player
    player_1 = pygame.image.load("images/player_1.png")
    player_2 = pygame.image.load("images/player_2.png")
    player_1 = pygame.transform.scale(player_1, (230, 230))
    player_2 = pygame.transform.scale(player_2, (230, 230))

    duck_1 = pygame.image.load("images/player_1.png")
    duck_2 = pygame.image.load("images/player_2_flip.png")
    duck_1 = pygame.transform.scale(duck_1, (100, 100))
    duck_2 = pygame.transform.scale(duck_2, (100, 100))

    # cloud position
    x_cloud1 = 0
    x_cloud2 = 0

    times = 0

    clock = pygame.time.Clock()
    fps = 30

    # dice rolling
    dice_images = [pygame.image.load(f"images/dice/{num}.png") for num in range(1, 7)]
    dice_rolling_images = [pygame.image.load(f"images/dice/{num}.png") for num in range(1, 7)]
    turn = "first time"

    rand_num = 0
    is_rolling = False
    rolling_img_cnt = 0
    dice_num_image = dice_images[0]
    pos_1 = 0
    pos_2 = 0
    first = True

    while running:

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


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # rolling
        if is_rolling:
            screen.blit(dice_rolling_images[rolling_img_cnt], (250, 270))
            rolling_img_cnt += 1
            if rolling_img_cnt >= len(dice_rolling_images):
                rolling_img_cnt = 0
                is_rolling = False
                rand_num = random.randint(0, 5)
                dice_num_image = dice_images[rand_num]


        else:
            screen.blit(dice_num_image, (250, 270))


        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not is_rolling:
            is_rolling = True
            rolling_img_cnt = 0
            first = False


        # turn switch
        if turn == "player1":
            turn_player(60, 640)
        elif turn == "player2":
            turn_player(1090, 130)
        else:
            pass

        if key[pygame.K_w]:
            if first:
                turn = "player1"

            else:
                if turn == "player1":
                    turn = "player2"
                    pos_1 += rand_num + 1
                else:
                    turn = "player1"
                    pos_2 += rand_num + 1

        screen.blit(duck_1, p1_pos[pos_1])
        screen.blit(duck_2, (p2_pos[pos_2]))



        pygame.time.delay(100)
        pygame.display.update()

        clock.tick(fps)

    pygame.quit()
