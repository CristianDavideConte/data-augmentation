from Augmenters.Augmenter import Augmenter
from PIL import Image

try: #test for full-gpu support
    import cupy as np 
    from cupyx.scipy import ndimage 
    from cupyx.scipy.ndimage.filters import gaussian_filter 
except:
    from scipy.ndimage.filters import gaussian_filter

class AugmenterBlur(Augmenter):
    def __init__(self, blur: float):
        self.__blur__ = abs(blur)

    def transform(self, image: Image):
        return gaussian_filter(self.get_array_from_image(image), (self.__blur__, self.__blur__, 0))
		
    def get_transformed_YOLO_values(self, center_x: float, center_y: float, width: float, height: float):       	
        return center_x, center_y, width, height

    def get_augmenter_signature(self):
        return "BLUR"
