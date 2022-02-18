from Augmenters.Augmenter import Augmenter
from PIL import Image

try: #test for full-gpu support
    import cupy as np 
    from cupyx.scipy import ndimage 
    from cupyx.scipy.ndimage.filters import gaussian_filter 
except:
    import numpy as np
    from scipy import ndimage

class AugmenterVShear(Augmenter):
    
    def __init__(self, shear_y: float = 0):
        self.__shear_y__: float = shear_y
        self.__transformation_matrix__: np.ndarray = np.array([[1, self.__shear_y__, 0, 0],
                                                               [0, 1,                0, 0], 
                                                               [0, 0,                1, 0],
                                                               [0, 0,                0, 1]])

    def transform(self, image: Image):
        self.__img_width__, self.__img_height__ = image.size
        self.__transformation_matrix__: np.ndarray = np.array([[1, self.__shear_y__, 0, -self.__img_width__  / 2 * self.__shear_y__],
                                                               [0, 1,                0, 0], 
                                                               [0, 0,                1, 0],
                                                               [0, 0,                0, 1]])

        return ndimage.affine_transform(input  = self.get_array_from_image(image),
                 	                    matrix = self.__transformation_matrix__)
    
    def get_transformed_YOLO_values(self, center_x: float, center_y: float, width: float, height: float):       	
        #s_center_y: float = center_y + center_x * self.__shear_y__ - width / 2 * self.__shear_y__      
        s_height: float = height * self.__img_height__ + abs(width * self.__img_width__ * self.__shear_y__) 
        
        return center_x, center_y, width, s_height / self.__img_height__


    def get_augmenter_signature(self):
        return "VSHEAR"