import pytest
import requests


@pytest.mark.parametrize("id, title, user_id", [
    (1, "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", 1),
    (2, "qui est esse", 1),
    (3, "ea molestias quasi exercitationem repellat qui ipsa sit aut", 1),
])
def test_postovi(base_url, id, title, user_id):
    response = requests.get(f"{base_url}/posts/{id}")
    
    assert response.status_code == 200
    assert response.json()["title"] == title 
    assert response.json()["userId"] == user_id

def test_kreiraj_post(base_url, headers):
    novi_post = {
        "userId": 1,
        "title": "Bla bla bla",
        "body": "Nema leba"
    }
    
    response = requests.post(
        f"{base_url}/posts",
        json=novi_post,
        headers=headers
    )
    
    assert response.status_code == 201
    assert response.json()["title"] == "Bla bla bla"
    assert response.json()["body"] == "Nema leba"

def test_svi_postovi(base_url):
    response = requests.get(f"{base_url}/posts")
    
    assert response.status_code == 200
    assert len(response.json()) == 100
