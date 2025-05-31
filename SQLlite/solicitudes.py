import sqlite3

def connect_db():
    return sqlite3.connect('JLcontador.sqlite')

def crear_tabla_solicitudes():
    """
    Crea la tabla solicitudes si no existe
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS solicitudes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            idcliente TEXT,
            servicio TEXT,
            anio_fiscal INTEGER,
            estado TEXT,
            UNIQUE(idcliente, servicio, anio_fiscal)
        )
    """)
    conn.commit()
    conn.close()

def add_solicitud():
    conn = connect_db()
    cursor = conn.cursor()

    id_cliente = input("Ingrese número de identificación del cliente: ")
    cursor.execute("SELECT * FROM clientes WHERE idcliente = ?", (id_cliente,))
    cliente = cursor.fetchone()

    if not cliente:
        print("Cliente no encontrado. Debe registrarlo primero.")
        conn.close()
        return

    servicio = "Declaración de impuesto a la renta"

    while True:
        try:
            anio = int(input("Ingrese el año fiscal: "))
            if 2000 <= anio <= 2025:
                break
            else:
                print("Año inválido.")
        except:
            print("Ingrese un número válido.")

    # Validar duplicado
    cursor.execute("""
        SELECT * FROM solicitudes WHERE idcliente = ? AND servicio = ? AND anio_fiscal = ?
    """, (id_cliente, servicio, anio))
    existente = cursor.fetchone()

    if existente:
        print("Ya existe una solicitud para este año y cliente.")
        conn.close()
        return

    estado = "Ingresando información"
    cursor.execute("""
        INSERT INTO solicitudes (idcliente, servicio, anio_fiscal, estado)
        VALUES (?, ?, ?, ?)
    """, (id_cliente, servicio, anio, estado))

    conn.commit()
    conn.close()
    print("Solicitud agregada correctamente.")

def listar_solicitudes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM solicitudes")
    solicitudes = cursor.fetchall()

    print("\nLISTA DE SOLICITUDES:")
    for s in solicitudes:
        print("-----------------------------")
        print(f"ID Cliente: {s[1]}")
        print(f"Servicio: {s[2]}")
        print(f"Año Fiscal: {s[3]}")
        print(f"Estado: {s[4]}")
    conn.close()

def buscar_solicitud():
    conn = connect_db()
    cursor = conn.cursor()
    id_cliente = input("Ingrese número de identificación: ")

    cursor.execute("SELECT * FROM solicitudes WHERE idcliente = ?", (id_cliente,))
    s = cursor.fetchone()
    if s:
        print("\n--- Solicitud encontrada ---")
        print(f"ID Cliente: {s[1]}")
        print(f"Servicio: {s[2]}")
        print(f"Año Fiscal: {s[3]}")
        print(f"Estado: {s[4]}")
    else:
        print("No se encontró solicitud.")
    conn.close()

def main():
    crear_tabla_solicitudes() # <- CREA LA TABLA SI NO EXISTE

    while True:
        print("\nMENU SOLICITUDES")
        print("1. Agregar Solicitud")
        print("2. Listar Solicitudes")
        print("3. Buscar Solicitud")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            add_solicitud()
        elif opcion == "2":
            listar_solicitudes()
        elif opcion == "3":
            buscar_solicitud()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
