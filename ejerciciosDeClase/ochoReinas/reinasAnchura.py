#Autor: Pedraza Martínez José Alberto
#Fecha 22/10/2020
#Descripción: Resulve el problema de las 8 reinas utilizando busqueda en anchura

import copy #libreria para realizar la copia de una lista

costo = 0	#Es la variable que cuenta el costo
numeroDeReinas=8 #Se modifica dependiendo del número de reinas que se necesiten

#Función que inicializa el estado inicial con 0 reinas, regresa una matriz de nxm con ceros
#------------------------
def creaMatriz(n,m):
	matriz = []
	for i in range(n):
		a = [0]*m
		matriz.append(a)
	return matriz 
#-------------------------

#se inicializa el nivel incial que sólo contiene el estado inicial
nivel=[creaMatriz(numeroDeReinas,numeroDeReinas)]


#Función principal
#--------------------------------------------------------------
def main():	
	global nivel
	resolver(nivel,0) #Se manda a llamar a la función que resuleve el problema // se le manda 0 debido a que no hay ninguna reina en el tablero
	print("costo: ",costo)	#Al terminar imprime el costo
#--------------------------------------------------------------

#Función que resuelve el problema
#------------------------------------------------------------------------------------------------
def resolver(nivel,numNivel):
	numRespuesta=1

	#Si se llega al nivel final y se muestran las respuestas
	if numNivel == numeroDeReinas:	

		#Muestra las respuestas
		#----------------------------------	
		for respuesta in nivel:
			print("Respuesta ",numRespuesta)
			numRespuesta=numRespuesta+1
			for i in range(numeroDeReinas):	
				print(respuesta[i])
			print("\n")
		#-----------------------------------

		return 1#Termina la función

	#Se vuelve a llamar a la función con el nuevo nivel
	resolver(generarNivel(nivel,numNivel),numNivel+1)
#------------------------------------------------------------------------------------------------

#Función que genera un nuevo nivel, recibe un nivel y genera el nuevo nivel
#-----------------------------------------
def generarNivel(nivel,numNivel):
	nuevoNivel=[]

	#Recorre los estados del nivel
	#-------------------------------
	for estado in nivel:
		hijos = generarHijos(estado) #genera los hijos del estado

		for hijo in hijos:
			nuevoNivel.append(hijo)#Agrega los hijos del estado en el nuevo nivel
	#---------------------------------		
	
	print("ternina el nivel\n",numNivel)#Indica que ya se terminó de generar el nuevo nivel
			
	return nuevoNivel #Se regresa el nuevo nivel
#------------------------------------------

#Función para generar hijos, recibe un estado y devuelve una lista con sus estdos hijos
#------------------------------------------------------------------------------------------------------
def generarHijos(estado): 
	global costo #Variable global que cuenta el costo


	columnaVacia=-1 #Bandera que detecta una columna vacia
	reinasTablero=[] #lista donde se almacenan las posiciones de las reinas que ya esta en el tablero
	hijos=[] #lista que va a guardar a los hijos generados
		

	#Se examinan todas las columnas para encontrar las posiciones de todas las reinas que ya están en
	#el tablero
	#------------------------------------------------------------------------------------------------
	reina=0	#Bandera que detecta si hay una reina en una columna
	for i in range(numeroDeReinas):

		
		#se examina toda una columna, si hay alguna reina se agrega su posición a la lista de reinas 
		#y se activa la bandera	
		for j in range(numeroDeReinas):
			if estado[j][i]==1:
				reinasTablero.append([i,j])
				reina=1


		#Significa que no hay ninguna reina en esa columna
		if reina == 0: 
			columnaVacia=i #se guarda el número de la columna vacia

		reina=0	#se reinicia la bandera para recorrer la siguiente columna
	#-------------------------------------------------------------------------------------------------

	#En este punto ya se examinó todo el tablero
	
	#columnaVacia almaceno el número de la columna vacia más a la derecha y si es -1 significa que no
	#hay ninguna columna vacia


	if columnaVacia==-1:
		return hijos 	#Retorna una lista vacia debido a que no hay hijos
	


	#En esta parte se verifican los estados hijos
	#utilizando las posiciones de las reinas que ya están en el tablero se verifica si son estados posibles
	#Si son posibles se agregan a la lista de los hijos
	#------------------------------------------------------------------------------------------------------
	bandera=0	#bandera que se activa cuando no es posible poner una reina en esa posición
	for i in range(numeroDeReinas):
		
		#Recorre a todas las reinas que se encuentran en el tablero
		#-----------------------------------------------------------------------------------------
		for r in reinasTablero:

			#Se verifica el renglón
			if i==r[1]:
				bandera=1
				break	#Se sale del for debido a que hay una reina en ese renglón

			
			#Se verifican diagonales calculando para la nueva reina y para la que ya se encuentra en el tablero
			#columna-(posición en la columna) y columna+(posición en la columna)
			
			diagonalN1=columnaVacia-i 
			diagonal1=r[0]-r[1]
			
			diagonalN2=columnaVacia+i 	
			diagonal2=r[0]+r[1] 	

			#Si alguna condición se cumple significa que están el diagonal
			if diagonalN1==diagonal1 or diagonalN2==diagonal2:	
				bandera=1
				break	#se sale del for debido a que hay una reina en diagonal
		#----------------------------------------------------------------------------------------------

		costo=costo+1#El costo se aumenta cada vez que se genera un hijo aunque no sea un estado posible
		
		if bandera==0: #Signifca que verifico a todas las reinas y no hay problema con ninguna

			nuevoEstado=copy.deepcopy(estado) #Se copia el estado padre
			nuevoEstado[i][columnaVacia]=1 #Se agrega a la reina

			hijos.append(nuevoEstado)	#Se agrega al nuevo estado a la columna de estados
		
		bandera=0 #Se cambia la bandera a 0 para crear al siguiente hijo
	#-----------------------------------------------------------------------------------------------------------------


	return hijos 	#Se retornan los hijos generados
#--------------------------------------------------------------------------------------------------------------------

main() #Se manda a llamar a la función principal
