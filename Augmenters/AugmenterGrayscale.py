from Augmenters.Augmenter import Augmenter
from PIL import Image

try: #test for full-gpu support
    import cupy as np 
    from cupyx.scipy import ndimage 
    from cupyx.scipy.ndimage.filters import gaussian_filter
except:
    import numpy as np
    from scipy import ndimage

class AugmenterGrayscale(Augmenter):
		
    def __init__(self):
        self.__transformation_matrix__: np.ndarray = np.array([[1, 0, 0, 0], 
                                                               [0, 1, 0, 0], 
                                                               [0, 0, 0, 0],
                                                               [0, 0, 0, 1]])

    def transform(self, image: Image):
        return ndimage.affine_transform(input  = self.get_array_from_image(image),
                                        matrix = self.__transformation_matrix__)
    
    def get_transformed_YOLO_values(self, center_x: float, center_y: float, width: float, height: float):       	
        return center_x, center_y, width, height
            
    def get_augmenter_signature(self):
        return "GRSCL"
