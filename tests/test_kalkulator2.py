import pytest

def oduzmi(a, b):
    return a - b

def pomnozi(a, b):
    return a * b

def podeli(a, b):
    if b == 0:
        return "Ne moze se deliti sa nulom"
    return a / b

@pytest.mark.parametrize("a, b, rezultat", [
    (5, 3, 2),
    (0, 0, 0),
    (10, 4, 6),
])
def test_oduzmi(a, b, rezultat):
    assert oduzmi(a, b) == rezultat

@pytest.mark.parametrize("a, b, rezultat", [
    (5, 3, 15),
    (2, 2, 4),
    (10, 0, 0),
])
def test_pomnozi(a, b, rezultat):
    assert pomnozi(a, b) == rezultat

@pytest.mark.parametrize("a, b, rezultat", [
    (10, 2, 5),
    (9, 3, 3),
    (5, 0, "Ne moze se deliti sa nulom"),
])
def test_podeli(a, b, rezultat):
    assert podeli(a, b) == rezultat