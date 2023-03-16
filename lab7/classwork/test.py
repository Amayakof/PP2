<<<<<<< HEAD
import pygame, sys
from datetime import datetime
import math


def main():

    # pygame initialization
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    # get the current time
    curr_time = datetime.now()
    curr_sec = curr_time.second
    curr_min = curr_time.minute


    # loading the images 
    clock_image = pygame.transform.scale(pygame.image.load('./images/mickeyclock.jpeg'), (800, 600))
    sechand_image = pygame.image.load('./images/sechand.png')
    sechand_image = pygame.transform.scale(sechand_image, (250, 75))
    sechand_rect = sechand_image.get_rect()
    sechand_rect.center = (400, 300)
    minhand_image = pygame.image.load('./images/minhand.png')
    minhand_image = pygame.transform.scale(minhand_image, (200, 50))
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
        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
=======
import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

def blitRotate(surf, image, pos, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)
  
    
def blitRotate2(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
    pygame.draw.rect(surf, (255, 0, 0), new_rect, 2)

try:
    image = pygame.image.load('AirPlaneFront.png')
except:
    text = pygame.font.SysFont('Times New Roman', 50).render('image', False, (255, 255, 0))
    image = pygame.Surface((text.get_width()+1, text.get_height()+1))
    pygame.draw.rect(image, (0, 0, 255), (1, 1, *text.get_size()))
    image.blit(text, (1, 1))
w, h = image.get_size()

angle = 0
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pos = (screen.get_width()/2, screen.get_height()/2)
    
    screen.fill(0)
    blitRotate(screen, image, pos, (w/2, h/2), angle)
    #blitRotate2(screen, image, pos, angle)
    angle += 1
    

    pygame.display.flip()
    
pygame.quit()
exit()
>>>>>>> 7bca860 (git pull)
