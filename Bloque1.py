#!/usr/bin/python
#hacen paro de correr esta mierda plox?
import math#el problema que les da es por que no importan este pedo morros

#tabla de distribucion de frecuencias
print("Datos ordenados")
#obtenemos el tamaño del vector
tama = int(input("digite la cantidad de datos que va a ingresar"))
datos = [0]*tama #creamos el vector de la cantidad que tiene la variable tama	
i= 0
print ("ingrese sus datos")
while i < tama:
	datos[i]=int (input ("dato: "))
	i+=1
#comienza metodo de ordenacion por seleccion
i=0
while i < tama:
	mayor= i
	j=i+1
	y=0
	while j < tama:
	    if datos[mayor]<datos[j]:
	        mayor = j
	    j+=1
	aux = datos[mayor]
	datos[mayor]=datos[i]
	datos[i]=aux
	i+=1
	  
print("estos son sus datos ordenados decendentemente")
print(datos)
m = ceil(1 + 3.3*log10(tama))
r = datos[0]-datos[tama-1]
a= ceil(r/m)-0.1
print("------------------------------------------")
print("------------------------------------------")
print("---------------Respuestas-----------------")


print("m = ",m," R= ",r," A = ",a)

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

def DistribucionF():
	
	items=int(input("Dame le numero de items a ingresar"))
	datos=[0]*items
	tem_list=[]
	frecuencia=[0]*items
	suma=0

	i=0
	print("ingresa Los datos y la Frecuencia:")
	while i<items:
		tem_list.append(input("Dato: "))
		frecuencia[i]=int(input("Frecuencia: "))
		i+=1

	i=0
	
	for x in range(0,len(frecuencia)):
		suma+=frecuencia[i]
		i+=1

	print("\tTabla de Frecuencia\n Dato\t\tFrecuencia\tPorcentaje")
	i=0
	while i<items:
		porcentaje=((frecuencia[i]*100)/suma)
		
		print(tem_list[i],"\t\t",frecuencia[i],"\t\t",porcentaje,"%")

		i+=1
	print("Total","\t\t",suma,"\t\t","100%")
		



#para hacer los algoritmos que faltan utilizaremos este pedo?
#necesito que alguien de grafico lo revise y me diga 
#http://unamatematicaseltigre.blogspot.mx/2014/05/tecnicas-de-visualizacion-de-datos-ser.html














