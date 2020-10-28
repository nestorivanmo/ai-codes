#Autor: Pedraza Martínez José Alberto
#Fecha 22/10/2020
#Descripción: Resulve el problema de las 8 reinas

import copy #libreria para realizar la copia de una lista

costo = 1	#Es la variable que cuenta el costo y es global para que las funciones recursivas lo aumenten
respuestas=1	#variable que cuenta las respuestas

numeroDeReinas=9


def creaMatriz(n,m):
	matriz = []
	for i in range(n):
		a = [0]*m
		matriz.append(a)
	return matriz



estado=creaMatriz(numeroDeReinas,numeroDeReinas)
#estado=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]	#estado inicial

def main():	#Función principal
	
	global numeroDeReinas

	global estado




	resolver(estado,0)	#Se manda a llamar a la función que resuleve el problema // se le manda 0 debido a que no hay ninguna reina en el tablero

	print("costo: ",costo)	#Al terminar imprime el costo

def resolver(estado,nivel):
	global costo	#Se toma la variable global para tomar el costo de todas las llamadas a la función
	global respuestas 
	costo = costo+1

	if nivel==numeroDeReinas:	#Si se llega al nivel 8 significa que llego a una respuesta
		print("Respuesta:",respuestas) #Se imprime el número de respuestas
		respuestas=respuestas+1		#Aumenta la variable que cuenta las respuestas
		
		for i in range(numeroDeReinas):	
			print(estado[i])
		return 1
	hijos = generarHijos(estado)

	if hijos==[]:	#No se generaron hijos
		return 0	#regresa 0 para terminar la función
	
	for hijo in hijos:
		resolver(hijo,nivel+1)
	return 0

def generarHijos(estado):	#Función para generar hijos
	
	columnaVacia=-1		#Se inicializa la variable de la columna vacia en -1
	reinasTablero=[]	#lista donde se almacenan las posiciones de las reinas que ya esta en el tablero
	hijos=[]	#lista que va a guardar a los hijos generados
		
	
	reina=0		#Bandera que detecta si hay una reina en una columna

	for i in range(numeroDeReinas): #indica en que columna se encuentra

		for j in range(numeroDeReinas):#indica en que posición de la columna se encuentra

			if estado[j][i]==1:	#Significa que en la posición actual hay una reina

				reinasTablero.append([i,j])	#Se agrega la reina que se encontro a la lista de reinas
				reina=1
		
		if reina == 0:	#Significa que se recorrio toda la columna y no encontro ninguna reina
			columnaVacia=i #se guarda el número de la columna vacia

		reina=0	#se reinicia la bandera para recorrer la siguiente columna


	if columnaVacia==-1:	#Significa que recorrio todo el tablero y no hay ninguna columna vacia
		return hijos 	#Retorna una lista vacia debido a que no hay hijos
	
	bandera=0	#bandera que se activa cuando no es posible poner una casilla en esa posición
	
	for i in range(numeroDeReinas):	#Va a ir moviendo a la nueva reina en la columna
		
		for r in reinasTablero:	#Recorre a todas las reinas que se encuentran en el tablero
			
			if i==r[1]:	#Significa que la reina esta en el mismo renglón que la posición actual
				bandera=1	#se activa la bandera
				break	#Se sale del for debido a que hay una reina en ese nivel
			
			#Si los números son iguales están en la misma diagonal
			diagonalN1=columnaVacia-i #calcula columna-(posición en la columna)
			diagonal1=r[0]-r[1]		#calcula columna-(posición en la columna)

			#Si los números son iguales están en la misma diagonal
			diagonalN2=columnaVacia+i 	#calcula columna+(posición en la columna)
			diagonal2=r[0]+r[1] 	#calcula columna+(posición en la columna)

			if diagonalN1==diagonal1 or diagonalN2==diagonal2:	#Significa que que la reina se encuentra en diagonal con la posición actual
				bandera=1	#se activa la bandera debido a que no es posible esa posición
				break	#se sale del for debido a que hay una reina en diagonal
		
		if bandera==0: #Signifca que verifico a todas las reinas y no hay problema con ninguna

			nuevoEstado=copy.deepcopy(estado) #Se copia el estado padre
			nuevoEstado[i][columnaVacia]=1 #Se agrega a la reina

			hijos.append(nuevoEstado)	#Se agrega al nuevo estado a la columna de estados

		bandera=0 #Se cambia la bandera a 0 para crear al siguiente hijo

	return hijos 	#Se retornan los hijos generados

main()	#Se manda a llamar a la función principal
