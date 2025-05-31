Esta rama implementa los mismos scripts, pero usando SQLite como base de datos relacional, con la librería estándar sqlite3 de Python.

También reemplacé las entidades:

Clínicas particulares → Clientes

Parques recreativos → Solicitudes

Aquí el código sigue la misma lógica que la versión Mongo, pero usando SQL:

Se crean tablas si no existen (clientes y solicitudes).

Se agregan validaciones para evitar registros duplicados o solicitudes de clientes no registrados.

La estructura de carpetas contiene una carpeta llamada sqlite donde están ambos scripts.
