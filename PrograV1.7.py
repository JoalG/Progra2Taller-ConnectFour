#Segunda Progra

import pygame
import random
from pygame.locals import *
import sys 
import math


rank = []
partida_ant = []
partida_antPC = []


pygame.mixer.pre_init(44100,16,2,4096)
pygame.font.init()
pygame.init()


Azul = (56,11,228)
Negro = (0,0,0)
Rojo = (255,0,0)
Amarillo = (255,255,0)
VerdeA  = (0,233,202)



jugador = ''
jugador2 = 'System '


#Arte

font = pygame.font.Font('ARCADECLASSIC.TTF',80)
font2 = pygame.font.SysFont('a',40)
font3 = pygame.font.Font('ARCADECLASSIC.TTF',100)
font4 = pygame.font.Font('ARCADECLASSIC.TTF',60)
player1wins = font.render(jugador + '  HA  GANADO',True,Azul)
player2wins = font.render(jugador2 +' HA  GANADO',True,Azul)
pcwins = font.render('EL  SISTEMA  HA  GANADO',True,Azul)
vsPCplay = font.render('1  JUGADOR',True,Azul)
vsPlay = font.render('2  JUGADORES',True,Azul)
rankings = font.render('RANKINGS',True,Azul)
titulo = font3.render('CONNECT FOUR',True,VerdeA)
nombre1 = font.render(jugador,True,Azul)
nombre2 = font.render(jugador2,True,Azul)
NoPermitido = font.render('Debe jugar a maximo 7',True,Negro)
NoPermitido2 = font.render('columnas de una ficha',True,Negro)
Continuar = font.render('CONTINUAR  LA  PARTIDA  ',True,Negro)
Continuar2 = font.render('ANTERIOR',True,Negro)





#Graficos

back = pygame.image.load("back.jpg")
electrico = pygame.image.load("electrico.png")
agua = pygame.image.load("agua.png")
fuego = pygame.image.load("fuego.png")
empty = pygame.image.load("empty.png")
borde = pygame.image.load("borde.png")
marco_izq = pygame.image.load("marco_izq.png")
marco_der = pygame.image.load("marco_der.png")
marco_arriba = pygame.image.load("marco_arriba.png")
flecha_abajo = pygame.image.load("flecha_abajo.png")
flecha_arriba = pygame.image.load("flecha_arriba.png")
flecha_der = pygame.image.load("flecha_der.png")
flecha_izq = pygame.image.load("flecha_izq.png")
FondoGane = pygame.image.load("FondoGane.png")
FondoMenuP = pygame.image.load("FondoMenuP.png")
FondoMenuNombres = pygame.image.load("FondoMenuNombres.png")
FondoRank = pygame.image.load("FondoRank.png")
back_button = pygame.image.load("back_button.png")
save_button = pygame.image.load("save_button.png")
selector_Fondo = pygame.image.load("selector_Fondo.png")
Yes_B = pygame.image.load("Yes_B.png")
No_B = pygame.image.load("No_B.png")

###################################################################################################################################
                                                        #Funciones Archivos
###################################################################################################################################

# metodo para grabar un mapa en el archivo
# E: el path del archivo, un string con formato de lista
# S: ninguna

def guardar (archivo, strLista):
    fo = open(archivo, "w")
    #abre en forma de sobrrescribirlo,
    #si no existe lo crea
    fo.write(strLista)
    fo.close()

# metodo para leer una archivo
# E: el path del archivo
# S: un string con el contenido del archivo

def leer (archivo):
    fo = open(archivo, "r") # abre en forma
                            # de solo lectura
    resultado = fo.read()
    fo.close()
    #retorna lo que leyo del archivo
    return resultado

#cargar archivo
# lee un archivo y hace las validaciones para colocarlo en la lista
#salida: retorna una lista de lo leido
def cargarArchivo(archivo):
    strResultado = leer(archivo)
    if strResultado != "":
        return eval(strResultado)
    else:
        return []



#########################################################################################

#E:
#S:
#D: Obtine las letras del Keyboard

import pygame
def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
      return event.key
    else:
      pass

#E: screen , string
#S:
#D: Muestra lo que se esta escribiendo

def display_box(screen, message):
 # "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,28)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 225-100,
                    (screen.get_height() / 2) - 25,
                    502-100,30), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 227-100,
                    (screen.get_height() / 2) - 27,
                    504-100,34), 1)
  if len(message) != 0 :
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 200-100-20, (screen.get_height() / 2) - 20))
  pygame.display.flip()

#E: screen, string
#S: string
#D: Es un input
  
def ask(screen, question):
  #"ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  string=''
  display_box(screen, question + ": " + string.join(current_string))
  while 1:
    inkey = get_key()
    if inkey == pygame.K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == pygame.K_RETURN:
      break
    elif inkey == pygame.K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string))
  return string.join(current_string)


#########################################################################################
#Matriz

MatrizCompleta=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]


IndicesC = [0,1,2,3,4,5,6]
IndiceF = [0,1,2,3,4,5]

Matriz = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

filaAct=5
columAct=6


#E: 2 int
#S: 
#D: Carga la Matriz

