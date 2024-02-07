from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    id: Optional[str] = None
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

