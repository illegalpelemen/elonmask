import model,pygame


pygame.init()
screen = pygame.display.set_mode([1000,500])

coin_drawing = pygame.image.load("sprites/bitcoin.png")
elon_drawing = pygame.image.load("sprites/elon_mask.jpg")
fon_drawing = pygame.image.load("sprites/fon_menu.jpg")
defeat_drawing = pygame.image.load("sprites/img.png")
coin = pygame.transform.scale(coin_drawing,[50,50])
elon = pygame.transform.scale(elon_drawing,model.rect_elon.size)
fon = pygame.transform.scale(fon_drawing,[1000,500])
defeat = pygame.transform.scale(defeat_drawing,[100,250])
comsans = pygame.font.SysFont("comicsansms",30)
text_intro = comsans.render("Нажмите enter чтобы начать игру",True,[255,255,255])


def vew():
    screen.fill([12,12,12])
    # pygame.draw.rect(screen,[25,25,225],model.rect_coin,2)
    if model.mode == "intro":
        screen.blit(fon, [0,0])

        screen.blit(text_intro,[500,350])
    if model.mode == "game":
        pygame.draw.rect(screen,[25,25,225],model.rect_elon,2)
        text = comsans.render(f"монет:{model.total_coins}",True, [255,255,255])
        screen.blit(coin,model.rect_coin)
        screen.blit(elon,model.rect_elon)
        for a in range(len(model.list_dot)-1):

            pygame.draw.circle(screen,[150,255,150],[1000/(len(model.list_dot) - 1) * a ,model.list_dot[a]],2)
            pygame.draw.line(screen,[55,255,55],[1000/(len(model.list_dot) -1) * a ,model.list_dot[a]],[1000/(len(model.list_dot)-1) * (a+1),model.list_dot[a+1]],3)
        screen.blit(text,[20,20])
    if model.mode == "game_over":
        screen.blit(defeat,[100,250])
        text_local_record = comsans.render(str(model.local_record),True,[255,255,255])
        screen.blit(text_local_record,[500,350])
    pygame.display.flip()