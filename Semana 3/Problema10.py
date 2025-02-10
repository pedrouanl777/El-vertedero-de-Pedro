#24. Calcular la suma de una serie numérica
def suma_serie(lista_numeros):
    return sum(lista_numeros)

# Ejemplo de uso con una lista ingresada manualmente
numeros = list(map(float, input("Ingrese los números de la serie separados por espacios: ").split()))
resultado = suma_serie(numeros)
print(f"La suma de la serie es: {resultado}")
