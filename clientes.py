from pymongo import MongoClient

def connect_to_mongo():
    """
        Este metodo se conecta a mongo
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client['JLcontador']
    return db['clientes']

def add_user(coleccion):
    """
        Este metodo agrega un cliente a la base de datos
    """
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
        "celular": celular,
        "email": email,
        "tipo de contribuyente": tipoContribuyente,
        "actividad economica": actividadEconomica
    }

    coleccion.insert_one(cliente)
    print("\nCliente agregado correctamente")

def list_user(coleccion):
    """
        Este metodo lista los clientes de la base de datos
    """
    print("\nLISTA de clientes: ")
    clientes = coleccion.find()
    for cliente in clientes:
        print("\n------------------------------")
        print(f"ID: {cliente['idcliente']}")
        print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
        print(f"Tipo ID: {cliente['tipo id']}")
        print(f"Dirección: {cliente['direccion']}")
        print(f"Celular: {cliente['celular']}")
        print(f"Email: {cliente['email']}")
        print(f"Tipo de Contribuyente: {cliente['tipo de contribuyente']}")
        print(f"Actividad Económica: {cliente['actividad economica']}")
        print("------------------------------")
        
def buscar_user(coleccion):
    """
        Este método permite buscar un cliente por número de identificación
    """
    print("\nBuscar Cliente:")
    id_buscar = input("Ingrese el número de identificación del cliente: ")

    cliente = coleccion.find_one({"idcliente": id_buscar})

    if cliente:
        print("\n--- Cliente encontrado ---")
        print(f"ID: {cliente['idcliente']}")
        print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
        print(f"Tipo ID: {cliente['tipo id']}")
        print(f"Dirección: {cliente['direccion']}")
        print(f"Celular: {cliente['celular']}")
        print(f"Email: {cliente['email']}")
        print(f"Tipo de Contribuyente: {cliente['tipo de contribuyente']}")
        print(f"Actividad Económica: {cliente['actividad economica']}")
        print("------------------------------")
    else:
        print("\n Cliente no encontrado.")    

def main():
    coleccion = connect_to_mongo()

    while True:
        print("MENU")
        print("1. Agregar Cliente")
        print("2. Listar Clientes")
        print("3. Buscar Cliente")
        print("4. Salir")

        opcion = input("Seleccione una opción:  ")
        if opcion == "1":
            add_user(coleccion)
        elif opcion == "2":
            list_user(coleccion)
        elif opcion == "3":
            buscar_user(coleccion)
        elif opcion == "4":
            print("Saliendo del programa")
            break
        else:
            print("Ingrese una opción válida") 

if __name__ == "__main__":
    main()
