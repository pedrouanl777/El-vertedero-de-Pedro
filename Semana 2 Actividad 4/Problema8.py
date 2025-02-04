import math
# Calcular el área y la circunferencia de un círculo (eZ)
n1 = input("Ingrese el radio del círculo")

n1 = float(n1)

area = (math.pi * n1**2)
circ = (2 * math.pi * n1)

mensaje = f"""
El área del círculo es: {area}
La circunferencia del círculo es: {circ}
"""
print(mensaje)