def cargarMatriz(filaM,columnaM):
    
    global Matriz
    
    indiceFila = IndiceF.index(filaM)
    indiceColumna = IndicesC.index(columnaM)

    res=[]

    for fila in MatrizCompleta[indiceFila-5:indiceFila+1]:
        res = [fila[indiceColumna-6:indiceColumna+1]] + res

    Matriz = res
    #print(filaM,columnaM)




#Matriz = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

#Juego

turn = random.randint(0,1)
gameOver = False
contFilas = len (Matriz)
NoFicha=True
salirMenu=False
vsPC=False

ROW_COUNT = len(MatrizCompleta)
COLUMN_COUNT = len(MatrizCompleta[0])

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

WINDOW_LENGTH = 4

#E:
#S:
#D: Imprime la matriz en consola

def printC():
    print('Matriz Actual')
    for fila in Matriz:
        for columna in fila:
            print(columna,end='  ')
        print()
    print()
    print('Matriz Completa')
    for fila in MatrizCompleta:
        for columna in fila:
            print(columna,end='  ')
        print()

#E: Un string
#S: Un boolean
#D: Determina si el jugador esta en el rank

def esRank(player):
    for i in rank:
        if i[0] == player:
            return True
    return False


#E:
#S:
#D:Imprime la Matriz
def printM():
    global rank,partida_ant,ROW_COUNT,COLUMN_COUNT
    ROW_COUNT = len(MatrizCompleta)
    COLUMN_COUNT = len(MatrizCompleta[0])
    for i in range(9):
        for j in range(7):
            screen.blit(borde,(i*squareS,j*squareS))
    for i in range(1):
        for j in range(1,7):
            screen.blit(marco_izq,(i*squareS,j*squareS))
    for i in range(8,9):
        for j in range(1,7):
            screen.blit(marco_der,(i*squareS,j*squareS))
    for i in range(1,8):
        for j in range(1):
            screen.blit(marco_arriba,(i*squareS,j*squareS))


    for i in range(7):                
        for j in range(6):
            screen.blit(back,(i*squareS+100,j*squareS+squareS))
            if Matriz[j][i] == 0:
                screen.blit(empty,(i*squareS+100,j*squareS+squareS))
                #pygame.draw .circle(screen,Negro,(100+(i*squareS+squareS//2),j*squareS+squareS+squareS//2),radio)
            elif Matriz[j][i] == 1:
                screen.blit(fuego,(i*squareS+100,j*squareS+squareS))
                #pygame.draw .circle(screen,Rojo,(100+(i*squareS+squareS//2),j*squareS+squareS+squareS//2),radio)
            else:
                screen.blit(electrico,(i*squareS+100,j*squareS+squareS))

    numf = filaAct
    for i in range (6):
        numero = font2.render(str(numf),True,Negro)
        screen.blit(numero,(50,(i)*100+110))
        numf = numf-1

    numC = columAct-6
    for i in range (7):
        numero = font2.render(str(numC),True,Negro)
        screen.blit(numero,((i)*100+125,70))
        numC = numC+1
        
    screen.blit(flecha_abajo,(825,125))
    screen.blit(flecha_arriba,(0,125))
    screen.blit(flecha_izq,(0,425))
    screen.blit(flecha_der,(825,425))
    #screen.blit(back_button,(5,625))
    screen.blit(save_button,(815,625))
    
    if turn and not gameOver:
        screen.blit(nombre1,(600,0))
    elif not gameOver:
        screen.blit(nombre2,(600,0))

    pygame.display.update()
    
    if gameOver and not turn:
        
        pygame.time.wait(2500)
        screen.blit(FondoGane,(0,0))
        screen.blit(player1wins,(10,500))
        if vsPC == False:
            #print('a')
            guardar('partida_ant.txt',str([]))
            if esRank(jugador):
                index=0
                for i in rank:
                    if i[0] == jugador:
                        rank = rank[:index]+[[i[0]]+[i[1]+1]]+rank[index+1:]
                        guardar('rank.txt',str(rank))
                    else:
                        index += 1
            else:
                rank = rank +[[jugador,1]]
                guardar('rank.txt',str(rank))
        else:
            guardar('partida_antPC.txt',str([]))
            

    if gameOver and turn:
        
        pygame.time.wait(2500)
        screen.blit(FondoGane,(0,0))
        if vsPC==False:
            #print('b')
            guardar('partida_ant.txt',str([]))
            screen.blit(player2wins,(10,500))
            if esRank(jugador2):
                index=0
                for i in rank:
                    if i[0] == jugador2:
                        rank = rank[:index]+[[i[0]]+[i[1]+1]]+rank[index+1:]
                        guardar('rank.txt',str(rank))

                    else:
                        index += 1
            else:
                rank = rank +[[jugador2,1]]
                guardar('rank.txt',str(rank))
        else:
            guardar('partida_antPC.txt',str([]))
            screen.blit(pcwins,(10,500))
            

    
    pygame.display.update()
    
    #printC()



#E:Un string 'left', 'right' or 'up'
#S:
#D:Aplia la matriz hacia la derecha izquierda o arriba

