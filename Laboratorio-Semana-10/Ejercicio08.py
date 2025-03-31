#Algoritmo Mergesort

def mergesort(lista):
    if len(lista) > 1:
        # Divido la lista en dos mitades
        medio = len(lista) // 2
        mitad_izquierda = lista[:medio]
        mitad_derecha = lista[medio:]

        
        mergesort(mitad_izquierda)
        mergesort(mitad_derecha)

        # Se inicia índices para los subarreglos y el arreglo principal
        i = j = k = 0

        # Fusion de las dos mitades 
        while i < len(mitad_izquierda) and j < len(mitad_derecha): #(Fuuusion)
            if mitad_izquierda[i] < mitad_derecha[j]:
                lista[k] = mitad_izquierda[i]
                i += 1
            else:
                lista[k] = mitad_derecha[j]
                j += 1
            k += 1

        # Hay que verificar si quedan elementos en la mitad izquierda
        while i < len(mitad_izquierda):
            lista[k] = mitad_izquierda[i]
            i += 1
            k += 1

        # Verificamos si quedan elementos en la mitad derecha
        while j < len(mitad_derecha):
            lista[k] = mitad_derecha[j]
            j += 1
            k += 1

# Solicitamos al usuario una lista de números
lista_usuario = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))

# Se muestra la lista antes del ordenamiento
print("Lista original:", lista_usuario)

# Utilizamos Mergesort
mergesort(lista_usuario)

# Y finalmente se muestra la lista jiji
print("Lista ordenada:", lista_usuario)
