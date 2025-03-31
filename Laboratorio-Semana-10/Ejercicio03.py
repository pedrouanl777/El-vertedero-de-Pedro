class AgendaContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, numero, correo):
        contacto = (nombre, numero, correo)
        self.contactos.append(contacto)
        print(f"Contacto '{nombre}' agregado correctamente.")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto[0].lower() == nombre.lower():
                print("Información del contacto:", contacto)
                return
        print("Contacto no encontrado.")

    def listar_contactos_ordenados(self):
        contactos_ordenados = sorted(self.contactos, key=lambda c: c[0])
        print("Lista de contactos ordenados por nombre:")
        for contacto in contactos_ordenados:
            print(contacto)

# Ejemplo de uso de la agenda de contactos
agenda = AgendaContactos()

# Agregar contactos
test_contactos = [
    ("Pedrinho", "555-1234", "elpepe@email.com"),
    ("Ana Gómez", "555-5678", "ana@email.com"),
    ("Luis Angelito", "555-9101", "luis@email.com")
]
for c in test_contactos:
    agenda.agregar_contacto(*c)

# Listar contactos ordenados
agenda.listar_contactos_ordenados()

# Buscar un contacto
agenda.buscar_contacto("Ana Gómez")