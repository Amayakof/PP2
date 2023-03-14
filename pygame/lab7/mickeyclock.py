#Create a simple clock application (only with minutes and seconds) which is synchronized with system clock. Use Mickey's right hand as minutes arrow and left - as seconds.
import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("mickeyclock_ioiiiomio")
pygame.display.set_icon(pygame.image.load(""))

check = True
while check :
    pygame.display.update()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()


#For moving Mickey's hands you can use: pygame.transform.rotate more explanation: https://stackoverflow.com/a/54714144


