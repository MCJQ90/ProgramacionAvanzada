"""Calculadora de Maria Jaramillo"""
print("""                   Bienvenidos
      Estás utilizando la calculadora creada por
                 María Jaramillo""")
Num1 = input("Ingresa el primer número: ")
Num1 = int(Num1)
Num2 = input("Ingresa el segundo número: ")
Num2 = int(Num2)

SUMA = Num1 + Num2
RESTA = Num1 - Num2
MULTIPLICACION = Num1 * Num2
DIVISION = Num1 / Num2

Operador = input("Digite el operador (+, -, *, /) con el que desea trabajar: ")

if Operador == "+":
    print(SUMA)
elif Operador == "-":
    print(RESTA)
elif Operador == "*":
    print(MULTIPLICACION)
elif Operador == "/":
    print(DIVISION)
