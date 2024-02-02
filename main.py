from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

#Creacion de una aplicacion FastAPI

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] =  None

@app.get('/')
def read_root():
    return "Hello world!"

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}

@app.get('/calculadora')
def calcular(operando1: float, operando2: float):
    return {'suma': operando1 + operando2}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name,
            'item_id': item_id,
            'item_price': item.price}