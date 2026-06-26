import pygame, random
mode = "intro"
rect_coin = pygame.Rect(500, 50, 50, 50)
rect_elon = pygame.Rect(100,200,256,144)
total_coins = 0
y = - 10
x = 2
def mod():
    pass
def elon():
    global y,x
    if mode != "game":
        return
    rect_elon.move_ip(x, y)
    if rect_elon.left >= 1000:
        rect_elon.right = 0

    if rect_elon.bottom >= 500:
        rect_elon.bottom = 500
        y = -y

    if rect_elon.top <= 0:
        rect_elon.top = 0
        y = -y




    steal()

def coin():
    if mode != "game":
        return
    rect_coin.left = random.randint(20, 900)
    rect_coin.top = random.randint(1, 450)

def click(mouse_pos):

    global total_coins
    if mode != "game":
        return
    collide_coin = rect_coin.collidepoint(mouse_pos[0],mouse_pos[1])
    if collide_coin:
        total_coins += 1
        coin()
    return collide_coin

def steal():
    global total_coins
    collide_elon = rect_coin.colliderect(rect_elon)
    if collide_elon:
        total_coins -= 1
        coin()

def speed_up():
    global x,y
    if mode != "game":
        return
    choice = random.randint(1,2)
    if choice == 1:
        x += 1
    else:
        if y < 0:
            y -= 1
        else:
            y += 1

def start_game():
    global mode
    if mode == "intro":
        mode = "game"
    elif mode == "game_over":
        mode = "intro"