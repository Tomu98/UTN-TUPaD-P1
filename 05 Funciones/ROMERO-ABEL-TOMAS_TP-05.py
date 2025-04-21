# Actividad 1
def imprimir_hola_mundo():
    return "Hola Mundo!"

print(imprimir_hola_mundo())


# Actividad 2
def saludar_usuario(nombre):
    return f"Hola {nombre.title().strip()}!"

nombre_usuario = str(input("Ingrese su nombre: "))
print(saludar_usuario(nombre_usuario))


# Actividad 3
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

nombre = str(input("Ingrese su nombre: ").title().strip())
apellido = str(input("Ingrese su apellido: ").title().strip())
edad = int(input("Ingrese su edad: "))
residencia = str(input("Ingrese su residencia: ").title().strip())
print(informacion_personal(nombre, apellido, edad, residencia))


# Actividad 4
from math import pi as pi
def calcular_area_circulo(radio):
    area = round(pi * radio ** 2, 2)
    return f"El área del círculo es {area}"

def calcular_perimetro_circulo(radio):
    perimetro = round(2 * pi * radio, 2)
    return f"El perímetro del círculo es {perimetro}"

radio = float(input("Ingrese el radio del círculo: "))
print(calcular_area_circulo(radio))
print(calcular_perimetro_circulo(radio))


# Actividad 5
def segundos_a_horas(segundos):
    horas = segundos // 3600
    return f"{segundos} segundos son {horas} horas."

segundos = int(input("Ingrese el número de segundos: "))
print(segundos_a_horas(segundos))


# Actividad 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero_a_multiplicar = int(input("Ingrese el número a multiplicar: "))
tabla_multiplicar(numero_a_multiplicar)


# Actividad 7
def operaciones_basicas(a, b):
    suma = f"Suma: {a + b}"
    resta = f"Resta: {a - b}"
    multiplicacion = f"Multiplicación: {a * b}"
    division = f"División: {a / b if b != 0 else "Error: división por cero"}"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
print(operaciones_basicas(a, b))


# Actividad 8
def calcular_imc(peso, altura):
    imc = (peso / altura ** 2)
    return f"Su IMC es: {imc:.2f}"

peso = int(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
print(calcular_imc(peso, altura))


# Actividad 9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return f"{celsius}°C equivalen a {fahrenheit:.2f}°F"

celsius = int(input("Ingrese la temperatura en Celsius: "))
print(celsius_a_fahrenheit(celsius))


# Actividad 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return f"El promedio es: {promedio:.2f}"

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
print(calcular_promedio(num1, num2, num3))