def crecerMatriz(direction):
    global MatrizCompleta,IndicesC,IndiceF

    if direction == 'left':
        finalM = []

        for fila in MatrizCompleta:
            finalM = finalM + [[0,0,0,0,0,0,0]+ fila]

        MatrizCompleta = finalM
        IndicesC = [IndicesC[0]-7]+[IndicesC[1]-7]+[IndicesC[2]-7]+[IndicesC[3]-7]+[IndicesC[4]-7] +[IndicesC[5]-7]+[IndicesC[6]-7] + IndicesC 

    elif direction == 'right':
        finalM = []

        for fila in MatrizCompleta:
            finalM = finalM + [fila + [0,0,0,0,0,0,0]]

        MatrizCompleta = finalM
        IndicesC = IndicesC + [IndicesC[-7]+7]+[IndicesC[-6]+7]+[IndicesC[-5]+7]+[IndicesC[-4]+7]+[IndicesC[-3]+7] +[IndicesC[-2]+7]+[IndicesC[-1]+7]


        
    else:
        MatrizCompleta = MatrizCompleta+[[0]*len(MatrizCompleta[0]),[0]*len(MatrizCompleta[0]),[0]*len(MatrizCompleta[0]),[0]*len(MatrizCompleta[0]),[0]*len(MatrizCompleta[0]),[0]*len(MatrizCompleta[0])]
        IndiceF = IndiceF +[IndiceF[-1]+1]+[IndiceF[-1]+2]+[IndiceF[-1]+3]+[IndiceF[-1]+4]+[IndiceF[-1]+5]+[IndiceF[-1]+6]

        

#E: Un int
#S: Un boolean
#D: Determina si hay almenos una ficha a maximo 7 columnas de distancia

def maximo7(columna):
    fila = siguienteFila(columna,MatrizCompleta)

    if NoFicha or fila != 0:
        return True
    
    for i in range (columna-7,columna+8):
        
        if i < 0:
            continue
        elif i == columna:
            continue
        else:
            try:
                pos = MatrizCompleta[fila][i]
                if pos != 0:
                    return True
                if MatrizCompleta[fila+1][i]:
                    return True
            except:
                pass

    return False
                
    




#D: Determina si se puede jugar en la columna
#E: Un int
#S: Un booleano

def columnaValida(columna):
    if maximo7(columna)== False:
        return False

    if MatrizCompleta[-1][columna]==0:
        if columna > IndicesC.index(columAct):
            
            #mover_Der()
            #pygame.time.wait(500)
            return True
        elif columna < IndicesC.index(columAct)-7:
            #mover_Izq()
            #pygame.time.wait(500)
            return True            
        else:
            return True
    else:
        crecerMatriz('up')
        return True
    

#E: 3 int
#S: 
#D: Coloca la pieza del jugador
    
def colocarPieza(fila,columna,pieza):
    global MatrizCompleta,NoFicha
    NoFicha=False
    res = MatrizCompleta[:fila]+[MatrizCompleta[fila][:columna]+[pieza]+MatrizCompleta[fila][columna+1:]]+MatrizCompleta[fila+1:]
    MatrizCompleta = res

    #Agregar el mover matriz con un while
            



#E:Un int
#S:Un int
#D:Determina la fila en la que debe caer la siguiente pieza

def siguienteFila (columna,M):
    fila=0

    for i in M:
        if i[columna]==0:
            return fila
        else:
            fila += 1
    return fila
    
    

#E: Un int
#S: Un booleano
#D: Determina si el juego ha acabado con el ultimo movimiento

def winMove(piece):
    board = MatrizCompleta
    
    #Horizontal
    for columna in range((len(MatrizCompleta[0]))-3):
        for fila in range(len(MatrizCompleta)):
            if board[fila][columna] == piece and board[fila][columna+1] == piece and board[fila][columna+2] == piece and board[fila][columna+3] == piece:
                return True


    #Vertical
    #for columna
    for columna in range(len(MatrizCompleta[0])):
        for fila in range(len(MatrizCompleta)-3):
            if board[fila][columna] == piece and board[fila+1][columna] == piece and board[fila+2][columna] == piece and board[fila+3][columna] == piece:
                return True


    #Diagonales positivas
    for columna in range(len(MatrizCompleta[0])-3):
        for fila in range(len(MatrizCompleta)-3):
            if board[fila][columna] == piece and board[fila+1][columna+1] == piece and board[fila+2][columna+2] == piece and board[fila+3][columna+3] == piece:
                return True
    
    #Diagonales negativas
    for columna in range(len(MatrizCompleta[0])-3):
        for fila in range(3,len(MatrizCompleta)):
            if board[fila][columna] == piece and board[fila-1][columna+1] == piece and board[fila-2][columna+2] == piece and board[fila-3][columna+3] == piece:
                return True
    return False






#E: Un int
#S: Un int
#D: Define cual es la columna en la que desea jugar

def ColumR(columna):
    res = IndicesC.index(columAct)
    return res -(6-columna) 


#def startMusic():
 #   pygame.mixer.music.load('sound.mp3')
  #  pygame.mixer.music.play(-1)


##############################################
  
  #Movimiento
  
###############################################

#E:
#S:
#D: Hace un scroll de la pantalla a la izquierda

def mover_Izq():
    global columAct
    columAct = columAct -7
    #iC = (IndicesC.index(columAct))-7
    try:
        cargarMatriz(filaAct,columAct)
    except:
        crecerMatriz('left')
        cargarMatriz(filaAct,columAct)
    printM()
    
#E:
#S:
#D:Hace un scroll de la pantalla a la derecha        

