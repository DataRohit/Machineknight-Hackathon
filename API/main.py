from typing import Union

from fastapi import FastAPI
from fastapi.responses import RedirectResponse


import pandas as pd
import pickle


from utils.get_features import *
from utils.get_rent import *

app = FastAPI()


@app.get("/")
def home():

    return RedirectResponse("https://machineknight-house-price.herokuapp.com/docs")
    # return "Hello World!"


df = pd.read_csv("./data/full_df.csv")


@app.get("/get_features/object_features")
def get_object_features():
    return {"object_features": get_obj_features(df)}


@app.get("/get_features/numerical_features")
def get_number_features():
    return {"numerical_features": get_num_features(df)}


@app.post("/predict/rent")
def predict_house_rent(
    house_type: str = "BHK2",
    lease_type: str = "FAMILY",
    furnishing: str = "SEMI_FURNISHED",
    parking: str = "BOTH",
    facing: str = "E",
    water_supply: str = "CORP_BORE",
    building_type: str = "AP",
    latitude: float = 12.934471,
    longitude: float = 77.634471,
    negotiable: int = 0,
    property_size: float = 1250,
    property_age: int = 25,
    bathroom: int = 2,
    cup_board: int = 2,
    floor_size: int = 6,
    total_floor_size: int = 12,
    amenities: float = 15,
    balconies: int = 2
):
    building_type_encoder = pickle.load(
        open('./encoders/building_type_encoder.pkl', 'rb'))
    facing_encoder = pickle.load(open('./encoders/facing_encoder.pkl', 'rb'))
    furnishing_encoder = pickle.load(
        open('./encoders/furnishing_encoder.pkl', 'rb'))
    lease_type_encoder = pickle.load(
        open('./encoders/lease_type_encoder.pkl', 'rb'))
    parking_encoder = pickle.load(open('./encoders/parking_encoder.pkl', 'rb'))
    type_encoder = pickle.load(open('./encoders/type_encoder.pkl', 'rb'))
    water_supply_encoder = pickle.load(
        open('./encoders/water_supply_encoder.pkl', 'rb'))

    model = pickle.load(
        open("./autosklearnregressor_model_2.sav", 'rb'))

    predicted_rent = get_rent(
        features={
            "type": house_type,
            "latitude": latitude,
            "longitude": longitude,
            "lease_type": lease_type,
            "negotiable": negotiable,
            "furnishing": furnishing,
            "parking": parking,
            "property_size": property_size,
            "property_age": property_age,
            "bathroom": bathroom,
            "facing": facing,
            "cup_board": cup_board,
            "floor_size": floor_size,
            "total_floor_size": total_floor_size,
            "amenities": amenities,
            "water_supply": water_supply,
            "building_type": building_type,
            "balconies": balconies
        },
        building_type_encoder=building_type_encoder,
        facing_encoder=facing_encoder,
        furnishing_encoder=furnishing_encoder,
        lease_type_encoder=lease_type_encoder,
        parking_encoder=parking_encoder,
        type_encoder=type_encoder,
        water_supply_encoder=water_supply_encoder,
        loaded_model=model
    )

    return {
        "input": {
            "type": house_type,
            "lease_type": lease_type,
            "furnishing": furnishing,
            "parking": parking,
            "facing": facing,
            "water_supply": water_supply,
            "building_type": building_type,
            "latitude": latitude,
            "longitude": longitude,
            "negotiable": negotiable,
            "property_size": property_size,
            "property_age": property_age,
            "bathroom": bathroom,
            "cup_board": cup_board,
            "floor_size": floor_size,
            "total_floor_size": total_floor_size,
            "amenities": amenities,
            "balconies": balconies
        },
        "predicted_rent": predicted_rent
    }
