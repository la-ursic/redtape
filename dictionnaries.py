dictionnary = {'name': 'Carlos', 'age': 22, 'programming_languages': ['Python', 'Flask']}
print(dictionnary['name'])
print(dictionnary['programming_languages'])

dic = dict(nombre='Nestor',apellido='Juarez')
print(dic)

print("___________________")
for key,value in dictionnary.items():
	print(key + " " + str(value))

print("___________________")
print("Cuántos elementos tiene el diccionario?")
print(len(dictionnary))

print("___________________")
print("Cuáles son todas las llaves del diccionario?")
print(dictionnary.keys())

print("___________________")
print("Cuáles son todos los valores del diccionario?")
print(dictionnary.values())

print("___________________")
print("?")
print(dictionnary.get("nombree","JUANITO"))

print("___________________")
print("Inserta un elemento al diccionario")
dictionnary['key'] = 'value'
print(dictionnary)

print("___________________")
print("Quita un elemento del diccionario")
dictionnary.pop('key')
print(dictionnary)

print("___________________")
print("Añade los elementos de un diccionario a otro")
dictionnary.update(dic)
print(dictionnary)

print("___________________")
print("Copia un diccionario")
second_dictionnary = dictionnary.copy()
print(second_dictionnary)


