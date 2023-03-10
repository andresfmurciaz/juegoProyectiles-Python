#importamos pygame
import pygame
import random

#CODIGO DE COLOR
BLANCO =(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
#fuentes
consolas= pygame.font.match_font('consolas')
times = pygame.font.match_font('times')
arial= pygame.font.match_font('arial')


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
        self.radius = 30
      #  pygame.draw.circle(self.image,ROJO,self.rect.center,self.radius)



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

class Meteoritos(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.img_aleatoria = random.randrange(3)
        if self.img_aleatoria ==0:
            self.image = pygame.transform.scale(pygame.image.load("img/balaroja.png").convert(),(100,100))
            self.radius=50
        if self.img_aleatoria == 1:
            self.image = pygame.transform.scale(pygame.image.load("img/balaroja.png").convert(), (50, 50))
            self.radius = 25
        if self.img_aleatoria == 2:
            self.image = pygame.transform.scale(pygame.image.load("img/balaroja.png").convert(), (25, 25))
            self.radius = 12

        self.rect = self.image.get_rect()
        self.rect.x= random.randrange(W -self.rect.width)
        self.rect.y= -self.rect.width
        #ancho
        self.velocidad_y = random.randrange(1,10)

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.top > H:
            self.rect.x = random.randrange(W -self.rect.width)
            self.rect.y = -self.rect.width

            self.velocidad_y= random.randrange(1,10)



class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("img/enemigo1.png").convert()
        self.rect = self.image.get_rect()

        self.radius = 30
        #.draw.circle(self.image, ROJO, self.rect.center, self.radius)

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




class Enemigo2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("img/enemigo1.png").convert()
        self.rect = self.image.get_rect()

        self.radius = 30
        #.draw.circle(self.image, ROJO, self.rect.center, self.radius)

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





class Enemigo3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("img/enemigo1.png").convert()
        self.rect = self.image.get_rect()

        self.radius = 30
        #.draw.circle(self.image, ROJO, self.rect.center, self.radius)

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




class Enemigo4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("img/enemigo1.png").convert()
        self.rect = self.image.get_rect()

        self.radius = 30
        #.draw.circle(self.image, ROJO, self.rect.center, self.radius)

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




class Enemigo5(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("img/enemigo1.png").convert()
        self.rect = self.image.get_rect()

        self.radius = 30
        #.draw.circle(self.image, ROJO, self.rect.center, self.radius)

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
#sistemas de puntuacion
puntuacion=0000000
def muestra_texto(pantalla,fuente,texto,color,dimensiones,x,y):
     tipo_letra = pygame.font.Font(fuente,dimensiones)
     superficie = tipo_letra.render(texto,True, color)
     rectangulo = superficie.get_rect()
     rectangulo.center = (x,y)
     pantalla.blit(superficie,rectangulo)





#ACELERAR O DESACELERAR EL JUEGO
FPS =20
RELOJ= pygame.time.Clock()
#title
pygame.display.set_caption('juegoProyectiles-Parcial 1.')

#grupo de sprites , instancion de objetos
sprites = pygame.sprite.Group()
enemigos_1 = pygame.sprite.Group()
enemigos_2 = pygame.sprite.Group()
enemigos_3 = pygame.sprite.Group()
enemigos_4 = pygame.sprite.Group()
enemigos_5 = pygame.sprite.Group()

balas =pygame.sprite.Group()
meteoritos = pygame.sprite.Group()



nave = Nave()
sprites.add(nave)

for x in range(10):
    meteorito = Meteoritos()
    meteoritos.add(meteorito)






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
    enemigos_1.update()
    enemigos_2.update()
    enemigos_3.update()
    enemigos_4.update()

    balas.update()
    meteoritos.update()

    #colisiona a nave y imagen de fuego
  #  colision_nave= pygame.sprite.spritecollide(nave,enemigos,False,pygame.sprite.collide_circle)
   # colision = pygame.sprite.groupcollide(enemigos,balas,False,True)
    colision_meteoritos= pygame.sprite.spritecollide(nave,meteoritos,False,pygame.sprite.collide_circle)



    colision_disparos_1 = pygame.sprite.groupcollide(enemigos_1, balas, True, True,
                                                             pygame.sprite.collide_circle)

    colision_disparos_2 = pygame.sprite.groupcollide(enemigos_2, balas, True, True,
                                                          pygame.sprite.collide_circle)

    colision_disparos_3= pygame.sprite.groupcollide(enemigos_3, balas, True, True,
                                                          pygame.sprite.collide_circle)

    colision_disparos_4 = pygame.sprite.groupcollide(enemigos_4, balas, True, True,
                                                         pygame.sprite.collide_circle)

    if colision_disparos_1:
        puntuacion += 10

    if colision_disparos_2:
        puntuacion += 25

    if colision_disparos_3:
        puntuacion += 50

    if colision_disparos_4:
        puntuacion += 100


    if not enemigos_1 and not enemigos_2 and not enemigos_3 and not enemigos_4:
        # instancia de enenmigos
        enemigo = Enemigo()
        enemigos_1.add(enemigo)

        enemigo2 = Enemigo2()
        enemigos_2.add(enemigo2)

        enemigo3 = Enemigo3()
        enemigos_3.add(enemigo3)

        enemigo4 = Enemigo4()
        enemigos_4.add(enemigo4)


   # if colision_nave:
    #   enemigo.image = pygame.image.load("img/navep.jpg")
     #  enemigo.velocidad_y += 20
   # elif enemigo.rect.top > W :
        #elimina objetos
    #    enemigo.kill()

    if colision_meteoritos:
        print('hola')





#LE DA EL FONDO DE PANTALLA
    pantalla.fill(NEGRO)
    sprites.draw(pantalla)
    enemigos_1.draw(pantalla)
    enemigos_2.draw(pantalla)
    enemigos_3.draw(pantalla)
    enemigos_4.draw(pantalla)
   # enemigos_5.draw(pantalla)
    meteoritos.draw(pantalla)
    balas.draw(pantalla)


    muestra_texto(pantalla,consolas,str(puntuacion),ROJO,40,700,50)
#actualiza el contenido de pantalla
    pygame.display.flip()


#CIERRA LA CLASE
pygame.quit()

