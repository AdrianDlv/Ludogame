import pygame
import sys
from pygame.locals import *
 
pygame.init()
 
ventana=pygame.display.set_mode((900,660))
pygame.display.set_caption("Ludo")
 
#colores
negro=(0,0,0)
blanco=(255,255,255)
rojo=(255,37,34)
amarillo=(255,255,34)
azul=(34,101,255)
verde=(14,176,12)
n=2
coordbase=-30
cont= True
miFuente=pygame.font.Font(None,30)
miTexto=miFuente.render("LUDO V0.9",0,blanco)
miTexto2=miFuente.render("Version Alpha",0,blanco)
 
#FICHAS
FichaAzul=pygame.image.load("figuras_ludo/fichaAzul.png")
FichaVerde=pygame.image.load("figuras_ludo/fichaVerde.png")
FichaAmarilla=pygame.image.load("figuras_ludo/fichaAmarilla.png")
FichaRoja=pygame.image.load("figuras_ludo/fichaRoja.png")
 
#DADOS
DadoAnimado=pygame.image.load("figuras_ludo/dado_animado.gif")
Dado1=pygame.image.load("figuras_ludo/dado1.png")
Dado2=pygame.image.load("figuras_ludo/dado2.png")
Dado3=pygame.image.load("figuras_ludo/dado3.png")
Dado4=pygame.image.load("figuras_ludo/dado4.png")
Dado5=pygame.image.load("figuras_ludo/dado5.png")
Dado6=pygame.image.load("figuras_ludo/dado6.png")
 
 
'''PARTE GRAFICA :v'''
#-----------------------------------------------------
pygame.draw.rect(ventana,blanco,(0,0,660,660))
pygame.draw.rect(ventana,verde,(0,300,240,60))
pygame.draw.rect(ventana,amarillo,(300,420,60,240))
pygame.draw.rect(ventana,azul,(300,0,60,240))
pygame.draw.rect(ventana,rojo,(420,300,240,60))
pygame.draw.circle(ventana,blanco,(80,80),10)
 
while cont==True:
	coordbase+=30
	pygame.draw.line(ventana,negro,(0,coordbase),(660,coordbase))
	pygame.draw.line(ventana,negro,(coordbase,0),(coordbase,660))
	if coordbase>=660:
		cont=False
 
 
pygame.draw.rect(ventana,verde,(0,0,240,240))
pygame.draw.rect(ventana,amarillo,(0,420,240,240))
pygame.draw.rect(ventana,azul,(420,0,240,240))
pygame.draw.rect(ventana,rojo,(420,420,240,240))
pygame.draw.rect(ventana,blanco,(241,241,179,179))
pygame.draw.polygon(ventana,verde,((241,241),(330,330),(241,419)))
pygame.draw.polygon(ventana,amarillo,((241,419),(330,330),(419,419)))
pygame.draw.polygon(ventana,azul,((241,241),(330,330),(421,241)))
pygame.draw.polygon(ventana,rojo,((419,241),(330,330),(419,419)))
#------------------CIRCULOS----------------------------------
pygame.draw.circle(ventana,blanco,(60,60),35)
pygame.draw.circle(ventana,blanco,(180,60),35)
pygame.draw.circle(ventana,blanco,(60,180),35)
pygame.draw.circle(ventana,blanco,(180,180),35)
pygame.draw.circle(ventana,blanco,(480,480),35)
pygame.draw.circle(ventana,blanco,(480,600),35)
pygame.draw.circle(ventana,blanco,(600,480),35)
pygame.draw.circle(ventana,blanco,(600,600),35)
pygame.draw.circle(ventana,blanco,(60,480),35)
pygame.draw.circle(ventana,blanco,(180,480),35)
pygame.draw.circle(ventana,blanco,(600,180),35)
pygame.draw.circle(ventana,blanco,(60,600),35)
pygame.draw.circle(ventana,blanco,(600,60),35)
pygame.draw.circle(ventana,blanco,(480,60),35)
pygame.draw.circle(ventana,blanco,(480,180),35)
pygame.draw.circle(ventana,blanco,(600,60),35)
pygame.draw.circle(ventana,blanco,(180,600),35)

