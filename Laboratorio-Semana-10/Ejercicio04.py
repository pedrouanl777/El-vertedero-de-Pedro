import statistics

def calcular_estadisticas(*numeros):
    if not numeros:
        return "No se ingresaron números."
    
    promedio = lambda nums: sum(nums) / len(nums)
    mediana = statistics.median(numeros)
    desviacion_estandar = statistics.stdev(numeros) if len(numeros) > 1 else 0
    
    return {
        "Promedio": promedio(numeros),
        "Mediana": mediana,
        "Desviación estándar": desviacion_estandar
    }

# Solicitar números al usuario
numeros_usuario = list(map(float, input("Ingrese una lista de números separados por espacios: ").split()))

# Calcular y mostrar estadísticas
resultados = calcular_estadisticas(*numeros_usuario)
print("Resultados estadísticos:")
for clave, valor in resultados.items():
    print(f"{clave}: {valor}")