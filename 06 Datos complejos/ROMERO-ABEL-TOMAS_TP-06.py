# Actividad 1
lista_numeros = list(range(4, 101, 4))
print(lista_numeros)


# Actividad 2
nombres_gatos = ["Gordo", "Misi", "Tao", "Blanquito", "Grisesito"]
print(nombres_gatos[-2])


# Actividad 3
lista_vacia = []
lista_vacia.append("Python")
lista_vacia.append("Java")
lista_vacia.append("C#")
print(lista_vacia)


# Actividad 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)


# Actividad 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

"""
Explicación:
    1. Primero la lista números contiene 5 elementos, en este caso números: [8, 15, 3, 22, 7]
    2. Luego se usa "remove" para eliminar el elemento máximo de la lista con la función "max", que sería el número 22
    3. Luego imprime la lista modificada, sin el número 22, ya que ese número era el máximo.
"""


# Actividad 6
lista_numeros2 = list(range(10, 31, 5))
print(lista_numeros2[:2])


# Actividad 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = "monopatín", "monociclo"
print(autos)


# Actividad 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)


# Actividad 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)


# Actividad 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
