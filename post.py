import requests
import json

# import env variables
with open("config.json", "r") as f:
    config = json.load(f)

# use same data from conftest.py
test_dict = {
    "age": 40,
    "workclass": "Private",
    "fnlgt": 83311,
    "education": "Masters",
    "education-num": 13,
    "marital-status": "Married-civ-spouse",
    "occupation": "Exec-managerial",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "Canada",
}

# post request
response = requests.post(
    url=config["heroku_url"],
    data=json.dumps(test_dict),
)

print(response)
