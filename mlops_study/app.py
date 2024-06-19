from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from http import HTTPStatus

from mlops_study.schemas import Features, Prediction
from mlops_study.domains import ModelPrediction


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def root():
    response = """
    <html>
        <head>
            <title>ofelipp / mlops-study</title>
        </head>
        <body>
            <h1>ofelipp / mlops-study</h1>
            <p>Wilkommen to the MLOPs</p>
        </body>
    </html>
    """
    return response


@app.post("/model", status_code=HTTPStatus.OK, response_model=Prediction)
def prediction_model(features: Features):
    prediction = ModelPrediction(
        prediction=True,
        features=features.model_dump().get("features")
    )
    return prediction.to_dict()



if __name__ == "__main__":
    print("Hello")
