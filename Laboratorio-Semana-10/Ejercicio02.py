class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, categoria, precio, cantidad):
        self.productos.append({
            'nombre': nombre,
            'categoria': categoria,
            'precio': precio,
            'cantidad': cantidad
        })
        print(f"Producto '{nombre}' agregado correctamente.")

    def eliminar_producto(self, nombre):
        self.productos = [p for p in self.productos if p['nombre'] != nombre]
        print(f"Producto '{nombre}' eliminado, si existía en el inventario.")

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto['nombre'].lower() == nombre.lower():
                print("Información del producto:", producto)
                return
        print("Producto no encontrado.")

    def mostrar_productos_ordenados(self):
        productos_ordenados = sorted(self.productos, key=lambda p: p['precio'])
        print("Productos ordenados por precio:")
        for producto in productos_ordenados:
            print(producto)

# Ejemplo de uso del sistema de inventario
inventario = Inventario()

# Ejemplos de productos
test_productos = [
    ("Laptop", "Electrónica", 1200, 5),
    ("Teclado", "Periféricos", 45, 10),
    ("Monitor", "Electrónica", 250, 7)
]
for p in test_productos:
    inventario.agregar_producto(*p)


inventario.mostrar_productos_ordenados()


inventario.buscar_producto("Teclado")


inventario.eliminar_producto("Laptop")


inventario.mostrar_productos_ordenados()
