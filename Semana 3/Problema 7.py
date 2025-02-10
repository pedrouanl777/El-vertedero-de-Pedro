import random

res = input("Desea lanzar los dados: S/N ")
while (res == 'S'):

    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)

    print("El dado uno en: " + str(n1) + " y el dado dos en:" + str(n2))
    print("La suma de los dos dados lanzados es: " + str(n1 + n2) + "\n")

    res = input("Desea lanzar los dados: S/N ")
    
# Tremendo video de 5 min en explicar que ondas, ahi por YT ha de estar, lo agradezco