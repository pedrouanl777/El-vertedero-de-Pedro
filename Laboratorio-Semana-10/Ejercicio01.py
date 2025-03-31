from collections import Counter

def analizar_texto(texto):
    # Es para convertir el texto a minúsculas y dividirlo en palabras
    palabras = texto.lower().split()
    
    # Elimino signos de puntuación comunes
    palabras = [palabra.strip(".,!?;:()[]{}\"'") for palabra in palabras]
    
    # Para que cuente el número total de palabras
    total_palabras = len(palabras)
    
    # Creo un conjunto para contar palabras únicas
    palabras_unicas = set(palabras)
    cantidad_unicas = len(palabras_unicas)
    
    # Usé Counter para contar las veces que se repite cada palabra jiji
    frecuencia_palabras = Counter(palabras)
    
    # Encontrar la palabra más frecuente y su frecuencia
    palabra_mas_frecuente, max_frecuencia = frecuencia_palabras.most_common(1)[0]
    
    # Y aquí para los resultados
    print("Resumen del análisis del texto:")
    print(f"Total de palabras: {total_palabras}")
    print(f"Cantidad de palabras únicas: {cantidad_unicas}")
    print("Frecuencia de cada palabra:")
    for palabra, frecuencia in frecuencia_palabras.items():
        print(f"  {palabra}: {frecuencia}")
    print(f"Palabra más frecuente: '{palabra_mas_frecuente}' con {max_frecuencia} apariciones")

# Se ingresa un texto para poder analizar jeje
texto_usuario = input("Ingrese un texto para analizar: ")
analizar_texto(texto_usuario)
