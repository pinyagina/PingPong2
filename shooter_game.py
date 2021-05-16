from pygame import *
from random import randint
from time import time as timer
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, w, h, player_x, player_y, player_speed):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.speed_x = player_speed
        self.speed_y = int(player_speed/2)
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.x>0:
            self.rect.y-=self.speed 
        if key_pressed[K_s] and self.rect.x<600:
            self.rect.y+=self.speed 

class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.x>0:
            self.rect.y-=self.speed 
        if key_pressed[K_DOWN] and self.rect.x>600:
            self.rect.y+=self.speed 

class Ball(GameSprite):
    def update(self):
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if self.rect.y<1 or self.rect.y>549:
            self.speed_y*=-1
        if sprite.collide_rect(ball, raket1) or sprite.collide_rect(ball, raket2):
            self.speed_x*=-1
            pong.play()

#Игровая сцена:
bg = (randint(0,255),randint(0,255),randint(0,255))
window = display.set_mode((1200, 600))
display.set_caption("PingPong")
window.fill(bg)

#переменные
fon_music = 'Krovostok.ogg'
pong_sound = 'ооо.ogg'
finish = False
run = True
clock = time.Clock()
raket_image = 'rocket.png'
ball = 'tennis_PNG10393.png'
#создание спрайтов

raket1 = Player1(raket_image, 15, 150, 10, 250, 5)
raket2 = Player2(raket_image, 15, 150, 1175, 250, 5)
ball = Ball(ball, 50, 50, 575, 275, 8)

#музыка
mixer.init()
mixer.music.load(fon_music)
mixer.music.play()
pong = mixer.Sound(pong_sound)
#шрифты
'''font.init()
win = font.SysFont('Arial', 70).render('YOU WIN', 1, (0,255,0))
lose = font.SysFont('Arial', 70).render('GAME OVER', 1, (255,0,0))'''

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not(finish):
        window.fill(bg)
        raket1.update()
        raket1.reset()
        raket2.update()
        raket2.reset()
        ball.update()
        ball.reset()
    display.update()
    clock.tick(60) 