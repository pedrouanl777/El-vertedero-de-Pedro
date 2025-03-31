class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrar_informacion(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Precio: {self.precio}'

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, precio, numero_puertas):
        super().__init__(marca, modelo, año, precio)
        self.numero_puertas = numero_puertas

    def mostrar_informacion(self):
        informacion = super().mostrar_informacion()
        return f'{informacion}, Número de puertas: {self.numero_puertas}'

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, precio, cilindrada):
        super().__init__(marca, modelo, año, precio)
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        informacion = super().mostrar_informacion()
        return f'{informacion}, Cilindrada: {self.cilindrada}'

# Ejemplos
# Una buena Toyotita y una Yamaha
auto = Automovil('Toyota', 'Corolla', 2021, 20000, 4)
moto = Motocicleta('Yamaha', 'R1', 2020, 15000, 1000)

# Y aquí la información de ambos vehículos
print(auto.mostrar_informacion())
print(moto.mostrar_informacion())