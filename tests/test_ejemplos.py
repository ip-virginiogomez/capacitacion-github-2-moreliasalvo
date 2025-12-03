# test_ejemplos.py - Tests para autograding

import sys
import os

# Agregar la carpeta ejemplos al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ejemplos'))

from calculadora import sumar, restar, multiplicar, dividir


def test_sumar():
    """Test función sumar."""
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0
    print("✓ Test sumar pasado")


def test_restar():
    """Test función restar."""
    assert restar(5, 3) == 2
    assert restar(10, 10) == 0
    assert restar(0, 5) == -5
    print("✓ Test restar pasado")


def test_multiplicar():
    """Test función multiplicar."""
    assert multiplicar(3, 4) == 12
    assert multiplicar(5, 0) == 0
    assert multiplicar(-2, 3) == -6
    print("✓ Test multiplicar pasado")


def test_dividir():
    """Test función dividir."""
    assert dividir(10, 2) == 5
    assert dividir(20, 4) == 5
    # Verificar que maneja división por cero
    resultado = dividir(10, 0)
    assert "Error" in str(resultado)
    print("✓ Test dividir pasado")


if __name__ == "__main__":
    # Ejecutar tests manualmente
    print("Ejecutando tests...")
    test_sumar()
    test_restar()
    test_multiplicar()
    test_dividir()
    print("\n✅ Todos los tests pasaron!")
