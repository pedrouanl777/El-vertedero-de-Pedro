# 12. Encontrar el mayor entre tres números dados

print("Introduce un primer número")
n1 = float(input(""))
print("Introduce un segundo número ")
n2 = float(input(""))
print("Introduce un tercer número")
n3 = float(input(""))


if n1 >= n2 and n1 >= n3:
    print(f"El número {n1} es mayor")
elif n2 >= n1 and n2 >= n3:
    print(f"El número {n2} es mayor")
elif n3 >= n1 and n3 >= n2:
    print(f"El número {n3} es mayor")
    
# Estuvo bien la verdad, se agradece