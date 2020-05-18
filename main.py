import pygame
import random
import os
from Maps.Map01 import Map01

def retorna_tile_random(lista):
	escolheu = False
	while escolheu == False:
		tale_inicial = random.choice(lista)
		if tale_inicial.e_comeco == True:
			return tale_inicial.path_image
m = Map01()

pygame.init()

window = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Window")

#escolhendo tail inicial

# print(tale_inicial.nome)
tile_inicial = retorna_tile_random(m.tiles)
gameLoop = True
while gameLoop:
    aux = pygame.image.load("{}/{}".format(os.getcwd(), tile_inicial))
    window.blit(aux, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
    pygame.display.flip()

pygame.quit()
