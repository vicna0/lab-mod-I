"""Listas de Python"""

lista_1 = ["Briana", 18, "Genestista y biotecnologo"]
lista_2 = ["Mariana", 20, "Ingeneria industrial"]

suma_edades = lista_1[1] + lista_2[1]
print("La suma de las edades es: {}".format(suma_edades))

suma_listas = lista_1 + lista_2
print("La suma de las edades es: {}".format(suma_listas))

lista_1.reverse()
print("Mi lista_1 en reversa es: {}".format(lista_1))

lista_2.reverse()
print("Mi lista_2 en reversa es: {}".format(lista_2))

del lista_1[1]
print("Mi lista_1 actualizada es: {}".format(lista_1))

del lista_2[1]
print("Mi lista_2 actualizada es: {}".format(lista_2))