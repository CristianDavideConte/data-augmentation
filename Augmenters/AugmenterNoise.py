from Augmenters.Augmenter import Augmenter
from PIL import Image

import skimage.util

try:
    import cupy as np
except:
    import numpy as np

class AugmenterNoise(Augmenter):

    def __init__(self, noise_index: float):
        self.__noise_index__ = abs(noise_index)

    def transform(self, image: Image):
        image_arr = np.array(skimage.util.img_as_float(image))
        noise = np.random.normal(loc = 0.0, scale = self.__noise_index__ ** 0.5, size = image_arr.shape)
        n_image = image_arr + noise
        n_image = np.clip(n_image, 0.0, 1.0)
        
        return np.array(255 * n_image, np.uint8)

    def get_transformed_YOLO_values(self, center_x: float, center_y: float, width: float, height: float):
        return center_x, center_y, width, height

    def get_augmenter_signature(self):
        return "NOISE"
