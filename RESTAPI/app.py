
from flask import Flask, request
app = Flask(__name__)
import uuid
from db import items

@app.get('/items') # http://127.0.0.1:5000/get-items
def get_items():
    return {"items":items}

@app.get('/item') # http://127.0.0.1:5000/get-items
def get_item():
    id = request.args.get('id')
    try:
        return items[id]
    except:
        return {"message": "Record doesn't exist"},404



@app.post('/items')
def add_item():
    request_data=request.get_json()
    if "name" not in request_data or "price" not in request_data:
        return {"message":"'name' and 'price' must be included"}
    items[uuid.uuid4().hex]= request_data
    return {"message": "item added successfully"}, 201


@app.put('/items')
def update_item():
    id = request.args.get('id')
    if id == None:
        return {"message":"given id not found"},404


    if id in items.keys():
        request_data = request.get_json()
        if "name" not in request_data or "price" not in request_data:
            return {"message": "'name' and 'price' must be included"}
        items[id] = request.get_json()
        return {"message": "item updated successfully"}, 200
    return{"message":"Not Found"},404



@app.delete('/items')
def delete_item():
    id = request.args.get('id')
    if id in items.keys():
        del items[id]
        return {"message":"item deleted successfully"}, 200
    else:
        return {"message": "Record doesn't exist"}, 404