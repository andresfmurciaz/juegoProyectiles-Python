#importamos pygame
import pygame, sys
#para especificar que es lo que necesitamos en especifico y no se traiga toda la libreria
from pygame.locals import *
#metodo de inicializacion
pygame.init()

#constante pantalla lleva la funcion para crear nuestra pantalla de juego

PANTALLA = pygame.display.set_mode((1000,600))


#carga la img de fondo en nuestro juego y la muestra
fondo = pygame.image.load("img/fondo2.png")
PANTALLA.blit(fondo,(0,0))


#carga la icono en nuestro juego y la muestra y title
#le ponemos el tamaño a la venta y un title
pygame.display.set_caption('juegoProyectiles-Parcial 1.')
icono= pygame.image.load("img/icono.png")
pygame.display.set_icon(icono)


#CODIGO DE COLOR
BLANCO =(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)

#poner fondo de pantalla
#PANTALLA.fill(BLANCO)

#CREA UN RECTANGULO CON POSI Y TAMAÑO- parametros van por posi y despues tamaño
#rectangulo1 = pygame.draw.rect(PANTALLA,ROJO,(100,50,100,50))




#toca crear un bucle para que no se cierre la ventana
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #actualiza evento para que aparezca la pantalla blanca
    pygame.display.update()