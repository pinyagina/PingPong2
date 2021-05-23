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
        self.speed_y = player_speed
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
        global score1
        global score2
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if self.rect.y<1 or self.rect.y>549:
            self.speed_y*=-1
        if sprite.collide_rect(ball, raket1) or sprite.collide_rect(ball, raket2):
            self.speed_x*=-1
        if self.rect.x<1:
            score1+=1
            self.rect.x=600
            self.rect.y=300
        if self.rect.x>1199:
            score2+=1
            self.rect.x=600
            self.rect.y=300

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
raket_image = 'rocket.jpg'
ballll = 'ball.png'
score1 = 0
score2 = 0
#создание спрайтов

raket1 = Player1(raket_image, 15, 150, 10, 250, 5)
raket2 = Player2(raket_image, 15, 150, 1175, 250, 5)
ball = Ball(ballll, 50, 50, 575, 275, 7)

#музыка

'''mixer.init()
mixer.music.load('ooo.ogg')


mixer.music.play()
shot = mixer.Sound('Krovostok.ogg')

pong = mixer.Sound(pong_sound)'''
#шрифты

font.init()
text_score1 = font.SysFont('Arial', 70).render('YOU WIN', 1, (0,255,0))
text_score2 = font.SysFont('Arial', 70).render('GAME OVER', 1, (255,0,0))


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill(bg)
    if not(finish):
        window.fill(bg)
        raket1.update()
        raket2.update()
        ball.update()
        text_score1 = font.SysFont('Arial', 70).render(str(score1), 1, (255,255,255))
        text_score2 = font.SysFont('Arial', 70).render(str(score2), 1, (255,255,255))
        window.blit(text_score1, (100, 100))
        window.blit(text_score2, (900, 100))
        if score1 == 10:
            text_score1 = font.SysFont('Arial', 70).render('WIN', 1, (255,255,255))
            text_score2 = font.SysFont('Arial', 70).render('LOSE', 1, (255,255,255))
            window.blit(text_score1, (100, 570))
            window.blit(text_score2, (900, 100))
            finish = True
        if score2 == 10:
            text_score1 = font.SysFont('Arial', 70).render('LOSE', 1, (255,255,255))
            text_score2 = font.SysFont('Arial', 70).render('WIN', 1, (255,255,255))
            window.blit(text_score1, (100, 100))
            window.blit(text_score2, (900, 100))
            finish = True
        raket1.reset()
        raket2.reset()
        ball.reset()
    display.update()
    clock.tick(60) 