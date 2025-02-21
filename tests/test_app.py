import fastapi.testclient
import json
import fastapi
from main import app

client = fastapi.testclient.TestClient(app)


def test_greeting():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == '"Welcome to the income prediction service!"'


def test_less_than_50K(features_less):
    r = client.post("/predict/", data=json.dumps(features_less))
    assert r.status_code == 200
    assert json.loads(r.text) == {"Predicted income": "<=50K"}


def test_more_than_50K(features_more):
    r = client.post("/predict/", data=json.dumps(features_more))
    assert r.status_code == 200
    assert json.loads(r.text) == {"Predicted income": ">50K"}
