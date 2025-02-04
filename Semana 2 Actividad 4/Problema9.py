def generar_pares_impares(limite):
    pares = []
    impares = []
    
    for n in range(limite + 1):
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
            
    return pares, impares

limite = int(input("Ingrese un límite de números"))
pares, impares = generar_pares_impares(limite)

print("Números pares hasta", limite, ":", pares)
print("Números impares hasta", limite, ":", impares)
# Me dio algo de miedito