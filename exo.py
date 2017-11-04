x = 4
y = 9
z = 15

suma = x + y + z
print (suma)

dos = ((x + y) // z)
print (dos)

tres = x * y + z
print (tres)

cuatro = z % x
print (cuatro)

cinco = y **2
print (cinco)

seis = (x **2) / (y + z)
print (seis)

siete = (z / x) - (z // x)
print (siete)

if (z // x) < (z / x):
	siete = (z / x) - (z // x)
else:
	siete = - (((z // x) - (z / x)) - 1)
print (siete)

monto_en_mxn = 300
un_mxn_en_usd = 19.22
monto_en_usd = monto_en_mxn / un_mxn_en_usd
print (monto_en_usd)

temp_en_f = 200
temp_en_c = (temp_en_f - 32) / 1.8
print (temp_en_c)



