"""Listas de Python"""

"""Listas (del): Elimmina un valor indicando el indice del valor de la lista"""

paises = []
paises.append("Peru")
paises.append("Brasil")
paises.append("Argentina")
paises.append("Canada")
paises.append("España")
paises.append("Colombia")

print("Los valores de mi lista son: {}".format(paises))

del paises[2]
del paises[4]

print("Mi lista actualizada tiene los siguientes valores: {}".format(paises))
