import math

n1 = input("Ingresa un número para calcular su factorial")

n1 = int(n1)

FC = math.factorial(n1)

mensaje = f"""
Su resultado al calcular el factorial del número es {FC}
"""
print(mensaje)
