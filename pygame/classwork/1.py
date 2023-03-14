import pygame

pygame.init()

monitor = pygame.display.set_mode((500, 500))
pygame.display.set_caption("IoIIIomio_1") #the title
pygame.display.set_icon(pygame.image.load("/Users/amayakof/Desktop/PP2/pygame/game_files/icon/clock.png")) #icon

check = True
font = pygame.font.Font('/Users/amayakof/Desktop/PP2/pygame/game_files/fonts/bebas_neue.ttf', 20)
text = font.render('IoIIIomio', False, 'Black') #Text parameters
image = pygame.image.load("/Users/amayakof/Desktop/PP2/pygame/game_files/images/bg.jpeg")#background
bg = pygame.image.load("/Users/amayakof/Desktop/PP2/pygame/game_files/icon/clock.png")
sound = pygame.mixer.Sound('/Users/amayakof/Desktop/PP2/pygame/game_files/sound/musica.mp3')
sound.play()

while check:
    monitor.fill((253, 201, 207))#bg color

    pygame.draw.circle(monitor, 'white',(250, 250), 100)#use function to add shapes

    monitor.blit(text, (300, 100)) #установка текста
    monitor.blit(image,(200, 200))
    monitor.blit(bg,(200,200))
    # To close the program
    pygame.display.update()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()