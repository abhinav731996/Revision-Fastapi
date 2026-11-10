from fastapi import FastAPI
from pydantic import BaseModel;
from typing import List;

app = FastAPI()

class chai(BaseModel):
    id: int
    name: str
    origin: str

teas: List[chai] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to drink chai"}

@app.get("/tea")
def get_teas():
    return teas

@app.post("/teas")
def add_tea(tea: chai):
    teas.append(tea)
    return tea

# @app.put("/teas/{teas_id}")
# def update_tea(tea_id:int, updated_tea: Tea):
#     for index tea in enumerate(teas):
#         if tea.id == tea_id:
#         teas[index]=update_tea
#     return updated_tea