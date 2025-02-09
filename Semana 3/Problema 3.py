print("Ingrese su moneda en pesos MX")
n1 = float(input(""))

USD = n1 * 0.050
EUR = n1 * 0.047
GBP = n1 * 0.039
JPY = n1 * 7.71

mensaje = f"""
La conversión de su moneda a USD es: {USD} $
La conversión de su moneda a EUR es: {EUR} $
La conversión de su moneda a GBP es: {GBP} $
La conversión de su moneda a JPY es: {JPY} $
"""
print(mensaje)