def mover_Der():
    global columAct
    columAct = columAct +7
    #iC = (IndicesC.index(columAct))-7
    try:
        cargarMatriz(filaAct,columAct)
    except:
        crecerMatriz('right')
        cargarMatriz(filaAct,columAct)
    printM()

#E:
#S:
#D: Hace un scroll de la pantalla hacia arriba

def mover_UP():
    global filaAct
    filaAct = filaAct +6
    #iC = (IndicesC.index(columAct))-7
    try:
        cargarMatriz(filaAct,columAct)
    except:
        crecerMatriz('up')
        cargarMatriz(filaAct,columAct)
    printM()
         

#E:
#S:
#D:Hace un scroll de la pantalla hacia abajo expto si ya esta en el fondo
    
def mover_Down():
    global filaAct
    fila = filaAct -6
    #iC = (IndicesC.index(columAct))-7
    try:
        cargarMatriz(fila,columAct)
        filaAct = fila
    except:
        pass
        
    printM()



#################################################################################
#################################################################################
#################################################################################


#Archivos para continuar partida
#jugador,jugador2
#nombre1,nombre2
#MatrizCompleta,IndicesC,IndiceF,Matriz,filaAct,columAct
#turn,gameOver,conFilas,NoFicha,salirMenu,vsPC


#E:
#S:
#D:Guardan la partida en cada modo

def guardarPartida():
    global partida_ant
    partida = [jugador,jugador2,MatrizCompleta,IndicesC,IndiceF,Matriz,filaAct,columAct,turn,gameOver,contFilas,NoFicha,salirMenu,vsPC]
    guardar('partida_ant.txt',str(partida))

def guardarPartidaPC():
    global partida_antPC
    partida = [jugador,jugador2,MatrizCompleta,IndicesC,IndiceF,Matriz,filaAct,columAct,turn,gameOver,contFilas,NoFicha,salirMenu,vsPC]
    guardar('partida_antPC.txt',str(partida))

#E:
#S:
#D:Carga la partida en cada modo

def cargarPartida():
    global player1wins,player2wins,partida_ant,jugador,jugador2,nombre1,nombre2,MatrizCompleta,IndicesC,IndiceF,Matriz,filaAct,columAct,turn,gameOver,contFilas,NoFicha,salirMenu,vsPC
    jugador = partida_ant[0]
    jugador2 = partida_ant[1]
    nombre1 = font.render(jugador,True,Azul)
    nombre2 = font.render(jugador2,True,Azul)
    player1wins = font.render(jugador + '  HA  GANADO',True,Azul)
    player2wins = font.render(jugador2 +' HA  GANADO',True,Azul)
    MatrizCompleta = partida_ant[2]
    IndicesC = partida_ant[3]
    IndiceF = partida_ant[4]
    Matriz = partida_ant[5]
    filaAct = partida_ant[6]
    columAct = partida_ant[7]
    turn = partida_ant[8]
    gameOver = partida_ant[9]
    contFilas = partida_ant[10]
    NoFicha = partida_ant[11]
    salirMenu = partida_ant[12]
    vsPC = partida_ant[13]


def cargarPartidaPC():
    global player1wins,partida_antPC,jugador,jugador2,nombre1,nombre2,MatrizCompleta,IndicesC,IndiceF,Matriz,filaAct,columAct,turn,gameOver,contFilas,NoFicha,salirMenu,vsPC
    jugador = partida_antPC[0]
    jugador2 = partida_antPC[1]
    nombre1 = font.render(jugador,True,Azul)
    nombre2 = font.render(jugador2,True,Azul)
    player1wins = font.render(jugador + '  HA  GANADO',True,Azul)
    MatrizCompleta = partida_antPC[2]
    IndicesC = partida_antPC[3]
    IndiceF = partida_antPC[4]
    Matriz = partida_antPC[5]
    filaAct = partida_antPC[6]
    columAct = partida_antPC[7]
    turn = partida_antPC[8]
    gameOver = partida_antPC[9]
    contFilas = partida_antPC[10]
    NoFicha = partida_antPC[11]
    salirMenu = partida_antPC[12]
    vsPC = partida_antPC[13]


#E:Un string
#S:
#D:Verifica si hay una partida anterior 

def hayPartAnt(tipo):
    global partida_ant,partida_antPC
    partida_antPC = cargarArchivo ('partida_antPC.txt')
    partida_ant = cargarArchivo ('partida_ant.txt')

    if tipo == True:
        if partida_antPC == []:
            return False
        elif partida_antPC[13]==tipo:

            return True
        else:
            return False
        
    else:
        if partida_ant == []:
            return False
        elif partida_ant[13]==tipo:

            return True
        else:
            return False

        
#    if partida_ant == []:
 #       return False
  #  elif partida_ant[13]==tipo:
   #     if tipo == True:
    #        partida_ant = cargarArchivo ('partida_ant.txt')
     #   else:
      #      partida_antPC = cargarArchivo ('partida_antPC.txt')
       # return True
    #else:
     #   return False




#
#
#

#def restart():
 #   global rank,partida_ant,partida_antPC,jugador,jugador2,MatrizCompleta,IndicesC,IndiceF,Matriz,filaAct,columAct,turn,gameOver,contFilas,NoFicha,salirMenu,vsPC,ROW_COUNT,COLUMN_COUNT,EMPTY,PLAYER_PIECE,AI_PIECE,WINDOW_LENGTH,nombre1,nombre2,player1wins,player2wins

