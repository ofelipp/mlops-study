from dataclasses import asdict, dataclass
from typing import Dict, Union


@dataclass
class ModelPrediction:
    prediction: Union[str, int, float]
    features: Dict[str, Union[str, int, float]]

    def to_dict(self):
        return asdict(self)
