from fastapi import FastAPI
from pymongo import MongoClient
import uvicorn
from bson.objectid import ObjectId
from typing import List, Optional
from restaurant import Restaurant
app = FastAPI()

CLIENT = MongoClient(
    "mongodb+srv://user:resu@cluster0.tdpqz.gcp.mongodb.net/resto?retryWrites=true&w=majority")

DB = CLIENT["resto"]
RESTOS = DB["restaurants"]


@app.get("/restaurants")
async def root():
    return {"message": "Super les filles"}


@app.post("/restaurants")
async def create_restaurant(restaurant: Restaurant):
    restaurant_id = str(RESTOS.insert_one(restaurant.dict()).inserted_id)
    return {"restaurant_id": restaurant_id}


@app.post("/restaurants/bulk")
async def insert_many_restaurants(restaurant: List[Restaurant]):
    restaurants_list = []
    for r in restaurants:
        restaurants_list.append(r.dict())
    restaurants_ids = RESTOS.insert_many(restaurants_list).inserted_ids
    list_ids = []
    for restaurant_id in restaurants_ids:
        list_ids.append(str(restaurant_id))
    return list_ids


@app.get("/restaurants")
async def get_all_restaurants():
    restaurants = RESTOS.find()
    restaurant_list = []
    for restaurant in restaurants:
        restaurant["_id"] = str(restaurant["_id"])
        restaurant_list.append(restaurant)
    return restaurant_list


@app.get("/restaurants/id/{restaurant_id}")
async def get_restaurant_by_id(restaurant_id):
    # SELECT * FROM STUDENTS WHERE id = student_id
    restaurant = RESTOS.find_one({"_id": ObjectId(restaurant_id)})
    if restaurant:
        restaurant["_id"] = str(restaurant["_id"])
        return restaurant
    else:
        return f"Restaurant with id = {restaurant_id} not exist"


@app.get("/restaurants/enseigne/{enseigne}")
async def get_restaurant_by_enseigne(enseigne):
    # SELECT * FROM STUDENTS WHERE id = student_id
    restaurant = RESTOS.find_one({"enseigne": enseigne})
    if restaurant:
        restaurant["_id"] = str(restaurant["_id"])
        return restaurant
    else:
        return f"No restaurant named = {enseigne}"


@app.put("/restaurants/id/{id}")
async def update_restaurant(id, restaurant: Restaurant):
    RESTOS.find_one_and_replace({"_id": ObjectId(id)}, restaurant.dict())
    restaurant = RESTOS.find_one({"_id": ObjectId(id)})
    restaurant["_id"] = str(restaurant["_id"])
    return restaurant


@app.delete("/restaurants/id/{id}")
async def delete_restaurant_by_id(id):
    restaurant = RESTOS.find_one({"_id": ObjectId(id)})
    if restaurant:
        RESTOS.find_one_and_delete({"_id": ObjectId(id)})
        return f"Restaurant {restaurant['name']} has been deleted"
    else:
        return "Please enter a valid id"


@app.delete("/restaurants/enseigne/{enseigne}")
async def delete_restaurant_by_enseigne(enseigne):
    return {"enseigne": enseigne}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
