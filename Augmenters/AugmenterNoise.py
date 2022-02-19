from Augmenters.Augmenter import Augmenter
from PIL import Image

import skimage.util

try:
    import cupy as np
except:
    import numpy as np

class AugmenterNoise(Augmenter):

    def __init__(self, noise_index: float):
        self.__noise_index__: float = abs(noise_index)

    def transform(self, image: Image):
        image_arr: np.ndarray = np.array(skimage.util.img_as_float(image))
        noise: np.ndarray= np.random.normal(loc = 0.0, scale = self.__noise_index__ ** 0.5, size = image_arr.shape)
        n_image: np.ndarray = image_arr + noise
        
        return np.array(255 * np.clip(n_image, 0.0, 1.0), np.uint8)

    def get_transformed_YOLO_values(self, center_x: float, center_y: float, width: float, height: float):
        return center_x, center_y, width, height

    def get_augmenter_signature(self):
        return "NOISE"
