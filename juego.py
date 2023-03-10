#importamos pygame
import pygame
import random

#CODIGO DE COLOR
BLANCO =(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)

#poner fondo de pantalla
#PANTALLA.fill(BLANCO)
#CREA UN RECTANGULO CON POSI Y TAMAÑO- parametros van por posi y despues tamaño
#rectangulo1 = pygame.draw.rect(PANTALLA,ROJO,(100,50,100,50))
#constante pantalla lleva la funcion para crear nuestra pantalla de juego
W,H=1000,600
# #CLASE DE LA NAVE
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load("img/navep.jpg").convert(), (100, 100))

        # self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.center= (500,500)
        #velocidad de la nave inicial
        self.velocidad_x=0
        # velocidad de la nave inicial
        self.velocidad_y = 0






#actualiza cada vez que el bucle de una vuelta
    def update(self):
#velocidad predeterminada
        self.velocidad_x=0
        self.velocidad_y = 0
        #para que las teclas esten pulsadas
        teclas=pygame.key.get_pressed()
        #izquierda
        if teclas[pygame.K_a]:
            self.velocidad_x=-20
        #derecha
        if teclas[pygame.K_d]:
            self.velocidad_x=20
        # arriba
        if teclas[pygame.K_w]:
            self.velocidad_y = -20
        # abajo
        if teclas[pygame.K_s]:
            self.velocidad_y = 20

        # abajo
        if teclas[pygame.K_SPACE]:
            nave.disparo()
          #  nave.disparo2()

      #actualiza la posi del personaje
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

#hace una margen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > W:
            self.rect.right = W

        if self.rect.bottom > H:
            self.rect.bottom = H

        if self.rect.top < 0:
            self.rect.top = 0


    def disparo(self):
        bala = Disparos(self.rect.centerx,self.rect.top + 30)
        balas.add(bala)


    def disparo2(self):
        bala = Disparos(self.rect.centerx + 20, self.rect.top + 40)
        balas.add(bala)


class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("img/enemigo1.png").convert()
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x=random.randrange(W - self.rect.width)
        self.rect.y=random.randrange(H - self.rect.height)
        # velocidad de la nave inicial

        self.velocidad_x = random.randrange(1, 10)
        self.velocidad_y = random.randrange(1, 10)

    def update(self):
        # actualiza la posi del personaje
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocidad_x += 1

        # Limita el margen derecho
        if self.rect.right > W:
            self.velocidad_x -= 1

        # Limita el margen inferior
        if self.rect.bottom > H:
            self.velocidad_y -= 1

        # Limita el margen superior
        if self.rect.top < 0:
            self.velocidad_y += 1


class Disparos (pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image= pygame.transform.scale(pygame.image.load("img/balaroja.png").convert(),(10,20))

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        self.rect.y -= 25
        if self.rect.bottom < 0:
            self.kill()


#-------------------------------------------------------------
#metodo de inicializacion
pygame.init()


pantalla = pygame.display.set_mode((W,H))
#ACELERAR O DESACELERAR EL JUEGO
FPS =20
RELOJ= pygame.time.Clock()
#title
pygame.display.set_caption('juegoProyectiles-Parcial 1.')

#grupo de sprites , instancion de objetos
sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
balas =pygame.sprite.Group()




nave = Nave()
sprites.add(nave)

enemigo = Enemigo()
enemigos.add(enemigo)


#nos da enemigos aleatoriamente
#for x in range(random.randrange(5)+1):

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
    enemigos.update()
    balas.update()

#colisiona a nave y imagen de fuego
    colision= pygame.sprite.spritecollide(nave,enemigos,False)
    if colision:
       enemigo.image = pygame.image.load("img/navep.jpg")
       enemigo.velocidad_y += 20
    elif enemigo.rect.top > W :
        #elimina objetos
        enemigo.kill()

#LE DA EL FONDO DE PANTALLA
    pantalla.fill(NEGRO)
    sprites.draw(pantalla)
    enemigos.draw(pantalla)

    balas.draw(pantalla)

#actualiza el contenido de pantalla
    pygame.display.flip()

#CIERRA LA CLASE
pygame.quit()

