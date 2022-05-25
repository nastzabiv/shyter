from curses import KEY_ENTER
from pygame import *
from random import randint
import notmain as cl



#спрайты

def main():
    global lost

    bg = transform.scale(image.load('bg.jpeg'), (cl.win_width, cl.win_height))
    player = cl.Player('chmon.png', cl.win_width/2-25, cl.win_height-105, 50, 100, 5)
    piclose = transform.scale(image.load('crazydog.jpg'), (250,250))
    picwin = transform.scale(image.load('angrycat.jpg'), (250,250))
    anger = transform.scale(image.load('anger.png'), (50,50))
    happy = transform.scale(image.load('happy1.png'), (50,50))


    #группа врагов
    enemies = sprite.Group()
    for i in range(3):
        enemy = cl.Enemy("enemies.png", randint(0, cl.win_width-80), -50, 80, 50, randint(1,3))
        enemies.add(enemy)

    #UI
    font.init()
    font_UI = font.SysFont("Times New Roman ", 35)

    FPS = 60
    clock = time.Clock()
    finish = False
    run = True
    while run:
        keys = key.get_pressed()
        for e in event.get():
            if e.type == QUIT or keys[K_ESCAPE]:
                run = False
            if e.type == K_KP_ENTER:
                run = True
            if e.type == KEYUP:
                init()

            elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    #fire_sound.play()
                    player.fire()

        if cl.lost > 3:
            finish = True
            
        if not finish:
            cl.main_win.blit(bg, (0,0))

            
            player.update()
            player.reset()

            enemies.update()
            enemies.draw(cl.main_win)
            
            cl.bullets.update()
            cl.bullets.draw(cl.main_win)

            text = font_UI.render("Счёт: " + str(cl.score), True, (0,0,0))
            cl.main_win.blit(text, (10, 20))
            text = font_UI.render("Пропущено: " + str(cl.lost), True, (0,0,0))
            cl.main_win.blit(text, (10, 50))


            #проверка соударения пули и врагов
            collides = sprite.groupcollide(enemies, cl.bullets, True, True)
            for c in collides:
                cl.score += 1
                enemy = cl.Enemy("enemies.png", randint(0, cl.win_width-80), -50, 80, 50, randint(1,3))
                enemies.add(enemy)

            #проверка проигрыша
            if sprite.spritecollide(player, enemies, False) or cl.lost >= cl.max_lost:
                finish = True
                text = font_UI.render("You lose", True, (200,0,0))
                cl.main_win.blit(text, (350, 250))
                text = font_UI.render("press enter for restart", True, (0,0,0))
                cl.main_win.blit(text, (250, 560))
                cl.main_win.blit(piclose, (300,300))
                cl.main_win.blit(anger, (475,245))
                #вывод на экран надписи

            #проверка выигрыша
            if cl.score >= cl.max_score:
                finish = True
                text = font_UI.render("You win", True, (0,102,0))
                cl.main_win.blit(text, (350, 250))
                text = font_UI.render("press enter for restart", True, (0,0,0))
                cl.main_win.blit(text, (250, 560))
                cl.main_win.blit(picwin, (300,300))
                cl.main_win.blit(happy, (475,245))
                #вывод на экран надписи


            display.update()
            clock.tick(FPS)

if __name__ == '__main__':
    main()