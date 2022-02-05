from Augmenters.Augmenter import Augmenter
import numpy as np

from PIL import Image
from scipy import ndimage

class AugmenterScale(Augmenter):
    
    def __init__(self, scaling_factor: float):
        self.__original_scaling_factor__: float = scaling_factor
        self.__scaling_factor__: float = 1 / scaling_factor
        self.__transformation_matrix__: np.ndarray = np.array([[ self.__scaling_factor__, 0,                       0, 0], 
                                                               [ 0,                       self.__scaling_factor__, 0, 0],
                                                               [ 0,                       0,                       1, 0],
                                                               [ 0,                       0,                       0, 1]])
        
    def transform(self, image: Image):      
        self.__img_width__, self.__img_height__ = image.size        
        self.__transformation_matrix__: np.ndarray = np.array([[ self.__scaling_factor__, 0,                       0, image.height / 2 * (1 - self.__scaling_factor__)], 
                                                               [ 0,                       self.__scaling_factor__, 0, image.width  / 2 * (1 - self.__scaling_factor__)],
                                                               [ 0,                       0,                       1, 0],
                                                               [ 0,                       0,                       0, 1]])

        return ndimage.affine_transform(input  = self.get_array_from_image(image), 
                                        matrix = self.__transformation_matrix__)    
                                        
                            
    def get_transformed_YOLO_values(self, center_x: float, center_y: float, width: float, height: float):
        s_center_x: float = center_x * self.__original_scaling_factor__ + (1 - self.__original_scaling_factor__) / 2
        s_center_y: float = center_y * self.__original_scaling_factor__ + (1 - self.__original_scaling_factor__) / 2
        
        return s_center_x, s_center_y, width * self.__original_scaling_factor__, height * self.__original_scaling_factor__
        
    def get_augmenter_signature(self):
        return "SCALE"