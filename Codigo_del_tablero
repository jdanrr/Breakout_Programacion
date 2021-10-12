import pygame #nos permite importar la libreria de Pygame 

pygame.init()

#tamaños que tendrá la pantalla
eje_x = 400
eje_y = 400

#método para definir el tamaño de la pantalla 
ventana = pygame.display.set_mode ((eje_x, eje_y))

pygame.display.set_caption ("Breaking Meta Space") #nombre de la pantalla

#códigos de colores que utilizaremos

color_fondo = (0,0,0)
nivel1 = (126, 232, 150)
nivel2 = (255, 158, 62)
nivel3 = (255, 62, 62)
  
#numero de bloques que aparecerán

verticales = 5
horizontales = 8



#clase para crear los rectangulos (obstaculos) del juego
class Obstaculos():
    def __init__(self):
        self.x = eje_x // horizontales
        self.y = 50

           
    def crear_obstaculos (self):
      
      self.bloques = []      
      #vamos a guardar los bloques dentro de una lista vacia 
        
      grupo_de_bloques = []
       
      for i in range (horizontales):
        
        bloques = []

        for j in range(verticales):

          #se define la posición en x y en y de los rectangulos para crear cada obstaculo. 

          bloque_x = verticales * self.y
          bloque_y = horizontales * self.x
          
          rect = pygame.Rect ((bloque_x, bloque_y, self.x, self.y))

          #dependiendo de la fila en la que se encuentre el bloque el valor o la reaccion va a ser diferente

          if verticales <= 1:
            valor = 3
          elif verticales <= 3:
            valor = 2
          elif verticales <= 5:
            valor = 1

          #en la primera lista vacia que creamos vamos a almacenar cada tipo de bloque, con los atributos rectangulo (obstaculo) y valor (color)

          grupo_de_bloques = [rect, valor]
          
          #agregar los bloques al grupo de bloques para compilar todos los obstaculos
          bloques.append (grupo_de_bloques)

          print (bloques)
          
      self.bloques.append(grupo_de_bloques)
      

    def dibujar_obstaculos (self):
      color_bloque = (0,0,0)

      for verticales in self.bloques:
        for bloque in verticales:
          #asignarle un color a cada bloque 

          if bloque [1] == 3:
            color_bloque = nivel3

          elif bloque [1] == 2:
            color_bloque = nivel2
              
          elif bloque [1] == 1:
            color_bloque = nivel1
                      
          pygame.draw.rect(ventana, color_bloque, self.bloques [0])
                  
          pygame.draw.rect(ventana, color_fondo , (bloque [0]))


tablero = Obstaculos ()
tablero.crear_obstaculos()


while True:
    ventana.fill(color_fondo)
    
    tablero.dibujar_obstaculos()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        break

    pygame.display.update() 
    
pygame.quit()
