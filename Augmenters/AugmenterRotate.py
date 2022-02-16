from Augmenters.Augmenter import Augmenter
import numpy as np
import math

from PIL import Image
from scipy import ndimage

class AugmenterRotate(Augmenter):
    
    def __init__(self, angle: float):
        self.__rotation__: float = angle     
        self.__angle__: float = math.radians(angle)
        self.__cos__: float = math.cos(self.__angle__)
        self.__sin__: float = math.sin(self.__angle__) 
        self.__transformation_matrix__: np.ndarray = np.array([[ self.__cos__, self.__sin__, 0, 0], 
                                                               [-self.__sin__, self.__cos__, 0, 0],
                                                               [ 0,            0,            1, 0],
                                                               [ 0,            0,            0, 1]])
        
    def transform(self, image: Image):   
        self.__img_width__, self.__img_height__ = image.size 

        origin_x: float = 0.5 * self.__img_width__
        origin_y: float = 0.5 * self.__img_height__
        
        delta_x: float = origin_x * (1 - self.__cos__) + origin_y * self.__sin__
        delta_y: float = origin_y * (1 - self.__cos__) - origin_x * self.__sin__
        self.__transformation_matrix__: np.ndarray = np.array([[ self.__cos__, self.__sin__, 0, delta_y], #y-transl
                                                               [-self.__sin__, self.__cos__, 0, delta_x], #x-transl
                                                               [ 0,            0,            1, 0],
                                                               [ 0,            0,            0, 1]])
        
        return ndimage.affine_transform(input  = self.get_array_from_image(image), 
                                        matrix = self.__transformation_matrix__)    
                                        
                            
    def get_transformed_YOLO_values(self, center_x: float, center_y: float, width: float, height: float):
        scaled_img_center_x: float = 0.5 * self.__img_width__
        scaled_img_center_y: float = 0.5 * self.__img_height__

        scaled_center_x: float = center_x * self.__img_width__
        scaled_center_y: float = center_y * self.__img_height__
        scaled_width:  float = width  * self.__img_width__
        scaled_height: float = height * self.__img_height__ 

        r_center_x: float = self.__cos__ * (scaled_center_x - scaled_img_center_x) + self.__sin__ * (scaled_center_y - scaled_img_center_y) + scaled_img_center_x 
        r_center_y: float = self.__cos__ * (scaled_center_y - scaled_img_center_y) - self.__sin__ * (scaled_center_x - scaled_img_center_x) + scaled_img_center_y

        r_width:  float = abs(scaled_width  * self.__cos__) + abs(scaled_height * self.__sin__)
        r_height: float = abs(scaled_height * self.__cos__) + abs(scaled_width  * self.__sin__)
        
        return r_center_x / self.__img_width__, r_center_y / self.__img_height__, r_width / self.__img_width__, r_height / self.__img_height__ 
        
        #area_proportion: float = math.sqrt(scaled_width * scaled_height / r_width / r_height)
        #return r_center_x / self.__img_width__, r_center_y / self.__img_height__, area_proportion * r_width / self.__img_width__, area_proportion * r_height / self.__img_height__ 
	
    def get_augmenter_signature(self):
        #N = negative rotation (es. -83.2° -> N83)
        #P = positve rotation  (es. +47.9° -> P47)
        rotation_sign: str = "P" if self.__rotation__ > 0.0 else "N" 
        return "ROTATE_" + rotation_sign + str(abs(int(self.__rotation__)))