import pygame

import model

my_event = pygame.USEREVENT
pygame.time.set_timer(my_event, 2000)

my_event1 = pygame.USEREVENT + 1
pygame.time.set_timer(my_event1, 20)

speed_event = pygame.USEREVENT + 2
pygame.time.set_timer(speed_event, 200)


def contr():
    a = pygame.event.get()

    for f in a:
        if f.type == pygame.QUIT:
            exit()
        if f.type == my_event1:
            model.elon()
        if f.type == my_event:
            model.coin()
        if f.type == speed_event:
            model.speed_up()

        if f.type == pygame.MOUSEBUTTONDOWN and model.click(f.pos):
            pygame.time.set_timer(my_event, 2000)
        if f.type == pygame.KEYDOWN:
            if f.key == pygame.K_RETURN:
                model.start_game()
