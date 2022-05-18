from pygame import *
from random import randint

#окно
win_width = 700
win_height = 500
main_win = display.set_mode((win_width, win_height))
display.set_caption("Шутер")

lost = 0
max_lost = 3
score = 0
max_score = 10

bullets = sprite.Group()


class GameSprite(sprite.Sprite):
    def __init__(self, picture, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(picture), (65,65))
        self.speed = speed
        self.height = height
        self.width = width
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        global bullets
        bullet = Bullet('knife', self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.y = -self.height
            self.x = randint(0,win_width-self.width)
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
