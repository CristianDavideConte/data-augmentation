from matplotlib.pyplot import draw
from Augmenters.Augmenter import Augmenter
from PIL import Image, ImageDraw

class Tester:

    def __init__(self, augmenter: Augmenter, draw_lines_width: int = 10, outline_color: str = "red"):
        self.__augmenter__: Augmenter = augmenter
        self.__draw_lines_width__: int = draw_lines_width
        self.__outline_color__: str = outline_color 
        self.__draw_on_image: bool = True

    def set_outline_color(self, outline_color: str = "red"):
        self.__outline_color__: str = outline_color 

    def set_draw_on_image(self, draw_on_image: bool = True):
        self.__draw_on_image = draw_on_image

    def draw_rectangle(self, image: Image, left: float, top: float, right: float, bottom: float, outline: str = "red", width: float = 10):
        drawing: ImageDraw = ImageDraw.Draw(image)
        drawing.rectangle([left, top, right, bottom], outline = outline, width = width)
        return image

    def draw_point(self, image: Image, left: float, top: float, right: float, bottom: float, fill: str = "red"):
        drawing: ImageDraw = ImageDraw.Draw(image)
        drawing.ellipse([left, top, right, bottom], fill = fill)
        return image

    def test_original_values(self, image: Image, center_x: float, center_y: float, width: float, height: float):
        img_width, img_height = image.size

        if self.__draw_on_image == True:
            self.draw_point(image,
                            img_width  * center_x - self.__draw_lines_width__, 
                            img_height * center_y - self.__draw_lines_width__, 
                            img_width  * center_x + self.__draw_lines_width__, 
                            img_height * center_y + self.__draw_lines_width__, 
                            fill = self.__outline_color__)

            self.draw_point(image,
                            img_width  / 2 - self.__draw_lines_width__, 
                            img_height / 2 - self.__draw_lines_width__, 
                            img_width  / 2 + self.__draw_lines_width__, 
                            img_height / 2 + self.__draw_lines_width__, 
                            fill = self.__outline_color__)
            self.draw_rectangle(image, 
                                img_width  * (center_x - width  / 2), 
                                img_height * (center_y - height / 2), 
                                img_width  * (center_x + width  / 2), 
                                img_height * (center_y + height / 2),
                                outline = self.__outline_color__, 
                                width = self.__draw_lines_width__)
                                
        return image

    def test(self, image: Image, center_x: float, center_y: float, width: float, height: float):
        t_image: Image = self.__augmenter__.get_image_from_array(self.__augmenter__.transform(image))

        t_center_x, t_center_y, t_width, t_height = self.__augmenter__.get_transformed_YOLO_values(center_x, center_y, width, height) 
        
        return self.test_original_values(t_image, t_center_x, t_center_y, t_width, t_height)

    def get_augmenter_signature(self):
        return self.__augmenter__.get_augmenter_signature()