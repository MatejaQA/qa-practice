import pytest
import requests


@pytest.mark.parametrize("korisnik_id, ocekivani_ime", [
    (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch"),
])
def test_korisnici(base_url, korisnik_id, ocekivani_ime):
    response = requests.get(f"{base_url}/users/{korisnik_id}")
    
    assert response.status_code == 200
    assert response.json()["name"] == ocekivani_ime 