n1 = input("Ingresa primer número")
n2 = input("Ingresa segundo número")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
La suma de sus números es igual a {suma}
La resta de sus números es igual a {resta}
La multiplicación de sus números es igual a {multi}
La división de sus números es igual a {div}
"""
print(mensaje)
