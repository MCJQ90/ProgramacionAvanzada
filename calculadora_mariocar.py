"""Calculadora de Maria Jaramillo"""
print("""                   Bienvenidos
      Estás utilizando la calculadora creada por
                 María Jaramillo""")
salir = False
while not salir:
    """
        De esta forma mientras salir sea False sigue el bucle
    """
    while True:
        try:
            Num1 = input("Ingresa el primer número: ")
            Num1 = float(Num1)
            break
        except ValueError:
            print("\nIngrese un número válido")
    while True:
        try:
            Num2 = input("Ingresa el segundo número: ")
            Num2 = float(Num2)
            break
        except ValueError:
            print("\nIngrese un número válido")

    SUMA = Num1 + Num2
    RESTA = Num1 - Num2
    MULTIPLICACION = Num1 * Num2
    try:
        DIVISION = Num1 / Num2
    except ZeroDivisionError:
        DIVISION = "No es posible dividir para cero"

    while True:
        print("\nOpciones:")
        print("Sumar =  +")
        print("Restar =  -")
        print("Multiplicar =  *")
        print("Dividir = /")
        print("Ingresar nuevos numeros: Nuevo")
        print("Salir = Salir")
        Operador = input("\nElija una opción: ")

        if Operador == "+":
            print("\nEl resultado de la suma es: ", SUMA)
        elif Operador == "-":
            print("\nEl resultado de la resta es: ", RESTA)
        elif Operador == "*":
            print("\nEl resultado de la multiplicacion es: ", MULTIPLICACION)
        elif Operador == "/":
            print("\nEl resultado de la division es: ", DIVISION)
        elif Operador == "Nuevo":
            break
        elif Operador == "Salir":
            print("\nSaliendo del sistema")
            salir = True 
            """Cambiamos la variable para salir del bucle"""
            break
        else:
            print("\ningrese una opcion valida")