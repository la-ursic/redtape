#!usr/bin/python
# -*- coding: utf-8 -*-

#1
w = int(input("Por favor, ingresa el número entero que se te de la chingada gana \n"))
x = int(input("Por favor, vuelve a hacer lo que hiciste en la etapa anterior, pero por favor, sé original...\n"))

y = w // x
z = w / x

if y == z:
	print ("La división de los dos enteros que ingresaste es igual a",y,". Ah, btw, esta división es exacta.")
else:
	print ("La división de los dos enteros que ingresaste es igual a",y,"pero este resultado no es exacto.")

#2
a = int(input("Vamos a hacer otro ejercicio. Escribe un entero de nuevo. Vamos a llamarlo MONKEY.\n"))
b = int(input("Gracias. Ahora escribe otro numero entero, lo llamaremos TURTLE.\n"))

if a == b:
	print ("MONKEY es igual a TURTLE")
elif a > b:
	print ("MONKEY es superior a TURTLE")
else:
	print ("TURTLE es superior a MONKEY")

#3
c = int(input("Ahora, ingresa el año actual.\n"))
d = int(input("Gracias. Ahora escribe el año en el que perdiste tu virginidad.\n"))

e = c - d
f = d - c

if e == 0:
	print ("Este año estamos de fiesta!!")
elif e > 0:
	print ("Llevas",e,"años viviendo en el pecado.")
else:
	print ("Faltan",f,"años para que eso suceda. BE PATIENT, YOUNG JEDI!")

#4
g = int(input("Seguimos. Escribe un entero.\n"))
h = int(input("Gracias. Ahora escribe otro entero.\n"))
i = int(input("Esta es la ultima vez que lo pido. Ingresa un numero entero.\n"))

if g == h and h == i:
	print ("Los tres enteros que ingresaste son iguales. Que original we.")
elif (g == h and h != i) or (g == i and h != i) or (h == i and g != h):
	print ("Ingresaste dos enteros iguales y uno distinto. Yey.")
else:
	print ("Los tres enteros son distintos.")

#5
j = int(input("Seguimos. Escribe un entero.\n"))
k = int(input("Gracias. Ahora escribe otro entero.\n"))
l = int(input("Esta es la penúltima vez que lo pido. Ingresa un número entero.\n"))

if j > k and k > l:
	print (j)
elif k > l:
	print (k)  
else:
	print (l)