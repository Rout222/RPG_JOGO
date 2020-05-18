import pygame
import random

class Tail:
    def __init__(self, nome, largura, altura, num_portas, e_comeco):
        self.nome = nome;
        self.largura = largura;
        self.altura = altura;
        self.num_portas = num_portas;
        self.e_comeco = e_comeco;

#Tails casa
lobby = Tail("Lobby", 2, 2, 6, True)
cozinha = Tail("Cozinha", 2, 2, 3, False)
corredor = Tail("Corredor", 2, 1, 5, True)

dispensa = Tail("Dispensa", 2, 1, 1, False)
dispensa_rotacionada = Tail("Dispensa", 1, 2, 1, False)
biblioteca = Tail("Biblioteca", 2, 1, 2, False)
biblioteca_rotacionada = Tail("Biblioteca", 1, 2, 2, False)
igreja = Tail("Igreja", 2, 1, 3, False)
igreja_rotacionada = Tail("Igreja", 1, 2, 3, False)
sala_de_bilhar = Tail("Sala de Bilhar", 2, 1, 1, False)
sala_de_bilhar_rotacionada = Tail("Sala de Bilhar", 1, 2, 1, False)
teatro = Tail("Teatro", 2, 1, 1, False)
teatro_rotacionada = Tail("Teatro", 1, 2, 1, False)


lista_tails = [lobby, teatro, corredor]


pygame.init()

window = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Window")

img_lobby = pygame.image.load("/home/aurelio/Documentos/git/RPG_JOGO/mansion_img/lobby.jpeg")


#escolhendo tail inicial
escolheu = False
while escolheu == False:
    tale_inicial = random.choice(lista_tails)
    if tale_inicial.e_comeco == True:
        escolheu = True


gameLoop = True
while gameLoop:

    window.blit(img_lobby, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
    pygame.display.flip()

pygame.quit()
