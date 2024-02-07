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

@app.delete('/producto/{producto_id}')
def elimina_producto_por_id(producto_id: str):
    resultado = list(filter(lambda p: p.id == producto_id, productos))

    if len(resultado):
        producto = resultado[0]
        productos.remove(producto)
        return {'message': f'Producto con {producto_id} fue eliminado satisfactoriamente'}




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


@app.put('/producto{producto_id}')
def actualizar_producto(producto_id: str, producto: Producto):
    resultado = list(filter(lambda p: p.id == producto_id, productos))

    if len(resultado):
        producto_encontrado = resultado[0]
        producto_encontrado.nombre = producto.nombre
        producto_encontrado.precio_compra = producto.precio_compra
        producto_encontrado.precio_venta = producto.precio_venta
        producto_encontrado.provedor = producto.provedor

        return producto_encontrado

    
    raise HTTPException(status_code=404, detail=f'El producto con id {producto_id} no fue encontrado')