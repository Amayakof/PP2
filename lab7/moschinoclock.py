#Create a simple clock application (only with minutes and seconds) which is synchronized with system clock. Use Mickey's right hand as minutes arrow and left - as seconds.
import pygame, sys
from datetime import datetime
import math

def main():

    # pygame initialization
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    
    # get the current time
    curr_time = datetime.now()
    curr_sec = curr_time.second
    curr_min = curr_time.minute

screen = pygame.display.set_mode((500, 586))

pygame.display.set_caption("moschinoclock") #the title
pygame.display.set_icon(pygame.image.load('/Users/amayakof/Desktop/PP2/lab7/pygame/game_files/icon/icon.jpg'))

check = True
bg = pygame.image.load("/Users/amayakof/Desktop/PP2/lab7/pygame/game_files/images/f_base.png")
hours = pygame.image.load("/Users/amayakof/Desktop/PP2/lab7/pygame/game_files/images/f_hours.png")
minutes = pygame.image.load("/Users/amayakof/Desktop/PP2/lab7/pygame/game_files/images/f_mins.png")
seconds = pygame.image.load("/Users/amayakof/Desktop/PP2/lab7/pygame/game_files/images/sec.png")

angle = 0

while check:
    screen.fill('White')#bg color

    screen.blit(bg, (0, 0))
    screen.blit(hours,(0, 0))
    screen.blit(minutes, (0, 0))
    screen.blit(seconds, (0, 0))


    
    pygame.display.update()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()
