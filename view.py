import model,pygame


pygame.init()
screen = pygame.display.set_mode([1000,500])
coin_drawing = pygame.image.load("sprites/bitcoin.png")
elon_drawing = pygame.image.load("sprites/elon_mask.jpg")
coin = pygame.transform.scale(coin_drawing,[50,50])
elon = pygame.transform.scale(elon_drawing,model.rect_elon.size)
print(pygame.font.get_fonts())
comsans = pygame.font.SysFont("comicsansms",30)
def vew():
    screen.fill([12,12,12])
    # pygame.draw.rect(screen,[25,25,225],model.rect_coin,2)
    pygame.draw.rect(screen,[25,25,225],model.rect_elon,2)
    text = comsans.render(f"монет:{model.total_coins}",True, [255,255,255])
    screen.blit(coin,model.rect_coin)
    screen.blit(elon,model.rect_elon)
    screen.blit(text,[20,20])

    pygame.display.flip()