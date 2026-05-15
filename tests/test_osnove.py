import pytest

def saberi(a, b):
    return a + b

@pytest.mark.parametrize("a, b, rezultat", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_saberi_vise_slucajeva(a, b, rezultat):
    assert saberi(a, b) == rezultat