from pymongo import MongoClient

def connect_to_mongo():
    """
    Se conecta a la base de datos MongoDB
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client['JLcontador']
    return db['solicitudes']

def add_solicitud(coleccion_solicitudes, coleccion_clientes):
    """
    Agrega una nueva solicitud de servicio solo si el cliente existe
    y no tiene una solicitud para el mismo año fiscal y servicio
    """
    print("\nAGREGAR SOLICITUD DE SERVICIO")
    idcliente = input("Ingrese número de identificación del cliente: ")

    cliente_existente = coleccion_clientes.find_one({"idcliente": idcliente})

    if not cliente_existente:
        print("\n Cliente no encontrado. Primero registre al cliente antes de generar la solicitud.")
        return

    print("\nServicios disponibles:")
    print("1. Declaración de impuesto a la renta")

    while True:
        opcion = input("Seleccione el servicio (solo opción 1 disponible): ")
        if opcion == "1":
            servicio = "Declaración de impuesto a la renta"
            break
        else:
            print("Opción no válida. Solo está disponible la opción 1.")

    while True:
        try:
            anio = int(input("Ingrese el año fiscal: "))
            if 2000 <= anio <= 2025:
                break
            else:
                print("Ingrese un año válido entre 2000 y 2025.")
        except ValueError:
            print("Debe ingresar un número válido para el año.")

    #  Verificar si ya existe una solicitud para ese cliente, año y servicio
    solicitud_existente = coleccion_solicitudes.find_one({
        "idcliente": idcliente,
        "servicio": servicio,
        "anio_fiscal": anio
    })

    if solicitud_existente:
        print("\n Ya existe una solicitud registrada para este cliente, con el mismo servicio y año fiscal.")
        return

    estado = "Ingresando información"

    solicitud = {
        "idcliente": idcliente,
        "servicio": servicio,
        "anio_fiscal": anio,
        "estado": estado
    }

    coleccion_solicitudes.insert_one(solicitud)
    print("\n Solicitud registrada correctamente.")

def list_solicitudes(coleccion):
    """
    Lista todas las solicitudes registradas
    """
    print("\nLISTA DE SOLICITUDES:")
    solicitudes = coleccion.find()
    for solicitud in solicitudes:
        print("\n------------------------------")
        print(f"ID Cliente: {solicitud['idcliente']}")
        print(f"Servicio: {solicitud['servicio']}")
        print(f"Año Fiscal: {solicitud['anio_fiscal']}")
        print(f"Estado: {solicitud['estado']}")
        print("------------------------------")

def buscar_solicitud(coleccion):
    """
    Busca una solicitud por número de identificación del cliente
    """
    print("\nBUSCAR SOLICITUD:")
    id_buscar = input("Ingrese el número de identificación del cliente: ")

    solicitud = coleccion.find_one({"idcliente": id_buscar})

    if solicitud:
        print("\n--- Solicitud encontrada ---")
        print(f"ID Cliente: {solicitud['idcliente']}")
        print(f"Servicio: {solicitud['servicio']}")
        print(f"Año Fiscal: {solicitud['anio_fiscal']}")
        print(f"Estado: {solicitud['estado']}")
        print("------------------------------")
    else:
        print("\n No se encontró ninguna solicitud para ese cliente.")

def main():
    coleccion_solicitudes = connect_to_mongo()  # solicitudes
    coleccion_clientes = MongoClient('mongodb://localhost:27017/')['JLcontador']['clientes']  # clientes

    while True:
        print("\nMENU - SOLICITUDES DE SERVICIO")
        print("1. Agregar Solicitud")
        print("2. Listar Solicitudes")
        print("3. Buscar Solicitud por Cliente")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            add_solicitud(coleccion_solicitudes, coleccion_clientes)
        elif opcion == "2":
            list_solicitudes(coleccion_solicitudes)
        elif opcion == "3":
            buscar_solicitud(coleccion_solicitudes)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Ingrese una opción válida.")

if __name__ == "__main__":
    main()