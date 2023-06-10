from autodistill.detection import DetectionTargetModel
import supervision as sv

class YOLOv8(DetectionTargetModel):
    def __init__(self, model_name):
        # load model
        # if only one variant is available, remove the "model_name" argument
        self.model = ...

    def predict(self, input:str, confidence=0.5) -> sv.Detections:
        pass

    def train(self, dataset_yaml, epochs=300):
        pass