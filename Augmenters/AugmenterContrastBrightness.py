from Augmenters.Augmenter import Augmenter
from PIL import Image

try: #test for full-gpu support
    import cupy as np 
    from cupyx.scipy import ndimage 
    from cupyx.scipy.ndimage.filters import gaussian_filter
except:
    import numpy as np

class AugmenterContrastBrightness(Augmenter):

	def __init__(self, contrast_index: float = 0, brightness_index: float = 0):
		self.__contrast_index__ = contrast_index
		self.__brightness_index__ = brightness_index

	def transform(self, image: Image):
		image_arr = self.get_array_from_image(image)
		return np.array(np.clip(image_arr * (self.__contrast_index__ / 127 + 1) - self.__contrast_index__ + self.__brightness_index__, 0, 255), 
						np.int8)
    
	def get_transformed_YOLO_values(self, center_x: float, center_y: float, width: float, height: float):       	
		return center_x, center_y, width, height

	def get_augmenter_signature(self):
		return "CSTBR"
    