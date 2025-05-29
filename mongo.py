from pymongo import MongoClient

def connect_to_mongo():
    """
        Este metodo se conecta a mongo
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client['JLcontador']
    return db['clientes']

def add_user():
    print("\nAgregar Cliente: ")
    print("\nTipo de identificación: ")
    print("1. Cédula")
    print("2. RUC")

    while True:
        opcion = input("\nSeleccione el número según el tipo de identifación:  ")
        if opcion == "1":
            tipoId = "Cédula"
            break
        elif opcion == "2":
            tipoId = "RUC"
            break
        else:
            print("Ingrese una opción válida")

    while True:
        Idcliente = input("Inserte numero de identificación: ")
        
        if tipoId == "Cédula":
            if Idcliente.isdigit() and len(Idcliente) == 10:
                break
            else:
                print("La cédula debe tener 10 dígitos")
        elif tipoId == "RUC":
            if Idcliente.isdigit() and len(Idcliente) == 13 and Idcliente.endswith("001"):
                break
            else:
                print("El RUC debe tener 13 dígitos y terminar en 001")

    nombre = input("Nombres: ")
    apellido = input("Apellidos: ")
    direccion = input("Dirección: ")
    
    while True:
        celular = input ("Celular: ")
        if celular.isdigit() and len(celular) == 10:
            break
        else:
            print("El celular debe tener 10 dígitos")

    while True:
        email = input("Correo: ")
        if "@" in email and "." in email:
            break
        else:
            print("Ingrese un correo válido ejemplo: usuario@dominio.com")
    
    while True:
        print("Tipo de contribuyente: ")
        print("1. Regimen General")
        print("2. Regimen Rimpe Emprendedor")
        print("3. Regimen Rimpe Negocio Popular")
        opcion = input("\nSeleccione el número según el tipo de contribuyente:  ")

        if opcion == "1":
            tipoContribuyente = "Regimen General"
            break
        elif opcion == "2":
            tipoContribuyente = "Regimen Rimpe Emprendedor"
            break
        elif opcion == "3":
            tipoContribuyente = "Regimen Rimpe Negocio Popular"
        else:
            print ("Ingrese un numero valido")

    actividadEconomica = input("Actividad Economica:")
            
    cliente = {
        "tipo id": tipoId,
        "idcliente": Idcliente,
        "nombre": nombre,
        "apellido": apellido,
        "direccion": direccion,
        "ceular": celular,
        "email": email,
        "tipo de contribuyente": tipoContribuyente,
        "actividad economica": actividadEconomica
    }

def list_user():
    print("LISTA")

def main():
    coleccion = connect_to_mongo()

    while True:
        print("MENU")
        print("1. Agregar Cliente")
        print("2. Listar Clientes")
        print("3. Salir")

        opcion = input("Seleccione una opción:  ")
        if opcion == "1":
            add_user()
        elif opcion == "2":
            list_user()
        elif opcion == "3":
            print("Saliendo del programa")
            break
        else:
            print("Ingrese una opción válida") 

if __name__ == "__main__":
    main()
