# Actividad 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)


# Actividad 2
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)


# Actividad 3
lista_frutas = ['Banana', 'Ananá', 'Melón', 'Uva', 'Naranja', 'Manzana', 'Pera']
print(lista_frutas)


# Actividad 4
contactos = {}

print("\nIngresa 5 contactos:")
for i in range(5):
    nombre = str(input(f"Nombre {i+1}: ")).strip()
    telefono = input(f"Teléfono {i+1}: ").strip()
    contactos[nombre] = telefono

nombre = input("\nBuscar contacto: ")
if nombre in contactos:
    print(f"{nombre}: {contactos[nombre]}")
else:
    print("Contacto no encontrado.")


# Actividad 5
frase = input("\nIngresa una frase: ")
palabras = frase.split()

print(f"Palabras únicas: {set(palabras)}")
print("Conteo:", {palabra: palabras.count(palabra) for palabra in set(palabras)})


# Actividad 6
print("\nIngresa los nombres de 3 alumnos:")
alumnos = {}

for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Nota {j+1}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")


# Ejercicio 7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {3, 4, 5, 6, 7}

print(f"\nAmbos: {parcial1.intersection(parcial2)}")
print(f"Solo uno: {parcial1.symmetric_difference(parcial2)}")
print(f"Al menos uno: {parcial1.union(parcial2)}")


# Ejercicio 8
print("\nMenú de Stocks")
stock = {"manzanas": 10, "bananas": 5, "naranjas": 8}

while True:
    producto = input("Producto (o 'salir'): ")
    if producto == 'salir':
        break

    if producto in stock:
        print(f"Stock actual: {stock[producto]}")
        cantidad = int(input("Agregar cantidad: "))
        stock[producto] += cantidad
    else:
        cantidad = int(input("Cantidad inicial: "))
        stock[producto] = cantidad

    print(f"Nuevo stock de {producto}: {stock[producto]}")


# Ejercicio 9
agenda = {
    ("lunes", "09:00"): "Reunión equipo",
    ("martes", "16:00"): "Dentista",
    ("miércoles", "10:30"): "Presentar TP",
    ("jueves", "22:00"): "Jugar partida muy urgente de Rocket League",
    ("viernes", "19:00"): "Clases de Italiano"
}

dia = input("\nDía: ")
hora = input("Hora: ")
evento = agenda.get((dia, hora), "Sin eventos")
print(f"{dia} {hora}: {evento}")


# Ejercicio 10
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo",
    "Chile": "Santiago",
    "Peru": "Lima"
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print(f"\nDiccionario invertido: {capitales_paises}")
