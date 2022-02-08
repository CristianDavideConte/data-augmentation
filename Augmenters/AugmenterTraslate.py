from Augmenters.Augmenter import Augmenter
import numpy as np

from PIL import Image
from scipy import ndimage

class AugmenterTraslate(Augmenter):
    def __init__(self, delta_x: float, delta_y: float):
        self.__delta_x__: float = delta_x
        self.__delta_y__: float = delta_y
        self.__transformation_matrix__: np.ndarray = np.array([[1, 0, 0, -self.__delta_y__], 
                                                               [0, 1, 0, -self.__delta_x__], 
                                                               [0, 0, 1, 0],
                                                               [0, 0, 0, 1]])

    def transform(self, image: Image):
        self.__img_width__, self.__img_height__ = image.size 
        return ndimage.affine_transform(input  = self.get_array_from_image(image),
                                        matrix = self.__transformation_matrix__)
    
    def get_transformed_YOLO_values(self, center_x: float, center_y: float, width: float, height: float):
        absolute_center_x: float = center_x * self.__img_width__
        translated_center_x: float = (absolute_center_x + self.__delta_x__) / self.__img_width__

        absolute_center_y: float = center_y * self.__img_height__
        translated_center_y: float = (absolute_center_y + self.__delta_y__) / self.__img_height__ 

        return translated_center_x, translated_center_y, width, height


    def get_augmenter_signature(self):
        return "TRASLT"