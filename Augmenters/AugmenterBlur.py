from Augmenters.Augmenter import Augmenter

from PIL import Image
from scipy.ndimage.filters import gaussian_filter

class AugmenterBlur(Augmenter):
    def __init__(self, blur: float):
        self.__blur__ = abs(blur)

    def transform(self, image: Image):
        return gaussian_filter(image, (self.__blur__, self.__blur__, 0))
		
    def get_transformed_label(self, center_x: float, center_y: float, width: float, height: float):       	
        return center_x, center_y, width, height
