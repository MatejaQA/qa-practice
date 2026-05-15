import pytest

def oduzmi(a, b):
    return a - b

def pomnozi (a, b):
    return a * b

def podeli (a, b):
    if b == 0:
        return "Ne moze se deliti sa nulom"
    return a / b

@pytest.fixture
def brojevi ():
    return {"a": 10, "b": 2}

@pytest.mark.parametrize("operacija, rezultat", [
    ("oduzmi", 8),
    ("pomnozi", 20),
    ("podeli", 5),
])
def test_kalkulator(brojevi, operacija, rezultat):
    if operacija == "oduzmi":
        assert oduzmi(brojevi["a"], brojevi["b"]) == rezultat
    elif operacija == "pomnozi":
        assert pomnozi(brojevi["a"], brojevi["b"]) == rezultat
    elif operacija == "podeli":
        assert podeli(brojevi["a"], brojevi["b"]) == rezultat

