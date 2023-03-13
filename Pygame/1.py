import pygame

pygame.init()

monitor = pygame.display.set_mode((800, 400))

check = True
while check:
    pygame.display.update()
    for action in pygame.event.get():
                                   if action.type == pygame.QUIT:
                                           check = False
                                           pygame.quit()


