#Create a simple clock application (only with minutes and seconds) which is synchronized with system clock. Use Mickey's right hand as minutes arrow and left - as seconds.
import pygame
pygame.init()

screen = pygame.dislay.set_mode((800, 800))

pygame.display.set_caption("moschinoclock") #the title
pygame.display.set_icon(pygame.image.load('/Users/amayakof/Desktop/PP2/pygame/game_files/icon/icon.jpg'))

check = True
bg = pygame.image.load("/Users/amayakof/Desktop/PP2/pygame/game_files/images/base.png")


while check:
    screen.blit(bg)

    for action in pygame.event.get():
        if action.type == pygame.QUIT():
            check = False
            pygame.quit()