#    rank = []
 #   partida_ant = []
  #  partida_antPC = []
   # jugador = ''
#    jugador2 = 'System '
 #   MatrizCompleta=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
  #  IndicesC = [0,1,2,3,4,5,6]
   # IndiceF = [0,1,2,3,4,5]
#    Matriz = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
 #   filaAct=5
  #  columAct=6
   # turn = random.randint(0,1)
#    gameOver = False
 #   contFilas = len (Matriz)
  #  NoFicha=True
    #salirMenu=False
#    vsPC=False
 #   ROW_COUNT = len(MatrizCompleta)
  #  COLUMN_COUNT = len(MatrizCompleta[0])
   # EMPTY = 0
#    PLAYER_PIECE = 1
 #   AI_PIECE = 2
  #  WINDOW_LENGTH = 4
   # nombre1 = font.render(jugador,True,Azul)
 #   nombre2 = font.render(jugador2,True,Azul)
#    player1wins = font.render(jugador + '  HA  GANADO',True,Azul)
  #  player2wins = font.render(jugador2 +' HA  GANADO',True,Azul)

#E:
#S:
#D: Juego multijugador
  
def startVSGame():
    printM()
    global gameOver,turn,vsPC
    vsPC=False
   # startMusic() 
    while not gameOver :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.display.quit()
                sys.exit()
                

            if event.type == pygame.MOUSEMOTION:
                #pygame.draw.rect(screen, Negro, (0,0,9*squareS, squareS))
                for i in range(1,8):
                    screen.blit(borde,(i*100,0))
                    screen.blit(marco_arriba,(i*squareS,0*squareS))
                    
                posx = event .pos[0]

                if turn == True:
                    numC = columAct-6
                    for i in range (7):
                        numero = font2.render(str(numC),True,Negro)
                        screen.blit(numero,((i)*100+125,70))
                        numC = numC+1
                    
                    #pygame.draw.circle(screen,Rojo,(posx, int(squareS/2)),radio)
                    if posx>100 and posx<800:
                        screen.blit(fuego,(posx-50, 0))
                        screen.blit(borde,(0,0))
                        screen.blit(borde,(8*100,0))
                        screen.blit(nombre1,(600,0))
                        
                    else:
                        screen.blit(nombre1,(600,0))
                        
                else:
                    numC = columAct-6
                    for i in range (7):
                        numero = font2.render(str(numC),True,Negro)
                        screen.blit(numero,((i)*100+125,70))
                        numC = numC+1
                    
                    #pygame.draw.circle(screen,Amarillo,(posx, int(squareS/2)),radio)
                    if posx>100 and posx<800:
                        screen.blit(electrico,(posx-50, 0))
                        screen.blit(borde,(0,0))
                        screen.blit(borde,(8*100,0))
                        screen.blit(nombre2,(600,0))
                        
                    else:
                        screen.blit(nombre2,(600,0))
                    
                pygame.display.update()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                
                if posx>100 and posx<800:
                    #Quitar Boton
                    pygame.draw.rect(screen, Negro, (0,0,7*squareS, squareS))
                    #print(event.pos)
                
                    if turn == True:


                        columna = int(math.floor(posx/squareS))

                        if columna != 0 and columna !=8:
                            columna = columna-1
                        else:
                            print()
                            print('Fuera del rango')
                            startVSGame()
                        
                        columna = ColumR(columna)
                    
                    
                        if columnaValida(columna):
                            fila = siguienteFila (columna,MatrizCompleta)

                            colocarPieza(fila,columna,1)

                            cargarMatriz(filaAct,columAct)
                           # printM()
                            turn = not turn

                            if winMove(1):
                                gameOver = True

                            printM()
                                

                        else:
                            print()
                            printM()
                            screen.blit(NoPermitido,(60,200))
                            screen.blit(NoPermitido2,(40,300))
                            pygame.display.update()
                            pygame.time.wait(1000)
                            printM()
                            
                               

                       # turn = not turn

                       # if winMove(1):
                        #    gameOver = True

                    else:

                    
                        columna = int(math.floor(posx/squareS))-1
                        columna = ColumR(columna)

                        if columnaValida(columna):
                            fila = siguienteFila (columna,MatrizCompleta)
                            colocarPieza(fila,columna,2)
                            cargarMatriz(filaAct,columAct)
                            #printM()
                            turn = not turn

                            if winMove(2):
                                gameOver = True
                            printM()
                        
                        else:
                            print()
                            printM()
                            screen.blit(NoPermitido,(60,200))
                            screen.blit(NoPermitido2,(40,300))
                            pygame.display.update()
                            pygame.time.wait(1000)
                            printM()
                            
                        #turn = not turn

                        #if winMove(2):
                           # gameOver = True


                if posx>825 and posx<900 and posy>125 and posy<200:
                    mover_Down()


                if posx>0 and posx<75 and posy>125 and posy<200:
                    mover_UP()


                if posx>825 and posx<900 and posy>425 and posy<500:
                    mover_Der()


                if posx>0 and posx<75 and posy>425 and posy<500:
                    mover_Izq()

                if posx>815 and posx<900 and posy>625 and posy<700:
                    guardarPartida()
                    pygame.time.wait(500)
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    sys.exit()
                    



    pygame.time.wait(2500)
    pygame.mixer.music.stop()
    pygame.display.quit()
    sys.exit()


