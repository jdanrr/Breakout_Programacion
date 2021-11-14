import pygame #nos permite importar la libreria de Pygame 
from pygame.locals import *
from pygame import mixer #Importamos el modulo para reproduccion musical en pygame


class Boton(): #clase donde se encuentra el boton inicial
	def __init__(self, x, y, image, scale):
		ancho = image.get_width()
		alto = image.get_height()
		self.image = pygame.transform.scale(image, (int(ancho * scale), int(alto * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def dibujar(self, superficie):
		action = False
		#posicionamiento del mouse
		pos = pygame.mouse.get_pos()

		#Registrar movimientos de mouse
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#Dibujar el boton en la entrada
		superficie.blit(self.image, (self.rect.x, self.rect.y))

		return action
#tamaño de la pantalla y color 
eje_x = 800
eje_y = 800
screen = pygame.display.set_mode((eje_x, eje_y))
screen.fill((0, 0, 0))

pygame.display.set_caption('BREAKING META SPACE')#nombre de la ventana

breaking_img = pygame.image.load('breaking.png').convert()#se carga la imagen con el nombre del juego
player_x = 120
player_y = 150

screen.blit(breaking_img, (player_x, player_y)) #se ejecuta la imagen

#Cargar imagen del boton, configurar tamaño y programar su funcionamiento
start_img = pygame.image.load('start_btn.png').convert_alpha()
start_boton = Boton(450, 500, start_img, 0.2)
run = True
while run:

	if start_boton.dibujar(screen):
		run = False
	

   
	
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			break

	pygame.display.update()

pygame.quit()

pygame.init() #función para iniciar el juego
#tamaños que tendrá la pantalla 
eje_x = 800
eje_y = 800
#método para definir el tamaño de la pantalla
ventana = pygame.display.set_mode((eje_x, eje_y))
pygame.display.set_caption('Breaking Meta Space') #nombre de la pantalla
#mensajes para el usuario 
fin_del_juego = pygame.font.Font(None, 60)
texto = fin_del_juego.render("FIN DEL JUEGO",0,(236, 112, 99))
ganador = fin_del_juego.render("FELICIDADES, GANASTE", 0, (165, 105, 189))
#colores que vamos a usar durante el juego
color_fondo = (0,0,0)
nivel1 = (39, 174, 96)
nivel2 = (243, 156, 18)
nivel3 = (231, 76, 60)
color_barra = (171, 235, 198)
color_s = (46, 204, 113)
#división de la pantalla de juego (bloques)
columnas = 6
filas = 5
#tiempo que tarda la pelota en moverse
tiempo = pygame.time.Clock()
tiempo_fps = 50

#Música del juego y duración del audio
mixer.music.load('Audio.ogg')
mixer.music.play(-1)


#clase en donde se encuentran todos los obstaculos
class Obstaculos():
  def __init__(self):
    self.x = eje_x // columnas
    self.y = 55

  def crear_obstaculos(self):
    self.bloques = [] 
    #lista sobre el objeto para guardar todos los obstaculos 
    for fila in range(filas):
      linea_bloques = [] #se guardan las filas de los bloques 

      #se define la posición en x y en y de los rectangulos para crear cada obstaculo. 
      for columna in range(columnas):
        #se crea cada bloque con las cordenadas en x e y, y su posición dentro del tablero
        cada_bloque = [] 
        bloques_x = columna * self.x
        bloques_y = fila * self.y
        rect = pygame.Rect(bloques_x, bloques_y, self.x, self.y) 
        #se le asigna un valor a cada nivel del juego

        if fila <= 1:
          valor = 3
        elif fila <= 3:
          valor = 2
        elif fila <= 5:
          valor = 1
        #se guarda cada bloque dentro de la lista, y luego se acumulan en filas
        cada_bloque = [rect, valor]
        linea_bloques.append(cada_bloque)
      #finalmente todas las filas quedan guardadas en la lista asignada al objeto
      self.bloques.append(linea_bloques)

#funcion para dibujar obstaculos
  def dibujar_obstaculos(self):
    #con los valores que definimos anteriormente se dibujarán los obstaculos
    #dependiendo de el valor del bloque va a ser un color (nivel) diferente
    for fila in self.bloques:
      for bloque in fila:
        if bloque [1] == 3:
          nivel_bloque = nivel3
        elif bloque[1] == 2:
          nivel_bloque = nivel2
        elif bloque[1] == 1:
          nivel_bloque = nivel1
        
        pygame.draw.rect(ventana, nivel_bloque , bloque [0]) #funcion para dibujar los obstaculos
        pygame.draw.rect(ventana, color_fondo, (bloque [0]), 2) #funcion para realizar los bordes de los obstaculos
        
#clase de la barra
class Barra():
  def __init__(self):
    #propiedades de un rectangulo, la posición, dirección y la velocidad en que se moverá la barra
    self.alto = 20
    self.ancho = 134
    self.x = 333
    self.y = 550
    self.velocidad = 10
    self.rect = Rect(self.x, self.y, self.ancho, self.alto) #se crea el atributo del rectangulo
    self.direction = 0

  def movimiento(self):
    #con el módulo "paygame.key" se le asigna una funcion a la tecla derecha y izquierda del teclado
    self.direccion = 0
    clave = pygame.key.get_pressed()
    if clave[pygame.K_LEFT] and self.rect.left > 0: #condición para que no se salga de la pantalla por la izquierda
      self.x -= 10
      self.rect.x -= self.velocidad #se corre de la posición inicial 
      self.dibujar_barra() #y se dibuja nuevamente
      self.direccion = -1
    if clave[pygame.K_RIGHT] and self.rect.right < eje_x: #condición para que no se salga de la pantalla por la derecha
      self.x += 10
      self.rect.x += self.velocidad #se corre de la posición inicial
      self.dibujar_barra() #vuelve a dibujar la barra luego que se mueve
      self.direction = 1

  def dibujar_barra(self):
    #funciones para dibujar la barra y su sombra de 3 pixeles de ancho
    pygame.draw.rect(ventana, color_barra, self.rect)
    pygame.draw.rect(ventana, color_s, self.rect, 3)

#clase de la pelota
class Pelota: 
  def __init__ (self):
    #atributos de la pelota y velocidad con la que se va a mover alrededor del tablero
    self.radio = 15
    self.x = 400
    self.y = 550
    self.velocidad_x = 4
    self.velocidad_y = -4
  
  def dibujar (self):
    pygame.draw.circle(ventana, color_s, (self.x , self.y - self.radio), self.radio)
    #funcion para dibujar la pelota

#se le asigna el nombre "tablero" a la clase Obstaculos
tablero = Obstaculos()
#se crean los obstaculos
tablero.crear_obstaculos()
#se le asigna el nombre "barra" a la clase Barra
barra = Barra()
#se le asigna el nombre "pelota" a la clase Pelota
pelota = Pelota ()

run = True
while run:
  
  #tiempo que tarda en moverse la pelota medido en fps
  tiempo.tick(tiempo_fps)
  #rellenar el tablero del color del fondo
  ventana.fill(color_fondo)
  #dibujar los obstaculos
  tablero.dibujar_obstaculos()
  #dibujar la barra
  barra.dibujar_barra()
  #hacer que la barra se mueva con el modulo movimiento
  barra.movimiento()
  #dibujar la pelota
  pelota.dibujar()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  #esto hace que la pelota se mueva constantemente
  pelota.x += pelota.velocidad_x
  pelota.y += pelota.velocidad_y
  
  #si la pelota toca algun lado del tablero, entonces rebota
  if pelota.x + pelota.radio > eje_x:
    pelota.velocidad_x = -4
  
  if pelota.y - pelota.radio < 0:
    pelota.velocidad_y = 4
 
  if pelota.x - pelota.radio < 0:
    pelota.velocidad_x = 4
  
  if pelota.y - pelota.radio >= 570:
    ventana.blit(texto, (250,400)) #si se sale inferiormente, el juego y la música terminan
    mixer.music.set_volume(0)

  #si la pelota toca la barra, entonces rebota
  if (pelota.y - pelota.radio >= 547 and pelota.y - pelota.radio <= 553) and pelota.x > barra.x -5 and pelota.x < barra.x + barra.ancho + 5:
    pelota.velocidad_y = -4

#para cada bloque en el tablero
  for fila in tablero.bloques:
    if len(fila) > 0: #si existen bloques, entonces:
    
      for bloque in fila:
        #para cada bloque
        if fila.index(bloque) == len(fila) -1:
          if pelota.y >= bloque[0].y - 3 + bloque[0].height and pelota.y <= bloque[0].y + 3 + bloque[0].height:
            if pelota.x <= bloque[0].x + bloque[0].width + 5 and pelota.x >= bloque[0].x:
              pelota.velocidad_y = 4
              bloque[1] -= 1
            if bloque[1] == 0:
              fila.remove(bloque)
            break
        else:
          #si el centro de la pelota es mayor que el alto del bloque 
          if pelota.y >= bloque[0].y - 3 + bloque[0].height and pelota.y <= bloque[0].y + 3 + bloque[0].height:
            #entonces cuando la pelota toca el bloque entonces rebota y se desaparece el boque o cambia de color, depende del valor
            if pelota.x <= bloque[0].x + bloque[0].width + 2 and pelota.x >= bloque[0].x:
              pelota.velocidad_y = 4
              bloque[1] -= 1
              if bloque[1] == 0:
                fila.remove(bloque)
              break
        #si el centro de la pelota - el radio es mayor que el ancho del bloque 
        if pelota.x - pelota.radio >= bloque[0].x + bloque[0].width -5 and pelota.x - pelota.radio <= bloque[0].x + bloque[0].width + 5:
          #entonces cuando la pelota toca el bloque entonces rebota y se desaparece el boque o cambia de color, depende del valor
          if pelota.y  > bloque[0].y - 3  and pelota.y  < bloque[0].y + bloque[0].height:
            pelota.velocidad_x = 4
            bloque[1] -= 1
            if bloque[1] == 0:
              fila.remove(bloque)
            break
        #si el centro de la pelota más el radio es mayor que el ancho del bloque 
        if pelota.x + pelota.radio >= bloque[0].x -3 and pelota.x + pelota.radio <= bloque[0].x + 3:
          #entonces cuando la pelota toca el bloque entonces rebota y se desaparece el boque o cambia de color, depende del valor
          if pelota.y  > bloque[0].y - 3  and pelota.y  < bloque[0].y + bloque[0].height:
            pelota.velocidad_x = -4
            bloque[1] -= 1
            fila.remove(bloque)
            break
    else:
      tablero.bloques.remove(fila)
#si ya no quedan bloques para eliminar, entonces fun del juego y la pelota se pausa
  if len (tablero.bloques) == 0:
    ventana.blit(ganador, (110,400))
    pelota.velocidad_y = 0
    pelota.velocidad_x = 0
 
  pygame.display.update()

pygame.quit()
