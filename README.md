En esta rama desarrollé dos scripts en Python utilizando MongoDB como base de datos NoSQL, con la librería pymongo. Adapté las entidades propuestas en el deber (Clínicas particulares y Parques recreativos) para que se ajusten a mi proyecto real:

Clínicas particulares fue reemplazada por la entidad Clientes, ya que en mi proyecto (Contador en Línea para PYMEs) es fundamental registrar a los clientes que solicitan servicios contables.

Parques recreativos fue reemplazada por Solicitudes, que representa cada vez que un cliente solicita un servicio (por ejemplo, declaración de impuesto a la renta).

Cada archivo implementa operaciones básicas:

clientes.py: permite agregar, listar y buscar clientes en la base de datos.

solicitudes.py: permite registrar solicitudes (una por cliente, por año fiscal), listarlas y buscarlas. Se valida que el cliente exista y que no tenga una solicitud duplicada para el mismo año.
