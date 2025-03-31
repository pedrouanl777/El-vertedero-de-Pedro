
def sumar(a, b):
    """Función para sumar dos números."""
    return a + b

def restar(a, b):
    """Función para restar dos números."""
    return a - b

def multiplicar(a, b):
    """Función para multiplicar dos números."""
    return a * b

def dividir(a, b):
    """Función para dividir dos números. Retorna None si la división no es posible."""
    if b == 0:
        return None
    return a / b
