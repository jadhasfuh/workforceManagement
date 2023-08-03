from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel

app = FastAPI()

# http://127.0.0.1:8000/createWorkOrder
# pip install fastapi uvicorn pymongo

# Replace 'your_mongodb_uri' with your actual MongoDB connection string
client = MongoClient('mongodb+srv://Adrian:bEyiBP4PsllpsylS@cluster0.wvmdahm.mongodb.net/?retryWrites=true&w=majority')

# Replace 'your_database_name' with your desired database name
db = client.wfm

# Replace 'your_collection_name' with your desired collection name
collection = db.orders

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
    try:
        # Create a new instance of the Item model
        new_item = Order(**order.dict())
        # Insert the new_item into the collection
        insert_result = collection.insert_one(new_item.dict())
        # Get the inserted document's ID
        inserted_id = str(insert_result.inserted_id)
        # Create the response message
        response_message = f"Orden {order.NumOrdenServicio} creada"
        # Return the response
        return {"message": response_message, "inserted_id": inserted_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
