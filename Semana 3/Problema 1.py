# 13. Convertir una temperatura entre distintas escalas
print('Ingrese la cantidad en Celsius')
n1 = float(input())


F = (n1 * 9/5) + 32
K = n1 + 273.15

mensaje = f"""
La conversión de grados Celsius a Fahrenheit es {F} F
La conversión de grados Celsius a Kelvin es {K} K
"""
print(mensaje)