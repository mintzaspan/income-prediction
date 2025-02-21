from fastapi import FastAPI
from pydantic import BaseModel, Field



class Payload(BaseModel):
    age : int = Field(default=30)
    workclass : str = Field(default="Private")
    fnlgt : int = Field(default=205019)
    education : str = Field(default="HS-grad")
    education_num : int = Field(default=9, alias="education-num")
    marital_status : str = Field(default="Never-married", alias="marital-status")
    occupation : str = Field(default="Adm-clerical")
    relationship : str = Field(default="Own-child")
    race : str = Field(default="Black")
    sex : str = Field(default="Male")
    capital_gain : int = Field(default=0, alias="capital-gain")
    capital_loss : int = Field(default=0, alias="capital-loss")
    hours_per_week : int = Field(default=40, alias="hours-per-week")
    native_country : str = Field(default="United-States", alias="native-country")

app = FastAPI()

@app.get("/")
def greeting():
    return("Welcome to the income prediction service!")

