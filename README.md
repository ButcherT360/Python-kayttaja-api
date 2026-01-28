\# Python User API



Tämä on yksinkertainen Python-backend FastAPI:lla, joka tallentaa käyttäjät SQLite-tietokantaan.



\## Teknologiat



\- Python

\- FastAPI

\- SQLAlchemy

\- SQLite



\## Käyttöönotto



1\. Luo virtuaaliympäristö:



```bash

python -m venv venv

source venv/bin/activate  # Windows: venv\\Scripts\\activate



Asenna riippuvuudet:



pip install fastapi uvicorn sqlalchemy pydantic





Käynnistä API:



uvicorn main:app --reload





Avaa selaimessa: http://127.0.0.1:8000/docs



POST /users → lisää käyttäjä



GET /users → näytä kaikki käyttäjät

## Harjoitusliikkeet (Exercises)

### POST /exercises – lisää liike

Lähetä JSON:

```json
{
  "name": "Penkkipunnerrus",
  "sets": 5,
  "reps": 5,
  "weight": 50
}

Kehonpainoliike ilman painoja:

{
  "name": "Punnerrus",
  "sets": 3,
  "reps": 12,
  "weight": 0
}

Vastaus:

{
  "message": "exercise created",
  "exercise": {
    "name": "Penkkipunnerrus",
    "sets": 5,
    "reps": 5,
    "weight": 50
  }
}

GET /exercises – näytä kaikki liikkeet

Vastaus:

[
  {
    "id": 1,
    "name": "Penkkipunnerrus",
    "sets": 5,
    "reps": 5,
    "weight": 50.0
  },
  {
    "id": 2,
    "name": "Punnerrus",
    "sets": 3,
    "reps": 12,
    "weight": 0.0
  }
]