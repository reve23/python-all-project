from fastapi import FastAPI,Path,Query,HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


#creating methods
# @app.get("/")
# def home():
#     return {"data":"Testing"}

# @app.get("/about")
# def about():
#     return {"data":"about"}

#inventory management system

inventory = {}
@app.get('/get-item/{item_id}')
def get_item(item_id:int = Path(None,description="The ID of the item you want")):
    return inventory[item_id]
#path/qurey params
@app.get("/get-by-name/{item_id}")
def get_item(*,item_id:int,name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404,detail="Item name not found")

#request body 
class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class Updateitem(BaseModel):
    name: Optional[str] = None
    price: Optional[str] = None
    brand: Optional[str] = None

@app.post("/create-item/{item_id}")
def create_item(item_id: int,item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400,detail="Item ID already exists")
    inventory[item_id] = item
    return inventory[item_id]

#update item 
@app.put("/update-item/{item_id}")
def update_item(item_id: int,item: Updateitem):
    if item_id not  in inventory:
        raise HTTPException(status_code=404,detail="Item ID does not exists")

    if item.name != None:
        inventory[item_id].name = item.name
    if item.price !=None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]

#delete item 
@app.delete("/delete-item")
def delete_item(item_id: int = Query(...,description="the ID of the item to delete")):
    if item_id not in inventory:
        raise HTTPException(status_code=404,detail="Item ID does not exists")
    del inventory[item_id]
    return {"success":"Item deleted"}
