# 11. Verificar si una cadena es un palíndromo
def es_palindromo(palabra):
    palabra = str(input("").lower())  
    return palabra == palabra[::-1]



print(es_palindromo("Programacion"))
print(es_palindromo("Ojo"))

# Lo que hacemos es comparar la palabra con la misma pero invertida