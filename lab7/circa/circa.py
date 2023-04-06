#Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. 
#When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key. 
#The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored

import pygame as pg
from sys import exit

screen=pg.display.set_mode((490,390))
pg.display.set_caption("circa")
pg.display.set_icon(pg.image.load('/Users/amayakof/Desktop/PP2/lab7/circa/images/icon.jpeg'))
clock=pg.time.Clock()

bg=pg.Surface((490,390))
bg2=pg.Surface((490,390))
pg.Surface.fill(bg2,(255,255,255))

posx=0
posy=0

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_DOWN:
                if(posy+45<=375):
                    posy+=20
            if event.key==pg.K_UP:
                if(posy-45>=-25):
                    posy-=20
            if event.key==pg.K_RIGHT:
                if(posx+45<=475):
                    posx+=20
            if event.key==pg.K_LEFT:
                if(posx-45>=-25):
                    posx-=20
        

    screen.fill('white')
    pg.draw.circle(screen, (255,0,0), (posx+25, posy+25), 25)
    pg.display.flip()
    clock.tick(60)