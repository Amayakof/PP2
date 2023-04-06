
import pygame, sys
from datetime import datetime
import math


def main():

    # pygame initialization
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("moschinoclock") #the title
    clock = pygame.time.Clock()
    pygame.display.set_icon(pygame.image.load('/Users/amayakof/Desktop/PP2/lab7/clock/images/icon.jpg'))

    # get the current time
    curr_time = datetime.now()
    curr_sec = curr_time.second
    curr_min = curr_time.minute


    # loading the images 
    clock_image = pygame.image.load('/Users/amayakof/Desktop/PP2/lab7/clock/images/moschinoclock.png')
    sechand_image = pygame.image.load('/Users/amayakof/Desktop/PP2/lab7/clock/images/1.png')

    sechand_rect = sechand_image.get_rect()
    sechand_rect.center = (400, 300)
    minhand_image = pygame.image.load('/Users/amayakof/Desktop/PP2/lab7/clock/images/2.png')
    minhand_rect = minhand_image.get_rect()
    minhand_rect.center = (400, 300)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
        screen.fill(0)
        screen.blit(clock_image, (0, 0))
    
        rot_minhand = pygame.transform.rotate(minhand_image, -1 * (6 * curr_min) - 160)
        rot_minhand_rect = rot_minhand.get_rect()
        rot_minhand_rect.center = minhand_rect.center
        screen.blit(rot_minhand, rot_minhand_rect)
    
        rot_sechand = pygame.transform.rotate(sechand_image, -1 * (6 * curr_sec) + 90)
        rot_sechand_rect =rot_sechand.get_rect()
        rot_sechand_rect.center = sechand_rect.center
        screen.blit(rot_sechand, rot_sechand_rect)

        curr_time = datetime.now()
        curr_sec = curr_time.second
        curr_min = curr_time.minute
        
        pygame.display.update()
        clock.tick(360)


if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
