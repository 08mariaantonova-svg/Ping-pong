#Создай собственный Шутер!
from pygame import *
init()
window = display.set_mode((700,500))
display.set_caption('Ping pong')
backround_colour =(0,0,0)
window.fill(backround_colour)

game = True 
clock = time.Clock()


while game: 
    for e in event.get(): 
        if e.type == QUIT: 
            game = False 
    window.fill(backround_colour)
    display.update()
    clock.tick(60)
quit()

