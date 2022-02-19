from Augmenters.Augmenter import Augmenter
from PIL import Image

try: #test for full-gpu support
    import cupy as np 
    from cupyx.scipy import ndimage 
    from cupyx.scipy.ndimage.filters import gaussian_filter 
except:
	import numpy as np
	from scipy.ndimage.filters import gaussian_filter


class AugmenterSharp(Augmenter):

    def __init__(self, sharp_index: float):
        self.__sharp_index__: float = float(sharp_index)

    def transform(self, image: Image):
        image_arr: np.ndarray = self.get_array_from_image(image)
        
        #https://stackoverflow.com/questions/26857829/does-filter2d-in-opencv-really-do-its-job
        blurred: np.ndarray = gaussian_filter(image_arr, (1, 1, 0)) 
        
        s_image: np.ndarray = float(self.__sharp_index__ + 1.0) * image_arr - self.__sharp_index__ * blurred
        s_image: np.ndarray = np.maximum(s_image, np.zeros(s_image.shape))
        s_image: np.ndarray = np.minimum(s_image, 255 * np.ones(s_image.shape))
        
        return s_image.round().astype(np.uint8)

    def get_transformed_YOLO_values(self, center_x: float, center_y: float, width: float, height: float):       	
        return center_x, center_y, width, height

    def get_augmenter_signature(self):
        return "SHARP"
