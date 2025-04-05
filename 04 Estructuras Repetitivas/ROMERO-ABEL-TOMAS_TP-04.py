# Actividad 1
for i in range(0, 101):
    print(i)


# Actividad 2
num = int(input("Ingrese un número entero: "))
num_length = len(str(abs(num)))

if num_length >= 2:
    print(f"El número {num} contiene {num_length} dígitos.")
elif num_length == 1:
    print(f"El número {num} contiene un dígito.")
else:
    print("El número no tiene dígitos.")


# Actividad 3
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

suma = 0
for i in range(num1 + 1, num2):
    suma += i
print(f"La suma total de los números entre {num1} y {num2} (ambos excluidos) es: {suma}")


# Actividad 4
suma_nums = 0
while True:
    nums = int(input("Ingrese un número entero (0 para salir): "))
    if nums == 0:
        break
    suma_nums += nums

print(f"La suma total de los números ingresados es: {suma_nums}")


# Actividad 5
import random

num_aleatorio = random.randint(0, 9)
intentos = 0

while True:
    eleccion = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if eleccion < 0 or eleccion > 9:
        print("Por favor, ingresa un número entre 0 y 9.")
        continue
    if eleccion == num_aleatorio:
        print(f"El número era el {num_aleatorio}, lo haz adivinado en {intentos} intentos.")
        break


# Actividad 6
for i in range(100, 0, -2):
    print(i)


# Actividad 7
num_final = int(input("Ingrese un número entero positivo: "))
suma_total = 0

if num_final <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    for i in range(0, num_final + 1):
        suma_total += i
    print(f"La suma total de los números entre 0 y {num_final} es: {suma_total}")


# Actividad 8
total, suma_pares, suma_impares, suma_positivos, suma_negativos = 0, 0, 0, 0, 0

while True:
    numeros = int(input("Ingrese 100 números enteros: "))
    total += 1
    if numeros % 2 == 0:
        suma_pares += 1
    else:
        suma_impares += 1

    if numeros > 0:
        suma_positivos += 1
    else:
        suma_negativos += 1

    if total == 100:
        break

print(f"Cantidad de números pares: {suma_pares}")
print(f"Cantidad de números impares: {suma_impares}")
print(f"Cantidad de números positivos: {suma_positivos}")
print(f"Cantidad de números negativos: {suma_negativos}")


# Actividad 9
suma_de_numeros = 0
cantidad = 0

while True:
    nums = int(input("Ingrese 100 números enteros: "))
    suma_de_numeros += nums
    cantidad += 1
    if cantidad == 100:
        break

media = suma_de_numeros / cantidad
print(f"La media de los números ingresados es: {round(media, 2)}")


# Actividad 10
num_normal = int(input("Ingrese un número entero: "))
num_invertido = 0
es_negativo = num_normal < 0
num_normal = abs(num_normal)

while num_normal > 0:
    digito = num_normal % 10
    num_invertido = num_invertido * 10 + digito
    num_normal //= 10

if es_negativo:
    num_invertido = -num_invertido

print(f"El número invertido es: {num_invertido}")