#------------------------Aqui tu codigo xd-----------------
cont=0
casa=[]
casillas={}
pos_ini=[]
#posicion de las casillas del tablero:
for i in range(4):
	casa.append([])
casa[0].append(101)
casa[0].append(102)
casa[0].append(103)
casa[0].append(104)
casa[1].append(201)
casa[1].append(202)
casa[1].append(203)
casa[1].append(204)
casa[2].append(301)
casa[2].append(302)
casa[2].append(303)
casa[2].append(304)
casa[3].append(401)
casa[3].append(402)
casa[3].append(403)
casa[3].append(404)

#casillas[101]=()
#casillas[102]=()
#casillas[103]=()
#casillas[104]=()
#casillas[201]=()
#casillas[202]=()
#casillas[203]=()
#casillas[204]=()
#casillas[301]=()
#casillas[302]=()
#casillas[303]=()
#casillas[304]=()
#casillas[401]=()
#casillas[402]=()
#casillas[403]=()
#casillas[404]=()



 
#---------------------------------------
casillas[1]=(365,5)
for i in range (2,9):
	casillas[i]=(365,casillas[i-1][1]+30)
casillas[9]=(425,245)
for i in range (10,17):
	casillas[i]=(casillas[i-1][0]+30,245)
casillas[17]=(casillas[16][0],305)
casillas[18]=(casillas[17][0],365)
for i in range (19,26):
	casillas[i]=(casillas[i-1][0]-30,365)
casillas[26]=(casillas[25][0]-60,425)
for i in range(27,34):
	casillas[i]=(365,casillas[i-1][1]+30)
casillas[34]=(305,casillas[33][1])
casillas[35]=(245,casillas[34][1])
for i in range (36,43):
	casillas[i]=(245,casillas[i-1][1]-30)
casillas[43]=(215,casillas[42][1]-60)
for i in range (44,51):
	casillas[i]=(casillas[i-1][0]-30,365)
casillas[51]=(5,casillas[50][1]-60)
casillas[52]=(5,casillas[51][1]-60)
for i in range (53,60):
	casillas[i]=(casillas[i-1][0]+30,245)
casillas[60]=(245,casillas[59][1]-30)
for i in range (61,68):
	casillas[i]=(245,casillas[i-1][1]-30)
casillas[68]=(305,5)
 
#Definir posicion de las casillas en casa, falta que tengan un tamaño adecuado

 

#ventana.blit(FichaAzul,casillas[101])
ventana.blit(FichaAzul,(50,50))
 
#-------------------------
#definimos la posicion inicial para caáa jugador
#pos_ini.append()
#pos_ini.append()
#pos_ini.append()
#pos_ini.append()
#decimos que fichas[i][j]=-1 si la ficha j del jugador i esta en la rec_final, el primer numero dice la cantidad de fichas en rec_f
fichas=[]
for i in range(4):
	fichas.append([])
	fichas[i].append(0)
	for j in range(4):
		fichas[i].append(casa[i][j])
 
ficha_color=[]
ficha_color.append(FichaAzul)
ficha_color.append(FichaRoja)
ficha_color.append(FichaAmarilla)
ficha_color.append(FichaVerde)

 
def jugada(cont):
 
	w=input("Tire el dado\n")
	dado = random.randint(1, 6)
 
	print("Su resultado fue", dado)
 
	k = int(input("¿Que ficha desea mover? "))
 
	if (fichas[cont % 4][k] >100):
		fichas[cont % 4][k] = pos_ini[cont % 4] + dado
	else:
		fichas[cont % 4][k] = (fichas[cont % 4][k] + dado) % 68
	ventana.blit(ventana,ficha_color[cont%4],casillas[fichas[cont%4][k]])
 
 
def Comer(numero_pos, cont):
	for i in range(4):
		if (i == cont):
			continue
		for j in range(1, 5):
			if (fichas[i][j] == numero_pos):
				fichas[i][j] = -i 
 
 
 
#----------------------------------------------------------
while True:
	for evento in pygame.event.get():
 
		if evento.type ==QUIT:
			pygame.quit()
			sys.exit()
		ventana.blit(miTexto,(700,30))
		ventana.blit(miTexto2,(700,50))
 
 
	pygame.display.update()# your code goes here