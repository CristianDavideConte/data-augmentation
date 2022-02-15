from Augmenter import Augmenter
import numpy as np

from PIL import Image
from scipy import ndimage
from scipy.ndimage.filters import gaussian_filter

class AugmenterGrey(Augmenter):
	def __init__(self, blur: float):
		self.__blur__ = blur
		self.__transformation_matrix__: np.ndarray = np.array([[1,  0,  0, 0], 
        	                      			       		[0, 1,  0, 0], 
        	                      			       		[0,  0,  1, 0],
        	                                       			[0,  0,  0, 1]])

	def transform(self, image: Image):
		image = gaussian_filter(image,(abs(self.__blur__),abs(self.__blur__),0))
		return image
    
	def get_transformed_label(self, center_x: float, center_y: float, width: float, height: float):       	
		return center_x, center_y, width, height
