import pygame, random

rect_coin = pygame.Rect(500, 50, 50, 50)
rect_elon = pygame.Rect(100,200,256,144)
total_coins = 0
y = - 10
x = 2
def mod():
    pass
def elon():
    global y,x

    if rect_elon.left >= 1000:
        rect_elon.right = 0

    if rect_elon.bottom >= 500:
        y = -10
    if rect_elon.top <= 0:
        y = 10


    rect_elon.move_ip(x,y)

def coin():
    rect_coin.left = random.randint(500, 900)
    rect_coin.top = random.randint(1, 450)

def click(mouse_pos):
    global total_coins
    collide_coin = rect_coin.collidepoint(mouse_pos[0],mouse_pos[1])
    if collide_coin:
        total_coins += 1
        coin()
    return collide_coin