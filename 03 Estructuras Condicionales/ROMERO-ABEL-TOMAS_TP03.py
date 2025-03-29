import random
from statistics import mode, median, mean

# Actividad 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


# Actividad 2
nota = int(input("Ingrese la nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# Actividad 3
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Has ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# Actividad 4
edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario >= 0 and edad_usuario < 12:
    print("Categoría: Niño/a")
elif edad_usuario >= 12 and edad_usuario < 18:
    print("Categoría: Adolescente")
elif edad_usuario >= 18 and edad_usuario < 30:
    print("Categoría: Adulto/a joven")
elif edad_usuario >= 30:
    print("Categoría: Adulto/a")
else:
    print("Edad no válida")


# Actividad 5
password = input("Introduce la contraseña: ")
if len(password) >= 8 and len(password) <= 14:
    print("Has ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


# Actividad 6
# Arriba están las importaciones para esta actividad
numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]
print("Lista de números aleatorios:", numeros_aleatorios)

mode_value = mode(numeros_aleatorios)
median_value = median(numeros_aleatorios)
mean_value = mean(numeros_aleatorios)

print(f"- Moda: {mode_value}")
print(f"- Mediana: {median_value}")
print(f"- Media: {mean_value}")

if mode_value == median_value and median_value == mean_value:
    print("Sin sesgo")
elif mean_value > median_value and median_value > mode_value:
    print("Sesgo a la derecha")
elif mean_value < median_value and median_value < mode_value:
    print("Sesgo a la izquierda")
else:
    print("Distribución normal")


# Actividad 7
frase = str(input("Ingrese una frase: "))
if frase[-1] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
    print(f"{frase}!")
else:
    print(frase)


# Actividad 8
nombre_usuario = str(input("Ingrese su nombre: "))
print("""
    Opciones:
    1. Si quiere su nombre en mayúsculas.
    2. Si quiere su nombre en minúsculas.
    3. Si quiere su nombre con la primera letra en mayúscula.
    """)
opcion = int(input("Ingrese una opción (1-3): "))
if opcion == 1:
    print(f"1. Su nombre en mayúsculas es: {nombre_usuario.upper()}")
elif opcion == 2:
    print(f"2. Su nombre en minúsculas es: {nombre_usuario.lower()}")
elif opcion == 3:
    print(f"3. Su nombre con las primeras letras en mayúsculas es: {nombre_usuario.title()}")
else:
    print("Opción no válida")


# Actividad 9
magnitud_terremoto = float(input("Ingrese la magnitud del terremoto: "))
if magnitud_terremoto >= 0.1 and magnitud_terremoto < 3:
    print("Muy leve (imperceptible)")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("Muy fuerte (puede causar daños significativos")
elif magnitud_terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Magnitud no válida")


# Actividad 10
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

if hemisferio == "N" or hemisferio == "S":
    if (mes == 12 and 21 <= dia <= 31) or (mes == 1 and 0 < dia <= 31) or (mes == 2 and 0 < dia <= 29) or (mes == 3 and 0 < dia <= 20):
        estacion = "Invierno" if hemisferio == "N" else "Verano"
    elif (mes == 3 and 21 <= dia <= 31) or (mes == 4 and 0 < dia <= 30) or (mes == 5 and 0 < dia <= 31) or (mes == 6 and 0 < dia <= 20):
        estacion = "Primavera" if hemisferio == "N" else "Otoño"
    elif (mes == 6 and 21 <= dia <= 30) or (mes == 7 and 0 < dia <= 31) or (mes == 8 and 0 < dia <= 31) or (mes == 9 and 0 < dia <= 20):
        estacion = "Verano" if hemisferio == "N" else "Invierno"
    elif (mes == 9 and 21 <= dia <= 30) or (mes == 10 and 0 < dia <= 31) or (mes == 11 and 0 < dia <= 30) or (mes == 12 and 0 < dia <= 20):
        estacion = "Otoño" if hemisferio == "N" else "Primavera"
    else:
        estacion = None
    
    if estacion:
        print(f"Se encuentra en {estacion}.")
    else:
        print("Fecha no válida")
else:
    print("Hemisferio no válido")
