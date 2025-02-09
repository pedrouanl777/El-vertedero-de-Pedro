#27. Crear un conversor de unidades.

print("Ingrese la cantidad en cm")
n = float(input(""))

km = n / 100000
m = n / 100
plg = n / 2.54
Lts = n * 1000
ft = n / 30.48


mensaje = f"""
La cantidad en kilometros es: {km} km
La cantidad en metros es: {m} m
La cantidad en pulgadas es: {plg} in
La cantidad en litros es: {Lts} L
La cantidad en pies es: {ft} ft
"""
print(mensaje)