import requests

def test_get_korisnik():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Leanne Graham"
    assert response.json()["email"] == "Sincere@april.biz"

def test_get_svi_korisnici():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    
    assert response.status_code == 200
    assert len(response.json()) == 10

def test_korisnik_ne_postoji():
    response = requests.get("https://jsonplaceholder.typicode.com/users/999")
    
    assert response.status_code == 404

def test_kreiraj_korisnika():
    novi_korisnik = {
        "name": "Mateja",
        "username": "mmirk",
        "email": "mateja@test.com"
    }
    
    response = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=novi_korisnik
    )
    
    assert response.status_code == 201
    assert response.json()["name"] == "Mateja"
    assert response.json()["email"] == "mateja@test.com"

def test_azuriraj_korisnika():
    azurirani_podaci = {
        "name": "Mateja Updated"
    }
    
    response = requests.put(
        "https://jsonplaceholder.typicode.com/users/1",
        json=azurirani_podaci
    )
    
    assert response.status_code == 200
    assert response.json()["name"] == "Mateja Updated"

def test_obrisi_korisnika():
    response = requests.delete("https://jsonplaceholder.typicode.com/users/1")
    
    assert response.status_code == 200