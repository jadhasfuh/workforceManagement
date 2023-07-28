from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# http://127.0.0.1:8000/createWorkOrder

class Order(BaseModel):
    Producto: str
    Domicilio: str
    Contacto: str
    FechaAgendada: str
    NumOrdenServicio: str
    TipoMovimientoFacilidades: str
    TipoModem: str
    TipoTecnologia: str


@app.post("/createWorkOrder")
def createWorkOrder(order: Order):
    return {"message": f"Orden {order.NumOrdenServicio} creada"}

    """
    {
        "Producto": "AltaServicio",
        "Domicilio": "Honduras #759",
        "Contacto": "Adrian Ceja",
        "FechaAgendada": "21/07/2023",
        "NumOrdenServicio": "123546789",
        "TipoMovimientoFacilidades": "Alta",
        "TipoModem": "Telmex",
        "TipoTecnologia": "Fibra"
    }
    """
