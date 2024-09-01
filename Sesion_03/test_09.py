"""Listas de Python"""

"""Listas (copy): Obtenemos todos lo valores de una lista en otra variable"""

var_1 =["SQLServer", "RDS", "MMYSQL", "PostgreSQL", "MariaDB"]

var_2 = var_1.copy()

print("El valor de mi var_2 es: {}".format(var_2))

var_2.append("SQLite3")
print
