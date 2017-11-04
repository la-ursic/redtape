print ("Multiplo de dos")
counter = 0
for i in range(1,100):
	if i % 2 == 0:
		counter = counter + 1

print (counter)

print ("Acumulador")
accumulate = 0
for i in range(1,5):
	print (i)
	accumulate = accumulate + i
print(accumulate)

print ("1 al 10 000, impresos")
for i in range (1,10001):
	print (i)

print ("Pares del 1 al 10 000, impresos")
for i in range (1,10001):
	if i % 2 == 0:
		print(i)

print("Tell me where the third E is")
elefante = "ELEFANTE"
counter = 0
eCounter = 0
for i in elefante:
	counter = counter + 1
	if i == "E":
		eCounter = eCounter + 1
	if eCounter == 3:
		print ("encontré la tercera 'E' en la posición", counter)

print ("Cart rules implementation")
itemsInCart = int(input("¿Cuantos productos desea comprar, joven? \n"))
itemPrice = int(input("¿Cuanto cuesta este producto? \n"))
if itemsInCart > 5:
	grandTotal = (itemPrice * itemsInCart) * 0.95
else:
	grandTotal = (itemsInCart * itemPrice)
print ("El precio total de su compra es de", grandTotal)

print("Contador de pares e impares")
userInputs = int(input("Ingresa el numero de valores que desees introducir"))
if userInputs < 1:
	print("Imposible")
else:
	evenNumbers = 0
	for i in range (1,userInputs):
		in = 