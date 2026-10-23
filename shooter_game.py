#Создай собственный Шутер!
from pygame import *

init()
##the players and sprites
im_ball = 'ball.jpg'
im_players = 'stick.jpg'


# the parents class for the other little sprites... 
class GameSprite(sprite.Sprite):
  # class contruct 
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite) :
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

player_left = Player(im_players, 30, 200, 30, 100, 10)
player_right = Player(im_players, 640, 200, 30, 100, 10)



game = True 
clock = time.Clock() 

window = display.set_mode((700,500))
display.set_caption('Ping pong')
backround_colour =(60,50,0)
window.fill(backround_colour)





while game: 
    for e in event.get(): 
        if e.type == QUIT: 
            game = False 
    window.fill(backround_colour)

    player_left.update_left()
    player_left.reset()
    player_right.update_right()
    player_right.reset()

    display.update()
    clock.tick(60)



quit()

