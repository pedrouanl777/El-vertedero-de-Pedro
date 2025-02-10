# 18 Resolver ecuaciones cuadráticas
import cmath


def resolver_ecuacion_cuadratica(a, b, c):
    if a == 0:
        return "No es una ecuación cuadrática (a no puede ser 0)"

    discriminante = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + discriminante) / (2 * a)
    x2 = (-b - discriminante) / (2 * a)

    return x1, x2


a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

soluciones = resolver_ecuacion_cuadratica(a, b, c)
print(f"Las soluciones son: {soluciones[0]} y {soluciones[1]}")


# GG