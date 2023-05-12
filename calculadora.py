# Funcion para sumar
def suma(num1, num2):
    return num1 + num2

# Funcion para restar
def resta(num1, num2):
    return num1 - num2

# Funcion para multiplicar
def multiplicacion(num1, num2):
    return num1 * num2

# Funcion para dividir
def division(num1, num2):
    return num1 / num2

# Menu de opciones
print("Selecciona una operacion:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

# Solicitar opcioin al usuario
opcion = int(input("Ingresa tu opcion (1/2/3/4): "))

# Solicitar dos numeros al usuario
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

# Realizar la operacion seleccionada
if opcion == 1:
    print(num1, "+", num2, "=", suma(num1, num2))

elif opcion == 2:
    print(num1, "-", num2, "=", resta(num1, num2))

elif opcion == 3:
    print(num1, "*", num2, "=", multiplicacion(num1, num2))

elif opcion == 4:
    print(num1, "/", num2, "=", division(num1, num2))

else:
    print("Opcion invalida")
