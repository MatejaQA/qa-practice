import os
import pytest
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def test_ai_odgovara():
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": "What is the capital of Serbia?"}
        ]
    )
    
    answer = response.choices[0].message.content
    print(answer)
    
    assert answer is not None
    assert len(answer) > 0

def test_ai_zna_glavni_grad():
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": "What is the capital of Serbia? Answer in one short sentence."}
        ]
    )
    
    answer = response.choices[0].message.content.lower()
    
    assert "belgrade" in answer
    assert len(answer) > 10
    assert len(answer) < 200


@pytest.mark.parametrize("pitanje, ocekivana_rec", [
    ("What is the capital of Serbia?", "belgrade"),
    ("What is the capital of France?", "paris"),
    ("What is the capital of Japan?", "tokyo"),
    ("What is the capital of Germany?", "berlin"),
])
def test_ai_glavni_gradovi(pitanje, ocekivana_rec):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": pitanje + " Answer in one short sentence."}
        ]
    )
    
    answer = response.choices[0].message.content.lower()
    
    assert ocekivana_rec in answer

def test_ai_vraca_json():
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a JSON API. Always respond with valid JSON only, no other text."},
            {"role": "user", "content": "Give me info about Belgrade. Return JSON with fields: name, country, population (approximate number)."}
        ],
        response_format={"type": "json_object"}
    )
    
    answer = response.choices[0].message.content
    print(answer)
    
    # Parse JSON
    data = json.loads(answer)
    
    # Proveri strukturu
    assert "name" in data
    assert "country" in data
    assert "population" in data
    
    # Proveri tipove
    assert isinstance(data["name"], str)
    assert isinstance(data["country"], str)
    assert isinstance(data["population"], int)
    
    # Proveri sadržaj
    assert "belgrade" in data["name"].lower()
    assert "serbia" in data["country"].lower()
    assert data["population"] > 0