from Augmenters.Augmenter import Augmenter
import numpy as np

from PIL import Image
from skimage.util import random_noise

class AugmenterNoise(Augmenter):

    def __init__(self, noise_index: float):
        self.__noise_index__ = abs(noise_index)

    def transform(self, image: Image):
        n_image = random_noise(self.get_array_from_image(image), mode = "gaussian", var = self.__noise_index__)
        return (255 * n_image).astype(np.uint8)
    def get_transformed_YOLO_values(self, center_x: float, center_y: float, width: float, height: float):
        return center_x, center_y, width, height

    def get_augmenter_signature(self):
        return "NOISE"
