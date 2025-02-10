# 16. Contar el número de vocales y consonantes en una cadena
def vocales(cadena):
    contador = 0
    contadorc = 0
    for x in cadena.lower():
        if x in ('aeiou'):
            contador += 1
        if x in ('bcdfghjklmnñpqrstvwxyz'):
            contadorc += 1
    s = (str(contador) + " vocales y " + str(contadorc) + " consonantes")
    return s


a = input("ingrese: ")
print(vocales(a))

# 5mentarios pero tuvo chidori