########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################

#E: Una lista y un int
#S: Un int
#D: Determina el puntaje de la ventana
    
def evaluate_window(window, piece):
	score = 0
	opp_piece = PLAYER_PIECE
	
	if piece == PLAYER_PIECE:
		opp_piece = AI_PIECE

	if window.count(piece) == 4:
		score += 100000
	elif window.count(piece) == 3 and window.count(EMPTY) == 1:
		score += 5
	elif window.count(piece) == 2 and window.count(EMPTY) == 2:
		score += 2
	elif window.count(EMPTY) == 2 and window.count(opp_piece) == 2:
		score -= 2
		
	if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
		score -= 4

	return score

#E: Una lista
#S:
#D: Determina el center Array
    
def getCA(board):
    res = []
    for i in range(len(board)):
        res += [board[i][COLUMN_COUNT//2]]
    return res

#E: Una lista y un int
#S: Un int
#D: Determina el colum Array

def getColA(board,col):
    res = []
    for i in range(len(board)):
        res += [board[i][col]]
    return res

#E: Una lista y un int
#S: Un int
#D: Determina el score de la posicion

def score_position(board, piece):
	score = 0

	## Score center column
	#print(COLUMN_COUNT)
	
	center_array = getCA(board)
	center_count = center_array.count(piece)
	score += center_count * 2

	## Score Horizontal
	for r in range(ROW_COUNT):
		row_array = board[r:]
		for c in range(COLUMN_COUNT-3):
			window = row_array[c:c+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score Vertical
	for c in range(COLUMN_COUNT):
		col_array = getColA(board,c)
		for r in range(ROW_COUNT-3):
			window = col_array[r:r+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score posiive sloped diagonal
	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	return score

#E: Una lista 
#S: Un booleano
#D: Determina si hay winning move en la FakeBoard

def winning_move(board, piece):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True
	return False


#E: Una lista
#S: Una lista
#D: Determina las columnas validas
			    
def get_valid_locations(board):
    res = []
    for i in range(len(board[0])):
        if columnaValida(i):
            res += [i]
    random.shuffle(res)
    return res

#E: Una lista
#S: Un boolean
#D: Determina si es el ultimo nodo

def is_terminal_node(board):
	return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0


#E: Una lista y 3 int
#S: 
#D: Pone la pieza en el FakeBoard
    
def drop_piece(board, row, col, piece):
    try:
        board[row][col] = piece
    except:
        pass
	#print('colocar', row, col, piece)
	

#E: Una lista, 2 numeros inf y - inf y un boolean
#S: Un int
#D: Algoritmo de arboles que retorna cual sera la mejor posicion jugar en un futuro
    
def minimax(board, depth, alpha, beta, maximizingPlayer):
	#print(depth)
	valid_locations = get_valid_locations(board)
	is_terminal = is_terminal_node(board)
	#print('fsd',board)
	if depth == 0 or is_terminal:
		if is_terminal:
			if winning_move(board, AI_PIECE):
				return [None, 100000000000000]
			elif winning_move(board, PLAYER_PIECE):
				return [None, -100000000000000]
			else: # Game is over, no more valid moves
				return (None, 0)
		else: # Depth is zero
			return [None, score_position(board, AI_PIECE)]
	if maximizingPlayer:
		value = -math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = siguienteFila(col , board)
			b_copy = list(map(list,board))
			drop_piece(b_copy, row, col, AI_PIECE)
			#print(b_copy, depth-1, alpha, beta, False)
			new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
			if new_score > value:
				value = new_score
				column = col
			alpha = max(alpha, value)
			if alpha >= beta:
				break
		return [column, value]
	else: # Minimizing player
		value = math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = siguienteFila(col , board)
			b_copy = list(map(list,board))
			drop_piece(b_copy, row, col, PLAYER_PIECE)
			new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
			if new_score < value:
				value = new_score
				column = col
			beta = min(beta, value)
			if alpha >= beta:
				break
		return column, value

#E: Una lista y un int
#S: Un int
#D: Determina la mejor posicion a jugar
	    
def pick_best_move(board,piece):
    valid_locations = get_valid_locations(board)
    print(valid_locations)
    best_score = -10000
    best_col = random.choice(valid_locations)
    for columna in valid_locations:
        fila = siguienteFila(columna,board)
        temp_board = list(map(list,board))
        temp_board[fila][columna]=piece

        score = score_position(temp_board,piece)
        if score > best_score:
            best_score = score
            best_col = columna

    return best_col

#E:
#S:
#D: Juego multijugador
  
def startVSPC():
    printM()
    global gameOver,turn,vsPC,ROW_COUNT,COLUMN_COUNT

    if NoFicha:
        turn = False
    
    ROW_COUNT = len(MatrizCompleta)
    COLUMN_COUNT = len(MatrizCompleta[0])
    vsPC=True
   # startMusic() 
    while not gameOver :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.display.quit()
                sys.exit()
                

            if event.type == pygame.MOUSEMOTION:
                #pygame.draw.rect(screen, Negro, (0,0,9*squareS, squareS))
                for i in range(1,8):
                    screen.blit(borde,(i*100,0))
                    screen.blit(marco_arriba,(i*squareS,0*squareS))
                    
                posx = event .pos[0]

                if turn == True:
                    
                    numC = columAct-6
                    for i in range (7):
                        numero = font2.render(str(numC),True,Negro)
                        screen.blit(numero,((i)*100+125,70))
                        numC = numC+1
                    #pygame.draw.circle(screen,Rojo,(posx, int(squareS/2)),radio)
                    if posx>100 and posx<800:
                        screen.blit(fuego,(posx-50, 0))
                        screen.blit(borde,(0,0))
                        screen.blit(borde,(8*100,0))
                        screen.blit(nombre1,(600,0))
                        
                    else:
                        screen.blit(nombre1,(600,0))
                        
                pygame.display.update()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                
                if posx>100 and posx<800:
                    #Quitar Boton
                    pygame.draw.rect(screen, Negro, (0,0,7*squareS, squareS))
                    #print(event.pos)
                
                    if turn == True:


                        columna = int(math.floor(posx/squareS))

                        if columna != 0 and columna !=8:
                            columna = columna-1
                        else:
                            print()
                            print('Fuera del rango')
                            startVSGame()
                        
                        columna = ColumR(columna)
                    
                    
                        if columnaValida(columna):
                            fila = siguienteFila (columna,MatrizCompleta)

                            colocarPieza(fila,columna,1)

                            cargarMatriz(filaAct,columAct)
                           # printM()
                            turn = not turn

                            if winMove(1):
                                gameOver = True

                            printM()
                                

                        else:
                            print()
                            printM()
                            screen.blit(NoPermitido,(60,200))
                            screen.blit(NoPermitido2,(40,300))
                            pygame.display.update()
                            pygame.time.wait(1000)
                            printM()
                            
                            

                       # turn = not turn

                       # if winMove(1):
                        #    gameOver = True


                if posx>825 and posx<900 and posy>125 and posy<200:
                    mover_Down()


                if posx>0 and posx<75 and posy>125 and posy<200:
                    mover_UP()


                if posx>825 and posx<900 and posy>425 and posy<500:
                    mover_Der()


                if posx>0 and posx<75 and posy>425 and posy<500:
                    mover_Izq()

                if posx>815 and posx<900 and posy>625 and posy<700:
                    guardarPartidaPC()
                    pygame.time.wait(500)
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    sys.exit()


        if turn == False and not gameOver:
            if turn :
                screen.blit(nombre1,(700,0))
            else:
                screen.blit(nombre2,(700,0))
            
            #columna = pick_best_move(MatrizCompleta,2)
            #columna = MejorMove(2)
            columna = minimax(MatrizCompleta, 3, -math.inf, math.inf, True)
            columna = columna[0]

            b_copyx = list(map(list,MatrizCompleta))
            fila = siguienteFila (columna,b_copyx)
            drop_piece(b_copyx, fila, columna, 2)
            if not winning_move(b_copyx, 2):
                if MatrizCompleta[0][0] == 1 and MatrizCompleta[0][1] == 1 and MatrizCompleta[0][2] == 1:
                    crecerMatriz('left')
                    columna = 6
                if MatrizCompleta[0][-1] == 1 and MatrizCompleta[0][-2] == 1 and MatrizCompleta[0][-3] == 1:
                    crecerMatriz('right')
                    columna = (len(MatrizCompleta[0]))-7

                        
            if columnaValida(columna):
                pygame.time.wait(100)
                fila = siguienteFila (columna,MatrizCompleta)
                colocarPieza(fila,columna,2)
                cargarMatriz(filaAct,columAct)
                #printM()
                turn = not turn

                if winMove(2):
                    gameOver = True
                printM()
                        


            #turn = not turn

            #if winMove(2):
            # gameOver = True



    pygame.time.wait(3000)
    pygame.mixer.music.stop()
    pygame.display.quit()
    sys.exit()


########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################

#E: Un pivot y array
#S: Una lista
#D: Crea una lista con los menores
    
def menores(pivot,arr):
    res=[]
    for i in arr:
        if i[1] < pivot:
            res = res + [i]
    return res


#E: Un pivot y un array
#S: Una lista
#D: Crea una lista con los elementos menores

def mayores(pivot,arr):
    res=[]
    for i in arr:
        if i[1] >= pivot:
            res = res + [i]
    return res


    
#E: Un array
#S: Una lista
#D: Ordena los elementos por puntaje

def qsort(arr): 
    if len(arr) <= 1:
        return arr
    else:
        menoresqs = menores(arr[0][1],arr[1:])
        mayoresqs = mayores(arr[0][1],arr[1:])
        return qsort(mayoresqs)+[arr[0]]+qsort(menoresqs)

#E: 
#S:
#D: Pantalla de rankings

def starRanking():
    screen.blit(FondoRank,(0,0))
    rankers = qsort(rank)
    j = font.render(' POS',True,Negro)
    k = font.render(' NAME',True,Negro)
    l = font.render(' SCORE',True,Negro)

    
    screen.blit(j,(0,0))
    screen.blit(k,(300,0))
    screen.blit(l,(600,0))
    #screen.blit(back_button,(5,625))

    for i in range(1,11):
        try:
            r = font.render(str(i),True,Negro)
            a = font.render(rankers[i-1][0],True,Negro)
            b = font.render(str(rankers[i-1][1]),True,Negro)
            
            screen.blit(r,(50,i*50))
            screen.blit(a,(300,i*50))
            screen.blit(b,(700,i*50))
        except:
            r = font.render(str(i),True,Negro)
            a = font.render('EMPTY',True,Negro)
            b = font.render(str(0),True,Negro)
            
            screen.blit(r,(50,i*50))
            screen.blit(a,(300,i*50))
            screen.blit(b,(700,i*50))   
        
    pygame.display.update()
    while not salirMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.display.quit()
                sys.exit()    
            #if event.type == pygame.MOUSEBUTTONDOWN:           No sirve regresar al menu
                #posx = event.pos[0]
                #posy = event.pos[1]
                #if posx > 3 and posx<75:
                    #if posy > 624 and posy < 696:
                        #restart()
                        #menuP()
                        








########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################

#E:
#S:
#D: Pantalla de continuar vs

def continuarVS():
    global jugador,player1wins,jugador2,player2wins,nombre1,nombre2
    screen.blit(selector_Fondo,(0,0))
    screen.blit(Continuar,(35,100))
    screen.blit(Continuar2,(270,170))
    screen.blit(Yes_B,(200,300))
    screen.blit(No_B,(500,300))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.display.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                if posy > 300 and posy <500:
                    if posx > 200 and posx<500:
                        cargarPartida()
                        return startVSGame()
                        
                        
                    elif posx > 500 and posx < 700:
                        guardar('partida_ant.txt',str([]))
                        
                        return llamarVSGame()
            
    
#E:
#S:
#D: Pantalla de continual vs pc

def continuarVSPC():
    global jugador,player1wins,nombre1
    screen.blit(selector_Fondo,(0,0))
    screen.blit(Continuar,(35,100))
    screen.blit(Continuar2,(270,170))
    screen.blit(Yes_B,(200,300))
    screen.blit(No_B,(500,300))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.display.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]

                if posy > 300 and posy <500:
                    if posx > 200 and posx<500:
                        cargarPartidaPC()
                        return startVSPC()
                        
                        
                    elif posx > 500 and posx < 700:
                        guardar('partida_antPC.txt',str([]))

                        return llamarVSPC()



    
#E:
#S:
#D: Pantalla de llamar a vs game

def llamarVSGame():
    global jugador,player1wins,jugador2,player2wins,nombre1,nombre2
    if hayPartAnt(False):
        return continuarVS()
    else:
        screen.blit(FondoMenuNombres,(0,0))
        jugador = str(ask(screen,'NOMBRE DEL JUGADOR 1 '))
        pygame.time.wait(400)
        jugador2 = str(ask(screen,'NOMBRE DEL JUGADOR 2 '))
        player1wins = font.render(jugador + '  HA  GANADO',True,Azul)
        player2wins = font.render(jugador2 + '  HA  GANADO',True,Azul)
        nombre1 = font.render(jugador,True,Azul)
        nombre2 = font.render(jugador2,True,Azul)
        pygame.time.wait(500)

        return startVSGame()

#E:
#S:
#D: Pantalla de llamar a vs pc game

def llamarVSPC():
    global jugador,player1wins,nombre1
    
    if hayPartAnt(True):
        return continuarVSPC()
    else:
        screen.blit(FondoMenuNombres,(0,0))
        jugador = str(ask(screen,'NOMBRE DEL JUGADOR '))
        player1wins = font.render(jugador + '  HA  GANADO',True,Azul)
        nombre1 = font.render(jugador,True,Azul)
        pygame.time.wait(500)
        return startVSPC()

#E:
#S:
#D: Pantalla de llamar rankings

def llamarRankings():
    return starRanking()



#E:
#S:
#D: Pantalla de menu

def menuP():
    global rank,partida_ant
    rank = cargarArchivo ('rank.txt')
    partida_ant = cargarArchivo ('partida_ant.txt')
    
    screen.blit(FondoMenuP,(0,0))
    screen.blit(titulo,(100,0+25))
    screen.blit(vsPCplay,(100,100+25))
    screen.blit(vsPlay,(100,200+25))
    screen.blit(rankings,(100,300+25))
    pygame.display.update()
    while not salirMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.display.quit()
                sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            posy = event.pos[1]

            if posx>100 and posx<470:
                if posy>100+25 and posy<165+25:
                    pygame.time.wait(500)
                    return llamarVSPC()

                if posy>300+25 and posy<365+25:
                    pygame.time.wait(500)
                    return llamarRankings()
                
            if posx>100 and posx<560:
                if posy>200+25 and posy<265+25:
                    pygame.time.wait(500)
                    return llamarVSGame()


















##################################
#       #Interface
#################################




squareS = 100
widht = 9*squareS
height = 7*squareS

size = (widht,height)

radio = (squareS//2)-5

screen = pygame.display.set_mode(size)

pygame.display.update()

pygame.mixer.music.load('sound.ogg')
pygame.mixer.music.play(-1)

#def dibujar_Matriz(Matriz:

menuP()
                   




#FALTA
#GUARDAD PARTIDAS
#CARGAR PARTIDAS
#IA







    
    
