# Actividad 1
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

print(factorial(5))

# Actividad 2
def fibonacci(posicion):
    if posicion == 0:
        return 0
    if posicion == 1:
        return 1
    return fibonacci(posicion-1) + fibonacci(posicion-2)

num = int(input("Ingrese un número: "))
for i in range(num):
    print(fibonacci(i))


# Actividad 3
def potencia(base, exponente):
    if exponente == 0:
        return 0
    if exponente == 1:
        return base
    return base * potencia(base, exponente-1)

print(potencia(3, 2))


# Actividad 4
def binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return binario(n // 2) + str(n % 2)

print(binario(12))


# Actividad 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    return False

print(es_palindromo("neuquen"))


# Actividad 6
def suma_digitos(n):
    if n < 10:
        return n
    ultimo_digito = n % 10
    resto_numero = n // 10
    return ultimo_digito + suma_digitos(resto_numero)

print(suma_digitos(12022023))


# Actividad 7
def contar_bloques(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + contar_bloques(n-1)

print(contar_bloques(12))


# Actividad 8
def contar_digito(numero, digito):
    if numero == 0 and digito == 0:
        return 1
    if numero == 0:
        return 0

    ultimo = numero % 10
    resto = numero // 10
    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    else:
        return contar_digito(resto, digito)

print(contar_digito(122124, 2))
