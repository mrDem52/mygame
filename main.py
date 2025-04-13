import random
from typing import List

from pygame import Surface, SurfaceType

from menu import Button
import pygame
import sys

# Параметры экрана
WIDTH, HEIGHT = 600, 550

pygame.init()  # инициация игры
screen_nemu = pygame.display.set_mode((WIDTH, HEIGHT))  # выбор размера экрана

pygame.display.set_caption('Бегущий ниндзя')  # название игры (подпись окна)
icon = pygame.image.load('images/icons/icon-ninja.png')  # ссылка на загрузку иконки
pygame.display.set_icon(icon)

main_bg = pygame.image.load('images/background/menu/title.png')
lose_bg = pygame.image.load('images/background/lose/lose.jpg')


def main_menu():
    first_button = Button(WIDTH / 2 - (252 / 2), 100, 252, 74, 'Играть',
                          'images/icons/button/btn-1.png', 'images/icons/button/btn-2.png',
                          'sound/effects/click_button/click.mp3')
    second_button = Button(WIDTH / 2 - (252 / 2), 200, 252, 74, 'Настройки',
                           'images/icons/button/btn-1.png', 'images/icons/button/btn-2.png',
                           'sound/effects/click_button/click.mp3')
    third_button = Button(WIDTH / 2 - (252 / 2), 300, 252, 74, 'Выход',
                          'images/icons/button/btn-1.png', 'images/icons/button/btn-2.png',
                          'sound/effects/click_button/click.mp3')
    running_menu = True

    while running_menu:
        screen_nemu.fill((0, 0, 0))
        screen_nemu.blit(main_bg, (-250, -200))

        font = pygame.font.Font(None, 72)
        text_surface = font.render('Бегущий ниндзя', True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(300, 50))
        screen_nemu.blit(text_surface, text_rect)

        for event_menu in pygame.event.get():
            if event_menu.type == pygame.QUIT:
                running_menu = False
                pygame.quit()
                sys.exit()
            if event_menu.type == pygame.USEREVENT and event_menu.button == first_button:
                running_menu = False

            if event_menu.type == pygame.USEREVENT and event_menu.button == second_button:
                settings_menu()

            if event_menu.type == pygame.USEREVENT and event_menu.button == third_button:
                pygame.quit()
                sys.exit()

            for btn in [first_button, second_button, third_button]:
                btn.handle_event(event_menu)

        for btn in [first_button, second_button, third_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw_btn(screen_nemu)

        pygame.display.flip()


def settings_menu():
    fourth_button = Button(WIDTH / 2 - (252 / 2), 100, 252, 74, 'Звук',
                           'images/icons/button/btn-1.png', 'images/icons/button/btn-2.png',
                           'sound/effects/click_button/click.mp3')
    fifth_button = Button(WIDTH / 2 - (252 / 2), 200, 252, 74, 'Урпавление',
                          'images/icons/button/btn-1.png', 'images/icons/button/btn-2.png',
                          'sound/effects/click_button/click.mp3')
    sixth_button = Button(WIDTH / 2 - (252 / 2), 300, 252, 74, 'Назад',
                          'images/icons/button/btn-1.png', 'images/icons/button/btn-2.png',
                          'sound/effects/click_button/click.mp3')

    running_menu = True
    while running_menu:

        screen_nemu.fill((0, 0, 0))
        screen_nemu.blit(main_bg, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render('Настройки', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(300, 50))
        screen_nemu.blit(text_surface, text_rect)

        for event_menu in pygame.event.get():
            if event_menu.type == pygame.QUIT:
                running_menu = False
                pygame.quit()
                sys.exit()
            if event_menu.type == pygame.USEREVENT and event_menu.button == sixth_button:
                running_menu = False
            if event_menu.type == pygame.USEREVENT and event_menu.button == fifth_button:
                controls_menu()
            if event_menu.type == pygame.USEREVENT and event_menu.button == fourth_button:
                print('h1')

            for btn in [fourth_button, fifth_button, sixth_button]:
                btn.handle_event(event_menu)

        for btn in [fourth_button, fifth_button, sixth_button]:
            btn.set_position(WIDTH / 2 - (252 / 2))
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw_btn(screen_nemu)
        pygame.display.flip()


def controls_menu():
    global WIDTH, HEIGHT, screen_nemu

    back_arrow_key = Button(150, 200, 72, 66, '',
                            'images/icons/control/back.png', '',
                            '')
    forward_arrow_key = Button(250, 200, 72, 66, '',
                               'images/icons/control/front.png', '',
                               '')

    attack_key = Button(350, 200, 103, 66, '',
                        'images/icons/control/ctrl.png', '',
                        '')
    jump_key = Button(150, 300, 300, 66, '',
                      'images/icons/control/space.png', '',
                      '')
    back_button = Button(WIDTH / 2 - (252 / 2), 450, 252, 74, 'Назад',
                         'images/icons/button/btn-1.png', 'images/icons/button/btn-2.png',
                         'sound/effects/click_button/click.mp3')

    running_settings_control = True

    while running_settings_control:
        screen_nemu.fill((0, 0, 0))
        screen_nemu.blit(main_bg, (0, -200))

        font = pygame.font.Font(None, 72)
        text_surface = font.render('Управление', True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(300, 50))
        screen_nemu.blit(text_surface, text_rect)

        for event_menu in pygame.event.get():
            if event_menu.type == pygame.QUIT:
                running_settings_control = False
                pygame.quit()
                sys.exit()

            if event_menu.type == pygame.USEREVENT and event_menu.button == back_button:
                running_settings_control = False

            back_button.handle_event(event_menu)

        back_button.check_hover(pygame.mouse.get_pos())
        back_button.draw_btn(screen_nemu)
        forward_arrow_key.draw_btn(screen_nemu)
        back_arrow_key.draw_btn(screen_nemu)
        attack_key.draw_btn(screen_nemu)
        jump_key.draw_btn(screen_nemu)
        pygame.display.flip()


def lose_menu():
    screen_lose = pygame.display.set_mode((1024, 800))
    try_again_button = Button(575, 180, 270, 74, 'Еще раз!',
                              'images/icons/button/btn-1.png', 'images/icons/button/btn-2.png',
                              'sound/effects/click_button/click.mp3')
    running_lose = True

    while running_lose:
        screen_lose.fill((255, 0, 0))
        screen_lose.blit(lose_bg, (0, 0))

        font = pygame.font.Font(None, 122)
        text_surface = font.render('Ты проиграл', True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(700, 100))
        screen_lose.blit(text_surface, text_rect)
        keys = pygame.key.get_pressed()

        for event_lose in pygame.event.get():
            if event_lose.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running_lose = False
                pygame.quit()
                sys.exit()
            if event_lose.type == pygame.USEREVENT and event_lose.button == try_again_button:
                game_start()
            try_again_button.handle_event(event_lose)

        try_again_button.check_hover(pygame.mouse.get_pos())
        try_again_button.draw_btn(screen_lose)
        pygame.display.flip()


def game_start():
    global keys
    clock = pygame.time.Clock()  # переменная для регулировки времени смены кадров

    pygame.init()  # инициация игры
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)  # выбор размера экрана
    pygame.display.set_caption('Бегущий ниндзя')  # название игры (подпись окна)
    icons = pygame.image.load('images/icons/icon-ninja.png')  # ссылка на загрузку иконки
    pygame.display.set_icon(icons)  # установка иконки на приложение

    bg = pygame.image.load('images/background/background_1.png')  # загрузка заднего фона

    run_right: list[Surface | SurfaceType] = [
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
    ]  # загрузка пошаговой анимации спрайта персонажа движущегося в право

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
    ]  # загрузка пошаговой анимации спрайта персонажа движущегося в лево

    play_animation_count = 0  # счетчик анимации

    bg_x = 0
    bg_sound = pygame.mixer.Sound('sound/bg/ForestWalk-bg.mp3')
    bg_sound.play()

    player_speed = 40  # скорость перемещения игрока
    player_x = 150  # координата по Х игрока
    player_y = 600  # координата по Y игрока
    jump = True
    jump_counter = - 14

    enemy_girl = pygame.image.load('images/enemy-1/enemy-girl-3.png')

    enemy_girl_game = []

    enemy_timer = pygame.USEREVENT + 1  # создаем событие для врага
    pygame.time.set_timer(enemy_timer, 6500)


    on_game = True  # игра запущена

    label = pygame.font.Font('fonts/VariableFont.ttf', 150)

    shuriken = pygame.image.load('images/weapon/shuriken.png').convert_alpha()
    shurikens = []
    shuriken_rec_collision = shuriken.get_rect()
    shuriken_col = 5
    shuriken_sound = pygame.mixer.Sound('sound/effects/throw a shuriken/throw.mp3')
    shuriken_climbing = pygame.mixer.Sound('sound/effects/climbing/climbing.mp3')
    shuriken_up = pygame.mixer.Sound('sound/effects/up_sh/shur_up.mp3')
    pos_sh_x = 600
    pos_sh_y = 300
    dead_enemy = 0
    font = pygame.font.Font(None, 72)

    running = True  # переключатель цикла
    while running:  # основной цикл игры
        text_surface = font.render(str(dead_enemy), True, (0, 0, 0))

        screen.blit(bg, (bg_x, 0))  # вывод заднего фона на экран
        screen.blit(bg, (bg_x + 1920, 0))  # вывод заднего фона на экран (для анимации)
        screen.blit(text_surface, (1800, 100))
        if on_game:
            player_rec_collision = run_right[0].get_rect(topleft=(player_x, player_y))  # рамка столкновения

            if enemy_girl_game:
                for (id, enemy) in enumerate(enemy_girl_game):  # перебор по объектам и нумерации
                    screen.blit(enemy_girl, enemy)
                    enemy.x -= 10

                    if enemy.x < - 50:  # проверка врага за экраном

                        enemy_girl_game.pop(id)  # удаление врага из списка

                    if player_rec_collision.colliderect(enemy):
                        on_game = False

            keys = pygame.key.get_pressed()  # какая клавиша нажата (список)

            if keys[pygame.K_LEFT]:
                screen.blit(run_left[play_animation_count], (player_x, player_y))  # вывод персонажа на экран
            else:
                screen.blit(run_right[play_animation_count], (player_x, player_y))  # вывод персонажа на экран

            # условия в лево для перемещения игрока и ограничение по перемещению
            if keys[pygame.K_LEFT] and player_x > 50:
                player_x -= player_speed
                # условия в право для перемещения игрока и ограничение по перемещению
            elif keys[pygame.K_RIGHT] and player_x < 1500:
                player_x += player_speed

            if not jump:
                if keys[pygame.K_SPACE]:
                    jump = True  # флаг прыжка
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

            if play_animation_count == 9:  # условия перебора спрайтов игрока
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
                                dead_enemy += 1

            shuriken_col_collision = shuriken.get_rect(topleft=(pos_sh_x, pos_sh_y))
            if shuriken_col == 0:
                screen.blit(shuriken, (pos_sh_x, pos_sh_y))
                pos_sh_x -= 20
                if shuriken_col_collision.colliderect(player_rec_collision):
                    shuriken_col = 5
                    shuriken_up.play()
                    pos_sh_x = random.randrange(1300, 1900, 200)
                    pos_sh_y = random.randrange(300, 800, 50)



        # условие проигрыша

        else:
            bg_sound.stop()
            on_game = False
            running = False
            lose_menu()

        pygame.display.update()  # обновить экран (постоянно из-за цикла)

        clock.tick(20)  # FPS

        for event in pygame.event.get():  # перебрать список событий
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:  # если нажат крестит или esc
                running = False  # остановить основной цикл
                pygame.quit()  # выходим из приложения
            if on_game and event.type == pygame.KEYUP and event.key == pygame.K_LCTRL and shuriken_col > 0:
                shurikens.append(shuriken.get_rect(topleft=(player_x + 100, player_y + 100)))
                shuriken_col -= 1
                shuriken_sound.play()

            if event.type == enemy_timer:
                enemy_girl_game.append(enemy_girl.get_rect(topleft=(random.randrange(1800, 2000, 100),
                                                                    random.randrange(200, 600, 50))))


main_menu()
game_start()
