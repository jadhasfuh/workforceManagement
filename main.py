from flask import Flask, request
from pymongo import MongoClient
from bson.json_util import dumps

#pip install Flask
app = Flask(__name__)

# Replace 'your_mongodb_uri' with your actual MongoDB connection string
client = MongoClient('mongodb+srv://Adrian:bEyiBP4PsllpsylS@cluster0.wvmdahm.mongodb.net/?retryWrites=true&w=majority')
# Replace 'your_database_name' with your desired database name
db = client.wfm
# Replace 'your_collection_name' with your desired collection name
collection = db.orders

# Create a new item
@app.route('/createWorkOrder', methods=['POST'])
def create_item():
    try:
        data = request.get_json()
        # Borramos antigua data
        collection.delete_many({})
        # Insert the new_item into the collection
        insert_result = collection.insert_one(data)
        # Get the inserted document's ID
        inserted_id = str(insert_result.inserted_id)
        # Create the response message
        response_message = f"Orden {data.get('NumOrdenServicio')} creada"
        # Return the response
        return {"message": response_message, "inserted_id": inserted_id}
    except Exception as e:
        return {"Error al insertar": e}

# Create a new item
@app.route('/confirmarNotificacion', methods=['POST'])
def send_notification():
    try:
        data = request.get_json()
        # Return the response
        return data
    except Exception as e:
        return {"Error al insertar": e}

# Cancelar orden
@app.route('/cancelarOrden', methods=['POST'])
def send_notification():
    try:
        data = request.get_json()
        # Borramos antigua data
        collection.delete_many({})
        # Insert the new_item into the collection
        insert_result = collection.insert_one(data)
        # Return the response
        return {"response": "200 OK"}
    except Exception as e:
        return {"Error al insertar": e}

# Get all items
@app.route('/', methods=['GET'])
def get_items():
    try:
        return dumps(list(collection.find()))
    except Exception as e:
        return {"Error al insertar": e}
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000)  # Change the port to your desired value
