# calculadora.py - Funciones básicas de matemáticas

def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def dividir(a, b):
    """Divide dos números."""
    if b == 0:
        return "Error: no se puede dividir por cero"
    return a / b

# Ejemplos de uso
if __name__ == "__main__":
    print("=== Calculadora Básica ===")
    print(f"5 + 3 = {sumar(5, 3)}")
    print(f"10 - 4 = {restar(10, 4)}")
    print(f"6 * 7 = {multiplicar(6, 7)}")
    print(f"20 / 4 = {dividir(20, 4)}")
    print(f"10 / 0 = {dividir(10, 0)}")
