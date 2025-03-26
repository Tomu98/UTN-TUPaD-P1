"""
Practico 1: Estructuras secuenciales
Alumno: Romero, Abel Tomás
"""


# Actividad 1
print("Hola Mundo!")


# Actividad 2
nombre = str(input("Ingrese su nombre: "))
print(f"Hola {nombre}!")


# Actividad 3
nombre2 = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))
localidad = str(input("Ingrese su localidad: "))
print(f"Soy {nombre2} {apellido}, tengo {edad} años y vivo en {localidad}.")


# Actividad 4
radio = float(input("Ingrese el radio del círculo: "))
area = 3.1416 * radio ** 2
perimetro = 2 * 3.1416 * radio
print(f"El área del círculo es: {round(area, 2)}")
print(f"El perímetro del círculo es: {round(perimetro, 2)}")


# Actividad 5
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos // 3600
print(f"La cantidad de segundos ingresada ({segundos}) es equivalente a {horas} horas.")


# Actividad 6
numero = int(input("Ingrese un número: "))
print(f"La tabla de multiplicar del número {numero} es:")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")


# Actividad 7
num1_act7 = int(input("Ingrese el primer número distinto a 0: "))
num2_act7 = int(input("Ingrese el segundo número distinto a 0: "))
suma = num1_act7 + num2_act7
resta = num1_act7 - num2_act7
multiplicacion = num1_act7 * num2_act7
division = num1_act7 / num2_act7
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


# Actividad 8
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
imc = peso / altura ** 2
print(f"Su índice de masa corporal es: {round(imc, 2)}")


# Actividad 9
celcius = float(input("Ingrese la temperatura en grados Celcius: "))
fahrenheit = 9/5 * celcius + 32
print(f"La temperatura en grados Fahrenheit es: {round(fahrenheit, 2)}")


# Actividad 10
num1_act10 = float(input("Ingrese el primer número: "))
num2_act10 = float(input("Ingrese el segundo número: "))
num3_act10 = float(input("Ingrese el tercer número: "))
promedio = (num1_act10 + num2_act10 + num3_act10) / 3
print(f"El promedio de los números ingresados es: {round(promedio, 2)}")
