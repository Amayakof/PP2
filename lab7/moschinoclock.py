#Create a simple clock application (only with minutes and seconds) which is synchronized with system clock. Use Mickey's right hand as minutes arrow and left - as seconds.
import pygame, sys
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("moschinoclock") #the title
pygame.display.set_icon(pygame.image.load('/Users/amayakof/Desktop/PP2/lab7/pygame/game_files/icon/icon.jpg'))

# get the current time
clock = pygame.time.Clock()
curr_time = datetime.now()
curr_sec = curr_time.second
curr_min = curr_time.minute

# get the imgs
clock_main = pygame.image.load("/Users/amayakof/Desktop/PP2/lab7/pygame/game_files/images/f_base.png")
clock_hours = pygame.image.load("/Users/amayakof/Desktop/PP2/lab7/pygame/game_files/images/f_hours.png")
clock_hours_rect = clock_hours.get_rect()
clock_hours_rect.center = (300, 300)

clock_minutes = pygame.image.load("/Users/amayakof/Desktop/PP2/lab7/pygame/game_files/images/f_mins.png")
clock_minutes_rect = clock_minutes.get_rect()
clock_minutes_rect.center = (300, 300)

clock_seconds = pygame.image.load("/Users/amayakof/Desktop/PP2/lab7/pygame/game_files/images/sec.png")
clock_seconds_rect = clock_minutes.get_rect()
clock_seconds_rect.center = (300, 300)

check = True

while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()

    #bg color
    screen.fill('White')
    screen.blit(clock_main, (0, 0))

    screen.blit(clock_hours,(0, 0))
    rot_hours = pygame.transform.rotate(clock_hours, -1 * (6 * curr_min) - 160)
    rot_hours_rect = rot_hours.get_rect()
    rot_hours_rect.center = clock_hours_rect.center
    screen.blit(rot_hours, rot_hours_rect)

    pygame.display.update()
