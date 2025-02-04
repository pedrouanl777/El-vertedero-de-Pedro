def es_primo(n):      # Verificar si es mi primo, La actividad
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


numero = int(input("Ingrese un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo") # Estuvo potente para un normie como yo
    