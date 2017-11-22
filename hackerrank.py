import arrow

def numeros_primos(lista_usuario: list):
	lista_primos = []
	for num in range(2,101):
		if all(num%i!=0 for i in range(2,num)):
			lista_primos.append(num)
	return(lista_primos)
	if (lista_primos) == lista_usuario:
		return True
	else:
		return False
numeros_primos(lista_usuario)

#Calcular el área de un triángulo equilátero de 5mts de altura y 10.3 mts de base
def area_triangulo(area_usuario: float):
	altura = 5
	base = 10.3
	area = altura * base / 2
	return (area)
	if area == area_usuario:
		return True
	else:
		return False
area_triangulo(area_usuario)

#Cual es la palabra más larga y la más corta y cuántas letras tienen “Electroencefalografista”,”Electrodoméstico” , “Arteriosclerosis”,”Otorrinolaringólogo”
def respuesta_usuario(mas_larga_usuario: str, mas_corta_usuario: str, length_usuario: list):
	palabras = ['Electroencefalografista','Electrodoméstico','Arteriosclerosis','Otorrinolaringólogo']

	length_palabras = []
	for i in palabras:
		length_palabras.append(len(i))
	return(length_palabras)

	mas_larga_numero = max(length_palabras)
	index_mas_larga = length_palabras.index(mas_larga_numero)
	mas_larga = palabras[index_mas_larga]
	return(mas_larga)

	mas_corta_numero = min(length_palabras)
	index_mas_corta = int(length_palabras.index(mas_corta_numero))
	mas_corta = palabras[index_mas_corta]
	return(mas_larga)

	lista_correcta = [mas_larga,mas_corta,length_palabras]

	if lista_correcta == [mas_larga_usuario,mas_corta_usuario,length_usuario]:
		return True
	else:
		return False

respuesta_usuario(mas_larga_usuario, mas_corta_usuario, length_usuario)


'''
#Cuales son palabras palíndromas? -Anita lava la tina, -A mi me mima, - Mi mama masa la masa en la mesa
primera = 
'''
#En el año 2009 viajé a Europa y a Estados Unidos. Voy a Europa cada 5 años y a Estados Unidos cada 2 años. ¿Cuál será el próximo año que realizaré ambos viajes?
def siguiente_viaje(siguiente_ano):
	frecuencia_usa = 2
	frecuencia_europa = 5
	viaje_ambos = 2009
	siguiente_viaje = frecuencia_europa * frecuencia_usa + viaje_ambos
	if siguiente_viaje_usuario == siguiente_viaje:
		return True
	else:
		return False
siguiente_viaje(siguiente_viaje_usuario)

#Tengo 1 ½ litros de leche para servir en vasitos de  1/8 litro cada uno, la misma cantidad de leche en cada vasito. ¿Cuántos vasitos necesito?
def vasitos_necesarios(vasitos):	
	cantidad_leche = 1.5
	capacidad_vasitos = 0.125
	necesidad_vasitos = cantidad_leche / capacidad_vasitos
	if necesidad_vasitos_usuario == necesidad_vasitos:
		return True
	else:
		return False
vasitos_necesarios()

#Una piscina olímpica de 2,5 millones de litros de agua está llena al 95% de su capacidad. Se calcula que se evaporará una cantidad de agua correspondiente al 5% de su capacidad total. Calcular cuántos litros se van a evaporar.
def agua_evaporada(capacidad):
	capacidad_total = 2500000 / 0.95
	litros_a_evaporar = int(capacidad_total * 0.05)
	if litros_usuario == litros_a_evaporar:
		return True
	else:
		return False
agua_evaporada()

#¿Cuál es la respuesta a El sentido de la vida, el universo y todo lo demás?
def sentido_vida(sentido):
	sentido_correcto = 42
	if respuesta_usuario = sentido_correcto:
		return True
	else:
		return False
sentido(sentido_usuario)

#La fecha y hora actual de Bucarest, Rumania con formato ‘YYYY-MM-DD HH:mm’
def hora_en_bucarest(hora)
	without_format = arrow.now('Europe/Bucharest')
	with_format = without_format.format('YYYY-MM-DD HH:mm')
	if hora_usuario == with_format:
		return True
	else:
		return False
hora_en_bucarest(hora_usuario)
