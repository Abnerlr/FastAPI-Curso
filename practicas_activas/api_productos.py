from uuid import uuid4 as uuid
from fastapi import FastAPI
from pydantic import BaseModel

class Producto(BaseModel):
    id: uuid
    nombre: str
    precio_compra: float
    precio_venta: float
    provedor: str

app = FastAPI()

productos = []

@app.get('/')
def index():
    return {'mensaje': 'Bienvenidos a la API de productos'}

@app.get('/producto')
def obtener_productos():
    return productos


@app.post('/producto')
def crear_producto(producto: Producto):
    productos.append(producto)
    return {'message': 'Producto creado satisfactoriamente'}

