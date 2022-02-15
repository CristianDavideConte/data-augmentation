from Augmenter import Augmenter
import numpy as np

from PIL import Image
from skimage.util import random_noise

class AugmenterGrey(Augmenter):
		
	def __init__(self, noise: float):
		self.__noise__ = abs(noise)
		self.__transformation_matrix__: np.ndarray = np.array([[1, 0, 0, 0], 
        	                      			       			   [0, 1, 0, 0], 
															   [0, 0, 1, 0],
        	                                       			   [0, 0, 0, 1]])

	def transform(self, image: Image):
		image = random_noise(image, mode = "gaussian", var = self.__noise__)
		return (255 * image).astype(np.uint8)
		
	def get_transformed_label(self, center_x: float, center_y: float, width: float, height: float):       	
		return center_x, center_y, width, height
