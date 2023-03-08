#importamos pygame
import pygame

#CODIGO DE COLOR
BLANCO =(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)

#poner fondo de pantalla
#PANTALLA.fill(BLANCO)
#CREA UN RECTANGULO CON POSI Y TAMAÑO- parametros van por posi y despues tamaño
#rectangulo1 = pygame.draw.rect(PANTALLA,ROJO,(100,50,100,50))

#CLASE DE LA NAVE
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((200,200))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.center= (W // 2, H // 2)

#actualiza cada vez que el bucle de una vuelta
    def update(self):
        self.rect.y += 10
        if self.rect.top > H:
            self.rect.bottom=0

#-------------------------------------------------------------
#metodo de inicializacion
pygame.init()

#constante pantalla lleva la funcion para crear nuestra pantalla de juego
W,H=1000,600
pantalla = pygame.display.set_mode((W,H))
#ACELERAR O DESACELERAR EL JUEGO
FPS =500
RELOJ= pygame.time.Clock()
#title
pygame.display.set_caption('juegoProyectiles-Parcial 1.')

#grupo de sprites , instancion de objetos
sprites = pygame.sprite.Group()
nave= Nave()
sprites.add(nave)


#bucle del juego

ejecutando= True

while ejecutando:

    # LLAMAMOS EL METODO PARA LA ACELERACION DEL FONDO
    RELOJ.tick(FPS)

    #EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #SE TERMINA EL BUCLE
            ejecutando=False


    #ACTUALIZACION DE SPRITES- actuali
    sprites.update()

#LE DA EL FONDO DE PANTALLA
    pantalla.fill(NEGRO)
    sprites.draw(pantalla)
    pygame.display.flip()

#CIERRA LA CLASE
pygame.quit()

