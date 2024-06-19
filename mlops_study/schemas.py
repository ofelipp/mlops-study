import json

from pydantic import BaseModel
from typing import Dict, List, Union


class Features(BaseModel):
    features: Dict[str, Union[str, int, float]]


class Prediction(BaseModel):
    prediction: Union[float, str]
    features: Dict[str, Union[str, int, float]]

