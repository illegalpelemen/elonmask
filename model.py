import pygame, random


def kurs():
    global pixel_x, list_dot
    list_dot.append([pixel_x, pixel_y])
    pixel_x += 30


def mod():
    pass


def elon():
    global y, x
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


def game_over():
    global total_coins, mode
    if total_coins < 0:
        mode = "game_over"


def coin():
    if mode != "game":
        return
    rect_coin.left = random.randint(600, 900)
    rect_coin.top = random.randint(1, 450)


def click(mouse_pos):
    global total_coins, local_record
    if mode != "game":
        return

    collide_coin = rect_coin.collidepoint(mouse_pos[0], mouse_pos[1])
    if not collide_coin:
        return

    total_coins += 1
    coin()
    if total_coins > local_record:
        local_record = total_coins
    return True


def steal():
    global total_coins
    collide_elon = rect_coin.colliderect(rect_elon)
    if collide_elon:
        total_coins -= 1
        coin()
        game_over()


def speed_up():
    global x, y
    if mode != "game":
        return
    choice = random.randint(1, 2)
    if choice == 1:
        x += 1
    else:
        if y < 0:
            y -= 1
        else:
            y += 1


def start_game():
    global mode, total_coins, local_record, x, y
    if mode == "intro":
        mode = "game"
        total_coins = local_record = 0
        x = 2
        y = - 10
        rect_elon.left = 0
        rect_elon.top = 1
    elif mode == "game_over":
        mode = "intro"


mode = "intro"
rect_coin = pygame.Rect(500, 50, 50, 50)
rect_elon = pygame.Rect(100, 200, 256, 144)
total_coins = 0
local_record = 0
pixel_x = 0
pixel_y = 250
list_dot = []
y = - 10
x = 2
for b in range(30):
    kurs()
