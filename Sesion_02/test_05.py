"""
Requisistos:

1. Crear variables para los valores de nombre, profesion y ciudad
2. Crear 2 variables de remuneracion de enero y febrero
3. Crear 1 variable donde se sumara el ingreso de los meses de enero y febrero
4. Mostar en pantalla el mensaje de

"""
nombre = "briana"
profesion = "genetista y biotecnologo"
ciudad = "lima"

rem_ene = 1500
rem_feb = 2000
rem_tot = format(rem_ene+rem_feb)
print("Hola soy {}, mi profesion es {}, vivo en la ciudad de {} y mi remuneracion total es {}".format(nombre,profesion,ciudad,rem_tot))
