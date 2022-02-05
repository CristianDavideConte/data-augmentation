from Augmenters.Augmenter import Augmenter
import numpy as np

from PIL import Image
from scipy import ndimage

class AugmenterHShear(Augmenter):
    
    def __init__(self, shear_x: float = 0):
        self.__shear_x__: float = shear_x
        self.__transformation_matrix__: np.ndarray = np.array([[1,                 0, 0, 0],
                                                               [self.__shear_x__,  1, 0, 0], 
                                                               [0,                 0, 1, 0],
                                                               [0,                 0, 0, 1]])

    def transform(self, image: Image):
        self.__img_width__, self.__img_height__ = image.size
        self.__transformation_matrix__: np.ndarray = np.array([[1,                 0, 0, 0],
                                                               [self.__shear_x__,  1, 0, -self.__img_height__ / 2 * self.__shear_x__], 
                                                               [0,                 0, 1, 0],
                                                               [0,                 0, 0, 1]])

        return ndimage.affine_transform(input  = self.get_array_from_image(image),
                 	                    matrix = self.__transformation_matrix__)
    
    def get_transformed_YOLO_values(self, center_x: float, center_y: float, width: float, height: float):   
        s_center_x: float = center_x + center_y * self.__shear_x__ + - height / 2 * self.__shear_x__      
        s_width: float = width * self.__img_width__ + abs(height * self.__img_height__ * self.__shear_x__) 
        
        return s_center_x, center_y, s_width / self.__img_width__, height
	
    def get_augmenter_signature(self):
        return "HSHEAR"