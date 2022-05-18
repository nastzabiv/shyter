from pygame import *
from random import randint
import notmain as cl





#спрайты

def main():
    global lost

    bg = transform.scale(image.load('cat.png'), (cl.win_width, cl.win_height))
    player = cl.Player('cmohya.png', cl.win_width/2-25, cl.win_height-105, 50, 100, 10)
    
    #группа врагов
    enemies = sprite.Group()
    for i in range(5):
        enemy = cl.Enemy("yuit", randint(0, cl.win_width-80), -50, 80, 50, randint(1,5))
        enemies.add(enemy)

    #UI
    font.init()
    font_UI = font.SysFont("Arial ", 36)

    finish = False
    run = True
    while run:
        keys = key.get_pressed()
        for e in event.get():
            if e.type == QUIT or keys[K_ESCAPE]:
                run = False

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

            text = font_UI.render("Счёт: " + str(cl.score), True, (255,255,255))
            cl.main_win.blit(text, (10, 20))
            text = font_UI.render("Пропущено: " + str(cl.lost), True, (255,255,255))
            cl.main_win.blit(text, (10, 50))


            #проверка соударения пули и врагов
            collides = sprite.groupcollide(enemies, cl.bullets, True, True)
            for c in collides:
                cl.score += 1
                enemy = cl.Enemy("", randint(0, cl.win_width-80), -50, 80, 50, randint(1,5))
                enemies.add(enemy)

            #проверка проигрыша
            if sprite.spritecollide(player, enemies, False) or cl.lost >= cl.max_lost:
                finish = True
                text = font_UI.render("ТЫ ЛОСЬ хахаха лох ", True, (255,255,255))
                cl.main_win.blit(text, (100, 100))
                #вывод на экран надписи

            #проверка выигрыша
            if cl.score >= cl.max_score:
                finish = True
                text = font_UI.render("ура ", True, (255,255,255))
                cl.main_win.blit(text, (100, 100))
                #вывод на экран надписи


            display.update()
            time.delay(5)

if __name__ == '__main__':
    main()