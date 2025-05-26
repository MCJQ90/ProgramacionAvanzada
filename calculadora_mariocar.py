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
            Num1 = int(Num1)
            break
        except ValueError:
            print("\nIngrese un número válido")
    Num2 = input("Ingresa el segundo número: ")
    Num2 = int(Num2)

    SUMA = Num1 + Num2
    RESTA = Num1 - Num2
    MULTIPLICACION = Num1 * Num2
    DIVISION = Num1 / Num2

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