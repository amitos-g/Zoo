from db import setup
from fastapi import FastAPI
from typing import Literal
from animals import AnimalRequest, Parrot, Pigeon, Crow, Tiger, Monkey, Lion, Shark, Whale, Dolphin
from dotenv import load_dotenv
import os
from fastapi import Request
# RUN THIS FILE FOR API START
load_dotenv()
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
PASSWORD = os.getenv("PASSWORD")

db_client = setup(HOST, PORT, PASSWORD)



app = FastAPI()

@app.get("/")
def home():
    return {"message" : "use /docs for api reference"}

### CREATE ###

@app.post("/create/sea")
def create_sea_animal(animalType: Literal["Shark", "Whale", "Dolphin"], new: AnimalRequest):
    this_animal = Shark(new) if animalType == "Shark" else Whale(new) if animalType == "Whale" else Dolphin(new)
    inserted_id = db_client.insert(this_animal)
    if inserted_id == -1:
        return {"error" : f"animal with name {new.name} already exists"}
    return {"message" : f"created animal named {new.name} with id {inserted_id}"}

@app.post("/create/air")
def create_air_animal(animalType: Literal["Parrot", "Pigeon", "Crow"], new: AnimalRequest):
    this_animal = Parrot(new) if animalType == "Parrot" else Pigeon(new) if animalType == "Pigeon" else Crow(new)
    inserted_id = db_client.insert(this_animal)
    if inserted_id == -1:
        return {"error" : f"animal with name {new.name} already exists"}
    return {"message" : f"created animal named {new.name} with id {inserted_id}"}

@app.post("/create/land")
def create_land_animal(animalType: Literal["Tiger", "Monkey", "Lion"], new: AnimalRequest):
    this_animal = Tiger(new) if animalType == "Tiger" else Monkey(new) if animalType == "Monkey" else Lion(new)
    inserted_id = db_client.insert(this_animal)
    if inserted_id == -1:
        return {"error" : f"animal with name {new.name} already exists"}
    return {"message" : f"created animal named {new.name} with id {inserted_id}"}

### READ ###

@app.get("/get/all")
def get_all_animals():
    answer = db_client.get_all()
    if answer == -1:
        return {"message" : "error"}
    return answer

@app.get("/get/air")
def get_air_animals():
    answer = db_client.get_air()
    if answer == -1:
        return {"message" : "error"}
    return answer
@app.get("/get/sea")
def get_sea_animals():
    answer = db_client.get_sea()
    if answer == -1:
        return {"message" : "error"}
    return answer
@app.get("/get/land")
def get_land_animals():
    answer = db_client.get_land()
    if answer == -1:
        return {"message" : "error"}
    return answer

