from uuid import uuid4 as uuid
from fastapi import FastAPI, HTTPException
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
    producto.id = str(uuid())
    productos.append(producto)
    return {'message': 'Producto creado satisfactoriamente'}


@app.get('/producto/{producto_id}')
def obtener_producto_por_id(producto_id: str):
#    for p in productos:
#        if p.id == producto_id:
#            return p
    resultado = list(filter(lambda p: p.id == producto_id, productos))

    if len(resultado):
        return resultado[0]
        
    #return{'mensaje': f'El producto con el id {producto_id} no fue encontrado'}

    raise HTTPException(status_code=404, detail=f'El producto con id {producto_id} no fue encontrado')
