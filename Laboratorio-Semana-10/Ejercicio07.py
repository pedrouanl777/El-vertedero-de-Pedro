import random

# Función de Quicksort (Taba raro pero ya medio que le entendí)
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2] 
    izquierda = [x for x in lista if x < pivot]
    derecha = [x for x in lista if x > pivot]
    return quicksort(izquierda) + [pivot] + quicksort(derecha)

# Función de búsqueda binaria
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Se Genera lista de números aleatorios
n = int(input('Ingrese la cantidad de números: '))
lista = [random.randint(1, 100) for _ in range(n)]

# Primero se muestra la lista antes de ordenarla
print('Lista original:', lista)

# Se ordena la lista con Quicksort
lista_ordenada = quicksort(lista)
print('Lista ordenada:', lista_ordenada)

# Se realiza la querida Búsqueda binaria
numero_buscar = int(input('Ingrese el número a buscar: '))
resultado_busqueda = busqueda_binaria(lista_ordenada, numero_buscar)

if resultado_busqueda != -1:
    print(f'Número {numero_buscar} encontrado en la posición {resultado_busqueda}.')
else:
    print(f'Número {numero_buscar} no encontrado en la lista.')
