# Secuencia de Fibonacci hasta un número dado de términos (khe?)

import math


def fibonacci_n(n):
    sqrt5 = math.sqrt(5)
    n1 = (1 + sqrt5) / 2
    n2 = (1 - sqrt5) / 2
    return int((n1**n - n2**n) / sqrt5)

# Usaré como "hasta número dado" hasta el 13


for i in range(13):
    print(fibonacci_n(i), end=" ")

    # Se usó la fórmula de Binet :I (no juzguen)
