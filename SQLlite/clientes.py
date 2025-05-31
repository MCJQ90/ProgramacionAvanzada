import sqlite3

def connect_db():
    conn = sqlite3.connect('JLcontador.sqlite')
    return conn

def add_cliente():
    conn = connect_db()
    cursor = conn.cursor()

    print("\nAgregar Cliente:")
    print("1. Cédula")
    print("2. RUC")

    while True:
        opcion = input("Seleccione el tipo de identificación: ")
        if opcion == "1":
            tipo_id = "Cédula"
            break
        elif opcion == "2":
            tipo_id = "RUC"
            break
        else:
            print("Opción inválida.")

    while True:
        id_cliente = input("Número de identificación: ")
        if tipo_id == "Cédula" and id_cliente.isdigit() and len(id_cliente) == 10:
            break
        elif tipo_id == "RUC" and id_cliente.isdigit() and len(id_cliente) == 13 and id_cliente.endswith("001"):
            break
        else:
            print("Identificación inválida.")

    nombre = input("Nombres: ")
    apellido = input("Apellidos: ")
    direccion = input("Dirección: ")

    while True:
        celular = input("Celular: ")
        if celular.isdigit() and len(celular) == 10:
            break
        else:
            print("Celular inválido.")

    while True:
        email = input("Correo electrónico: ")
        if "@" in email and "." in email:
            break
        else:
            print("Correo inválido.")

    print("Tipo de contribuyente:")
    print("1. Régimen General")
    print("2. Rimpe Emprendedor")
    print("3. Rimpe Negocio Popular")
    while True:
        tipo = input("Seleccione una opción: ")
        if tipo == "1":
            tipo_contribuyente = "Régimen General"
            break
        elif tipo == "2":
            tipo_contribuyente = "Rimpe Emprendedor"
            break
        elif tipo == "3":
            tipo_contribuyente = "Rimpe Negocio Popular"
            break
        else:
            print("Opción inválida.")

    actividad = input("Actividad económica: ")

    cursor.execute("""
        INSERT INTO clientes (
            idcliente, tipo_id, nombre, apellido, direccion, celular, email, tipo_contribuyente, actividad_economica
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (id_cliente, tipo_id, nombre, apellido, direccion, celular, email, tipo_contribuyente, actividad))

    conn.commit()
    conn.close()
    print("Cliente agregado correctamente.")

def listar_clientes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    print("\nLISTA DE CLIENTES:")
    for c in clientes:
        print("-----------------------------")
        print(f"ID: {c[0]}")
        print(f"Nombre: {c[2]} {c[3]}")
        print(f"Tipo ID: {c[1]}")
        print(f"Dirección: {c[4]}")
        print(f"Celular: {c[5]}")
        print(f"Email: {c[6]}")
        print(f"Contribuyente: {c[7]}")
        print(f"Actividad: {c[8]}")

    conn.close()

def buscar_cliente():
    conn = connect_db()
    cursor = conn.cursor()
    id_cliente = input("Ingrese número de identificación: ")
    cursor.execute("SELECT * FROM clientes WHERE idcliente = ?", (id_cliente,))
    c = cursor.fetchone()
    if c:
        print("\n--- Cliente encontrado ---")
        print(f"ID: {c[0]}")
        print(f"Nombre: {c[2]} {c[3]}")
        print(f"Tipo ID: {c[1]}")
        print(f"Dirección: {c[4]}")
        print(f"Celular: {c[5]}")
        print(f"Email: {c[6]}")
        print(f"Contribuyente: {c[7]}")
        print(f"Actividad: {c[8]}")
    else:
        print("Cliente no encontrado.")
    conn.close()

def crear_tabla_clientes():
    """
    Crea la tabla clientes si no existe
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            idcliente TEXT PRIMARY KEY,
            tipo_id TEXT,
            nombre TEXT,
            apellido TEXT,
            direccion TEXT,
            celular TEXT,
            email TEXT,
            tipo_contribuyente TEXT,
            actividad_economica TEXT
        )
    """)
    conn.commit()
    conn.close()    

def main():
    crear_tabla_clientes()  # <- ESTA LÍNEA CREA LA TABLA SI NO EXISTE

    while True:
        print("\nMENU CLIENTES")
        print("1. Agregar Cliente")
        print("2. Listar Clientes")
        print("3. Buscar Cliente")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            add_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()