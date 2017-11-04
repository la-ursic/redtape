'''
list1 = [1,2,3,4,5,2,32,53,4,333,57,90]
list2 = ["A","B"]
list3 = ["A",1,2,3,4,5,6,7,8,9]
list4 = [list1,list2,list3]
#print(list4)
list1.append(6)
print(list1)
list1.extend([7,8])
print(list1)
list1.insert(2,"melon")
print(list1)
list1.pop(3)
print("POP")
print(list1)

list3.reverse()
print("REVERSE")
print(list3)

print("COUNT")
print(list1.count(333))

print("INDEX")
print(list1.index(333))

print("Let's get this machine to create a 100 hundred var list")
oneHundredList = [1]
for i in range(2,101):
	oneHundredList.append(i)
print (oneHundredList)

tableToBuild = int(input("Now we'll build a multiplication table. Please, enter an integer \n"))
multiplicationTable = [0]
for i in range(1,11):
	multiplicationTable.append(i * tableToBuild)
print(multiplicationTable) 

print("Sum of two lists' elements")
firstList = [4,76,3,12,65,3]
firstListSum = 0
for i in firstList:
	firstListSum = firstListSum + i
secondList = [234,222,523,65]
secondListSum = 0
for i in secondList:
	secondListSum = secondListSum + i
print(firstListSum + secondListSum)

print("Second version of the previous exercise")
firstListB = [4,76,3,12,65,3]
secondListB = [234,222,523,65]
concatenatedList = []
concatenatedList.extend(firstListB)
concatenatedList.extend(secondListB)
print(concatenatedList)
concatenatedListSum = 0
for i in concatenatedList:
	concatenatedListSum = concatenatedListSum + i
print(concatenatedListSum)

print("Hagamos una lista de palabras")
wordCount = int(input("Cuantas palabras quieres que tenga tu lista? \n"))
if wordCount < 1:
	print ("Imposible!")
else:
	words = []
	for _ in range(wordCount):
		words.append(str(input("Ingresa la palabra: ")))
	print(words)

print("Hagamos una lista de palabras - segunda manera")
wordCount = int(input("Cuantas palabras quieres que tenga tu lista? \n"))
if wordCount < 1:
	print ("Imposible!")
else:
	words = [str(input("Ingresa una palabra: ")) for _ in range(wordCount)]
	print(words)

find_word = str(input("que palabra quiere buscar? \n"))
if words.count(find_word) > 0:
	#print("tu palabra aparece" & str(words.count(find_word)) & "veces")
	print("tu palabra aparece {} veces".format(str(words.count(find_word))))
else:
	print("no esta en la lista")
words.index(find_word)
replacement = str(input("porque palabra quieres reemplazar? \n"))
print("porque palabra quieres reemplazar?")
words.insert(words.index(find_word),replacement)
words.remove(find_word)
print(words)
'''

print("Hagamos una lista de palabras en la que se elimina una palabra")
wordCount = int(input("Cuantas palabras quieres que tenga tu lista? \n"))
if wordCount < 1:
	print ("Imposible!")
else:
	words = [str(input("Ingresa una palabra: ")) for i in range(wordCount)]
	print(words)

find_word = str(input("que palabra quiere eliminar? \n"))
if words.count(find_word) > 0:
	for count in range(words.count(find_word)):
		words.remove(find_word)
	print(words)
else:
	print("no esta en la lista")