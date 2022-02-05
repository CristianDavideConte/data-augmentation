from Augmenters.Augmenter import Augmenter
from abc import ABC, abstractclassmethod

class Worker(ABC):
    
    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def transform_image_and_YOLO_label(self, path: str):
        pass