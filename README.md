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

