from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_read_item():
    response = client.get("http://127.0.0.1:8000/users/1", headers={
        "Authorization": f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMSIsImV4cCI6MTcwNzg0NDMzOH0.izrzc-reOCnBnPQlYKr9vQ5nN3uAg9bq3SN8FqIK--k'})
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }