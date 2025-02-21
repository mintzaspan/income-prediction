from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Dict
import pandas as pd
import json
import pickle

with open("config.json", "r") as f:
    config = json.load(f)


class Payload(BaseModel):
    age: int = Field(default=30)
    workclass: str = Field(default="Private")
    fnlgt: int = Field(default=205019)
    education: str = Field(default="HS-grad")
    education_num: int = Field(default=9, alias="education-num")
    marital_status: str = Field(
        default="Never-married", alias="marital-status"
    )
    occupation: str = Field(default="Adm-clerical")
    relationship: str = Field(default="Own-child")
    race: str = Field(default="Black")
    sex: str = Field(default="Male")
    capital_gain: int = Field(default=0, alias="capital-gain")
    capital_loss: int = Field(default=0, alias="capital-loss")
    hours_per_week: int = Field(default=40, alias="hours-per-week")
    native_country: str = Field(
        default="United-States", alias="native-country"
    )


app = FastAPI()


@app.get("/")
def greeting():
    return "Welcome to the income prediction service!"


@app.post("/predict/")
def make_prediction(features: Payload) -> Dict[str, str]:
    # import model
    with open(config["model_output_path"], "rb") as file:
        model = pickle.load(file)

    X = pd.DataFrame([features.model_dump(by_alias=True)])

    prediction = model.predict(X)[0]
    return {"Predicted income": prediction}
