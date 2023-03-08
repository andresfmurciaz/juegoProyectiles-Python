#importamos pygame
import pygame, sys
#para especificar que es lo que necesitamos en especifico y no se traiga toda la libreria
from pygame.locals import *
#metodo de inicializacion
pygame.init()
#constante pantalla lleva la funcion para crear nuestra pantalla de juego
#le ponemos el tamaño a la venta y un title
PANTALLA = pygame.display.set_mode((500,400))
pygame.display.set_caption('juegoProyectiles-Parcial 1.')

#toca crear un bucle para que no se cierre la ventana

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exixt()
