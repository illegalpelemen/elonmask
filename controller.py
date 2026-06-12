import pygame

import model

my_event = pygame.USEREVENT
pygame.time.set_timer(my_event, 2000)

my_event1 = pygame.USEREVENT + 1
pygame.time.set_timer(my_event1, 20)
def contr():
    a = pygame.event.get()

    for f in a:
        if f.type == pygame.QUIT:
            exit()
        if f.type == my_event1:
            model.elon()
        if f.type == my_event:
            model.coin()
        if f.type == pygame.MOUSEBUTTONDOWN and model.click(f.pos):
            pygame.time.set_timer(my_event, 2000)
