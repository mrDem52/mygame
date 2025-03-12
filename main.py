import random

import pygame

clock = pygame.time.Clock() # переменная для регулировки времени смены кадров

pygame.init()                                               # инициация игры
screen = pygame.display.set_mode((1920, 1080))               # выбор размера экрана
pygame.display.set_caption('Бегущий ниндзя')                # название игры (подпись окна)
icon = pygame.image.load('images/icons/icon-ninja.png')     # ссылка на загрузку иконки
pygame.display.set_icon(icon)                               # установка иконки на приложение


bg = pygame.image.load('images/background/background_1.png') # загрузка заднего фона

run_right = [
    pygame.image.load('images/player-right/1.png'),
    pygame.image.load('images/player-right/2.png'),
    pygame.image.load('images/player-right/3.png'),
    pygame.image.load('images/player-right/4.png'),
    pygame.image.load('images/player-right/5.png'),
    pygame.image.load('images/player-right/6.png'),
    pygame.image.load('images/player-right/7.png'),
    pygame.image.load('images/player-right/8.png'),
    pygame.image.load('images/player-right/9.png'),
    pygame.image.load('images/player-right/10.png')
] # загрузка пошаговой анимации спрайта персонажа движущегося в право

run_left = [
    pygame.image.load('images/player-left/1.png'),
    pygame.image.load('images/player-left/2.png'),
    pygame.image.load('images/player-left/3.png'),
    pygame.image.load('images/player-left/4.png'),
    pygame.image.load('images/player-left/5.png'),
    pygame.image.load('images/player-left/6.png'),
    pygame.image.load('images/player-left/7.png'),
    pygame.image.load('images/player-left/8.png'),
    pygame.image.load('images/player-left/9.png'),
    pygame.image.load('images/player-left/10.png')
] # загрузка пошаговой анимации спрайта персонажа движущегося в лево

jump_up = [
    pygame.image.load('images/player-jump/1.png'),
    pygame.image.load('images/player-jump/2.png'),
    pygame.image.load('images/player-jump/3.png'),
    pygame.image.load('images/player-jump/4.png'),
]  # загрузка прыжка анимации спрайта персонажа

play_animation_count = 0                                    # счетчик анимации


bg_x = 0
bg_sound = pygame.mixer.Sound('sound/bg/ForestWalk-bg.mp3')
bg_sound.play()

player_speed = 40 # скорость перемещения игрока
player_x = 150 # координата по Х игрока
player_y = 600 # координата по Y игрока
jump = True
jump_counter = - 13

enemy_girl = [
    pygame.image.load('images/enemy-1/enemy-girl-1.png'),
    pygame.image.load('images/enemy-1/enemy-girl-2.png'),
    pygame.image.load('images/enemy-1/enemy-girl-3.png')
] # анимация врага - 1
enemy_girl_game = []
enemy_girl_x = random.randrange(1200, 1800, 200)
enemy_girl_y = random.randrange(500, 800, 100)
play_animation_enemy_girl = 0
enemy_timer = pygame.USEREVENT + 1 # создаем событие для врага
pygame.time.set_timer(enemy_timer, 1000)


running = True                                              # переключатель цикла
while running:                                              # основной цикл игры

    screen.blit(bg, (bg_x, 0))                            # вывод заднего фона на экран
    screen.blit(bg, (bg_x + 1920, 0))                     # вывод заднего фона на экран (для анимации)
    screen.blit(enemy_girl[play_animation_enemy_girl],(enemy_girl_x, enemy_girl_y))

    if play_animation_enemy_girl != 2: play_animation_enemy_girl += 1

    player_rec_collision = run_right[0].get_rect(topleft=(player_x, player_y)) # рамка столкновения
    enemy_girl_rec_collision = enemy_girl[1].get_rect(topleft=(enemy_girl_x, enemy_girl_y)) # рамка столкновения

    if player_rec_collision.colliderect(enemy_girl_rec_collision): # проверка столкновения
        print('Boom!')



    keys = pygame.key.get_pressed()  # какая клавиша нажата

    if keys[pygame.K_LEFT]:
        screen.blit(run_left[play_animation_count], (player_x, player_y)) # вывод персонажа на экран
    else:
        screen.blit(run_right[play_animation_count], (player_x, player_y))  # вывод персонажа на экран



    if keys[pygame.K_LEFT] and player_x > 50: # условия в лево для перемещения игрока и ограничение по перемещению
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 1500: # условия в право для перемещения игрока и ограничение по перемещению
        player_x += player_speed

    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True # флаг прыжка
    else:
        if jump_counter >= - 13:
            if jump_counter > 0:
                player_y -= (jump_counter ** 2) / 2
            else:
                player_y += (jump_counter ** 2) / 2
            jump_counter -= 1
        else:
            jump = False
            jump_counter = 13

    if play_animation_count == 9:                           # условия перебора спрайтов игрока
        play_animation_count = 0
    else:
        play_animation_count += 1

    bg_x -= 10
    if bg_x == -1920:
        bg_x = 0

    enemy_girl_x -= 40 * 1.5
    pygame.display.update()                                 # обновить экран (постоянно из-за цикла)

    clock.tick(12)  # FPS

    for event in pygame.event.get():                        # перебрать список событий
        if event.type == pygame.QUIT:                       # если нажат крестит
            running = False                                 # остановить основной цикл
            pygame.quit()                                   # выходим из приложения



