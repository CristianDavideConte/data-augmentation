from Augmenters.Augmenter import Augmenter
import numpy as np

from PIL import Image
from scipy import ndimage

class AugmenterVFlip(Augmenter):
		
	def __init__(self):
		self.__transformation_matrix__: np.ndarray = np.array([[-1,  0,  0, 0], 
        	                      			      			   [ 0,  1,  0, 0], 
        	                      			       			   [ 0,  0,  1, 0],
        	                                       			   [ 0,  0,  0, 1]])

	def transform(self, image: Image):
		self.__transformation_matrix__: np.ndarray = np.array([[-1,  0,  0, image.height], 
        	                      			       			   [ 0,  1,  0, 0], 
															   [ 0,  0,  1, 0],
															   [ 0,  0,  0, 1]])

		return ndimage.affine_transform(input  = self.get_array_from_image(image),
                 	                    matrix = self.__transformation_matrix__)
    
	def get_transformed_YOLO_values(self, center_x: float, center_y: float, width: float, height: float):       	
		return center_x, 1.0 - center_y, width, height

	def get_augmenter_signature(self):
		return "VFLIP"