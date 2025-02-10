# 15. Determinar si un año bisiesto.

print("Introduce el año que quieras determinar")
ano = int(input(""))

print("Es bisiesto" if not ano % 4 and (ano %
      100 or not ano % 400) else "No es bisiesto")

# Fue algo agotador a pesar de todo ajssjaasj