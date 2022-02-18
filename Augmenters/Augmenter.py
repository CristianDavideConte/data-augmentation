from abc import ABC, abstractclassmethod
from PIL import Image 

try: #test for full-gpu support
    import cupy as np 
    from cupyx.scipy import ndimage 
    from cupyx.scipy.ndimage.filters import gaussian_filter
except:
    import numpy as np
    from scipy import ndimage

class Augmenter(ABC):
    __rotation__: float = 0
    
    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def transform(image: Image):
        pass

    @abstractclassmethod
    def get_transformed_YOLO_values(self, center_x: float, center_y: float, width: float, height: float):
        pass

    @abstractclassmethod
    def get_augmenter_signature(self):
        pass
    
    def get_identity_matrix(self): 
        return np.array([[1,0,0], [0,1,0], [0,0,1]])

    def get_tranformation_matrix(self):
        return self.__transformation_matrix__

    def get_array_from_image(self, image: Image):
        return np.array(image)
        
    def get_image_from_array(self, image_arr: np.ndarray):
        try:
            return Image.fromarray(np.asnumpy(image_arr), "RGB") #gpu
        except:
            return Image.fromarray(image_arr, "RGB") #cpu
            
    def get_image_rotation(self, image: Image):
        return self.__rotation__
