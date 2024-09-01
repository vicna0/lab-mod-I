"""Diccionario en Python"""

"""del: elimina un key y valor del diccionario"""

var_1 = {"nombre": "Matias", "edad": 26, "promedio":14}

"""Para eliminar valores de nuestro diccionario usammos a del, delante de la variable"""

var_1["distrito"] = "lince"
del var_1["edad"]
del var_1["promedio"]

print("El diccionario actualizado tiene los siguientes valores: {}".format(var_1))
