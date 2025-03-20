import random
from weapon import Weapon
from menu import Button
import pygame
import sys

# Параметры экрана
WIDTH, HEIGHT = 600, 550

pygame.init()                                               # инициация игры
screen_nemu = pygame.display.set_mode((WIDTH, HEIGHT))               # выбор размера экрана
pygame.display.set_caption('Бегущий ниндзя')                # название игры (подпись окна)
icon = pygame.image.load('images/icons/icon-ninja.png')     # ссылка на загрузку иконки
pygame.display.set_icon(icon)

first_button = Button(WIDTH/2-(252/2), 100, 252, 74, 'Button', 'images/icons/button/btn-1.png')

def main_menu():
    running_menu = True
    while running_menu:
        screen_nemu.fill((0, 0, 0))



        for event_menu in pygame.event.get():
            if event_menu.type == pygame.QUIT:
                running_menu = False
                pygame.quit()
                sys.exit()
        first_button.check_hover(pygame.mouse.get_pos())
        first_button.draw_btn(screen_nemu)
        pygame.display.flip()

main_menu()




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
jump_counter = - 14

enemy_girl = pygame.image.load('images/enemy-1/enemy-girl-3.png')

enemy_girl_game = []



enemy_timer = pygame.USEREVENT + 1 # создаем событие для врага
pygame.time.set_timer(enemy_timer, 6500)

on_game = True # игра запущена

label = pygame.font.Font('fonts/VariableFont.ttf', 150)
lose_label = label.render('YOU LOSE!', False, (193, 196, 199))
restart_label = label.render('TRY AGAIN!', False, (15, 96, 109))
restart_label_rec = restart_label.get_rect(topleft=(1920/1/3, 1080/2))

shuriken = pygame.image.load('images/weapon/shuriken.png').convert_alpha()
shurikens = []
shuriken_rec_collision = shuriken.get_rect()
shuriken_col = 5
shuriken_sound = pygame.mixer.Sound('sound/effects/throw a shuriken/throw.mp3')
shuriken_climbing = pygame.mixer.Sound('sound/effects/climbing/climbing.mp3')

running = True                                              # переключатель цикла
while running:                                              # основной цикл игры

    screen.blit(bg, (bg_x, 0))                            # вывод заднего фона на экран
    screen.blit(bg, (bg_x + 1920, 0))                     # вывод заднего фона на экран (для анимации)

    if on_game:
        player_rec_collision = run_right[0].get_rect(topleft=(player_x, player_y)) # рамка столкновения

        if enemy_girl_game:
            for (id, enemy) in enumerate(enemy_girl_game): # перебор по объектам и нумерации
                screen.blit(enemy_girl, enemy)
                enemy.x -= 10

                if enemy.x < - 50: # проверка врага за экраном

                    enemy_girl_game.pop(id) # удаление врага из списка

                if player_rec_collision.colliderect(enemy):
                    on_game = False






        keys = pygame.key.get_pressed()  # какая клавиша нажата (список)

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
            if jump_counter >= - 14:
                if jump_counter > 0:
                    player_y -= (jump_counter ** 2) / 2
                else:
                    player_y += (jump_counter ** 2) / 2
                jump_counter -= 1
            else:
                jump = False
                jump_counter = 14

        if play_animation_count == 9:                           # условия перебора спрайтов игрока
            play_animation_count = 0
        else:
            play_animation_count += 1

        bg_x -= 10
        if bg_x == -1920:
            bg_x = 0



        if shurikens:
            for (i, elem) in enumerate(shurikens):
                screen.blit(shuriken, (elem.x, elem.y))
                elem.x += 80

                if elem.x > 1920:
                    shurikens.pop(i)

                if enemy_girl_game:
                    for (index, enemy_el) in enumerate(enemy_girl_game):
                        if elem.colliderect(enemy_el):
                            shuriken_climbing.play()
                            enemy_girl_game.pop(index)
                            shurikens.pop(i)
                        


    else:
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (1920/1/3, 1080/1/3))
        screen.blit(restart_label, restart_label_rec)
        bg_sound.stop()
        where_mouse = pygame.mouse.get_pos()
        if restart_label_rec.collidepoint(where_mouse) and pygame.mouse.get_pressed()[0]:
            on_game = True
            enemy_girl_game.clear()
            bg_sound.play()
            shurikens.clear()
            shuriken_col = 5



    pygame.display.update()                                 # обновить экран (постоянно из-за цикла)

    clock.tick(20)  # FPS


    for event in pygame.event.get():                        # перебрать список событий
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: # если нажат крестит или esc
            running = False                                 # остановить основной цикл
            pygame.quit()                                   # выходим из приложения
        if on_game and event.type == pygame.KEYUP and event.key == pygame.K_LCTRL and shuriken_col > 0:
            shurikens.append(shuriken.get_rect(topleft=(player_x + 100, player_y + 100)))
            shuriken_col -= 1
            shuriken_sound.play()

        if event.type == enemy_timer:
            enemy_girl_game.append(enemy_girl.get_rect(topleft=(random.randrange(1800, 2000, 100),
                                                                random.randrange(200, 600, 50))))



