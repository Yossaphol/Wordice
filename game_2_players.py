"""selecting game mode"""
import pygame
from player_profile import profile
import random
from turn_player import turn_player
from winner import winner_alert
from new_wordle import *
from vocab import *

def game_2_players():
    """return screen for selecting game mode"""
    from button import text_object

    pygame.display.set_caption("wordice")
    screen = pygame.display.set_mode((1280, 720))
    pygame.mixer.music.load("sounds/sound.mp3")
    pygame.mixer.music.play(-1)

    running = True
    win = False
    a_point = 0
    b_point = 0
    total_a = 0
    total_b = 0
    final_point_a = 0
    final_point_b = 0

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

    # duck
    duck_1 = pygame.image.load("images/player_1.png")
    duck_2 = pygame.image.load("images/player_2_flip.png")
    duck_1 = pygame.transform.scale(duck_1, (100, 100))
    duck_2 = pygame.transform.scale(duck_2, (100, 100))
    duck_1_flip = pygame.image.load("images/player_1_flip.png")
    duck_1_flip = pygame.transform.scale(duck_1_flip, (100, 100))
    duck_2_flip = pygame.transform.scale(player_2, (100, 100))
    backside1 = pygame.image.load("images/backside_duck1.gif")
    backside2 = pygame.image.load("images/backside_duck2.gif")
    backside1 = pygame.transform.scale(backside1, (100, 100))
    backside2 = pygame.transform.scale(backside2, (100, 100))
    backside1_flip = pygame.image.load("images/backside_duck1_flip.gif")
    backside2_flip = pygame.image.load("images/backside_duck2_flip.gif")
    backside1_flip = pygame.transform.scale(backside1_flip, (100, 100))
    backside2_flip = pygame.transform.scale(backside2_flip, (100, 100))

    # cloud position
    x_cloud1 = 0
    x_cloud2 = 0

    times = 0

    clock = pygame.time.Clock()
    fps = 30

    # dice rolling
    dice_images = [pygame.image.load(f"images/dice/{num}.png") for num in range(1, 7)]
    dice_rolling_images = [pygame.image.load(f"images/dice/{num}.png") for num in range(1, 7)]
    turn = "player1"

    rand_num = 0
    is_rolling = False
    rolling_img_cnt = 0
    dice_num_image = dice_images[0]
    pos_1 = 0
    pos_2 = 0
    final_point_a = 0
    final_point_b = 0
    alert = False
    total_turn = 0

    dark_brown = 73, 56, 41
    burly_wood = 222,184,135
    light_steel_blue  = 176,196,222
    silver = 192,192,192
    grey = 128,128,128

    rand_num = 0
    is_rolling = False
    rolling_img_cnt = 0
    dice_num_image = dice_images[0]
    alert = False
    who_win = "player1"
    lose = False

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


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        key = pygame.key.get_pressed()


        # duck's direction
        if pos_1 < 5 or pos_1 >= 25:
            screen.blit(backside1, p1_pos[pos_1])
        elif 9 <= pos_1 < 11 or 13 < pos_1 < 19:
            screen.blit(duck_1_flip, p1_pos[pos_1])
        elif 19 <= pos_1 < 25 or 11 <= pos_1 < 14 or 5 <= pos_1 < 9:
            screen.blit(backside1_flip, p1_pos[pos_1])

        if pos_2 < 5 or pos_2 >= 25:
            screen.blit(backside2, p2_pos[pos_2])
        elif 9 <= pos_2 < 11 or 13 < pos_2 < 19:
            screen.blit(duck_2_flip, (p2_pos[pos_2]))
        elif 19 <= pos_2 < 25 or 11 <= pos_2 < 14 or 5 <= pos_2 < 9:
            screen.blit(backside2_flip, p2_pos[pos_2])


        if not alert:
            describes = pygame.font.Font("fonts/Pixelify.ttf", 50)
            describe = describes.render("Press space bar for next step", True, "RED", white)
            screen.blit(describe, (300, 640))

            pygame.draw.rect(screen, wheat, (330, 30, 550, 60), 0, 0, 40, 40, 40, 40)
            turn_remain = describes.render("TURN REMAINING : ", True, dark_brown)
            remain = describes.render(f"{20 - total_turn}", True, red)
            screen.blit(turn_remain, (350, 30))
            screen.blit(remain, (800, 30))

            if key[pygame.K_SPACE]:
                alert = not alert
                alert = True

        # alert box code
        else:
            if not win:
                turn = who_win
                win, lose, who_win, total_turn, a_point, b_point, final_point_a, final_point_b = wordle(turn, total_turn, total_a, total_b, final_point_a, final_point_b)
                total_a = a_point
                total_b = b_point
            else:
                if win:
                    total_a = a_point
                    total_b = b_point

                    turn = who_win
                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()

                    dice_images = [pygame.image.load(f"images/dice/{num}.png") for num in range(1, 7)]
                    dice_rolling_images = [pygame.image.load(f"images/dice/{num}.png") for num in range(1, 7)]

                    pygame.draw.rect(screen, grey, (243, 113, 803, 503), 0, 0, 20, 20, 20, 20)
                    pygame.draw.rect(screen, burly_wood, (240, 110, 800, 500), 0, 0, 20, 20, 20, 20)


                    sound = pygame.mixer.Sound("sounds/click.MP3")

                    # random button
                    if 600 > mouse[0] > 400 and 540 > mouse[1] > 500:
                        pygame.draw.rect(screen, "BLACK", (403, 503, 200,40), 0, 0, 30 ,30, 30, 30)
                        pygame.draw.rect(screen, silver, (400,500,200,40), 0, 0, 30 ,30, 30, 30)

                        if click[0] == 1:
                            sound.play()
                            is_rolling = True
                            rolling_img_cnt = 0

                    else:
                        pygame.draw.rect(screen, "BLACK", (403, 503, 200,40), 0, 0, 30 ,30, 30, 30)
                        pygame.draw.rect(screen, light_steel_blue, (400,500,200,40), 0, 0, 30 ,30, 30, 30)

                    if is_rolling:
                        screen.blit(dice_rolling_images[rolling_img_cnt], (595, 350))
                        rolling_img_cnt += 1
                        if rolling_img_cnt >= len(dice_rolling_images):
                            rolling_img_cnt = 0
                            is_rolling = False
                            rand_num = random.randint(0, 5)
                            dice_num_image = dice_images[rand_num]

                    else:
                        screen.blit(dice_num_image, (595, 350))

                    smallText = pygame.font.Font("fonts/Pixelify.ttf", 30)
                    text_surface, text_rect = text_object("RANDOM", smallText)
                    text_rect.center = ((500), (520))
                    screen.blit(text_surface, text_rect)

                    # movement button
                    if 880 > mouse[0] > 680 and 540 > mouse[1] > 500:
                        pygame.draw.rect(screen, "BLACK", (683, 503, 200,40), 0, 0, 30 ,30, 30, 30)
                        pygame.draw.rect(screen, silver, (680,500,200,40), 0, 0, 30 ,30, 30, 30)

                        if click[0] == 1:
                            sound.play()
                            alert = False
                            win = False
                            if turn == "player1":
                                turn = "player2"
                                if pos_1 + rand_num + 1 > len(p1_pos) - 1:
                                    pos_1 = 35
                                else:
                                    pos_1 += rand_num + 1
                            else:
                                turn = "player1"
                                if pos_2 + rand_num + 1 > len(p2_pos) - 1:
                                    pos_2 = 35
                                else:
                                    pos_2 += rand_num + 1
                    else:
                        pygame.draw.rect(screen, "BLACK", (683, 503, 200,40), 0, 0, 30 ,30, 30, 30)
                        pygame.draw.rect(screen, light_steel_blue, (680,500,200,40), 0, 0, 30 ,30, 30, 30)

                    smallText = pygame.font.Font("fonts/Pixelify.ttf", 30)
                    text_surface, text_rect = text_object("MOVE", smallText)
                    text_rect.center = ((780), (520))
                    screen.blit(text_surface, text_rect)

        profile(130, 630, total_a, 70, brown, "PLAYER 1", player_1)
        profile(1150, 120, total_b, 70, brown, "PLAYER 2", player_2)

        if turn == "player1":
            turn_player(90, 640)
        else:
            turn_player(1120, 130)

        if pos_1 >= len(p1_pos) - 1 or pos_2 >= len(p2_pos) - 1 or total_turn >= 20:
            if pos_1 + final_point_a > pos_2 + final_point_b:
                winner_alert("PLAYER1", final_point_a + pos_1, final_point_b + pos_2)
            elif pos_1 + final_point_a == pos_2 + final_point_b:
                draw(final_point_a + pos_1, final_point_b + pos_2)
            else:
                winner_alert("PLAYER2", final_point_a + pos_1, final_point_b + pos_2)

        pygame.time.delay(100)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
