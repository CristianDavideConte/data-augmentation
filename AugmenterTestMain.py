import copy

from Augmenters.AugmenterContrastBrightness import AugmenterContrastBrightness
from Augmenters.AugmenterHFlip import AugmenterHFlip
from Augmenters.AugmenterVFlip import AugmenterVFlip
from Augmenters.AugmenterRotate import AugmenterRotate
from Augmenters.AugmenterTraslate import AugmenterTraslate
from Augmenters.AugmenterHShear import AugmenterHShear
from Augmenters.AugmenterVShear import AugmenterVShear
from Augmenters.AugmenterScale import AugmenterScale
from Augmenters.AugmenterBlur import AugmenterBlur
from Augmenters.AugmenterNoise import AugmenterNoise
from Augmenters.AugmenterGrayscale import AugmenterGrayscale
from Augmenters.AugmenterSharp import AugmenterSharp
from Testers.Tester import Tester
from PIL import Image

import random 

contrast: AugmenterContrastBrightness = AugmenterContrastBrightness(+50, 100)
rotate: AugmenterRotate = AugmenterRotate(225)
traslate: AugmenterTraslate = AugmenterTraslate(300, 500)
h_flip: AugmenterHFlip = AugmenterHFlip()
v_flip: AugmenterVFlip = AugmenterVFlip()
h_shear: AugmenterHShear = AugmenterHShear(0.3)
v_shear: AugmenterVShear = AugmenterVShear(-0.4)
scale: AugmenterScale = AugmenterScale(0.5)
blur: AugmenterBlur = AugmenterBlur(10)
noise: AugmenterNoise = AugmenterNoise(0.10)
grayscale: AugmenterGrayscale = AugmenterGrayscale()
sharp: AugmenterSharp = AugmenterSharp(15)

#center_x, center_y, width, height = 0.59, 0.247, 0.085, 0.085 #eye
center_x, center_y, width, height = 0.45, 0.32, 0.76, 0.36 #head
create_original_image = True
test_image_path = "test.jpg" #test.jpg or subject.jpg

with Image.open(test_image_path) as image: 
    tester: Tester = Tester(sharp) #change this in order to test a new augmenter

    if create_original_image == True:
        #tester.set_draw_on_image(True)
        tester.set_outline_color("red")
        original_image: Image = tester.test_original_values(copy.deepcopy(image), center_x, center_y, width, height)
        original_image.save("test_image_draw.jpg", "JPEG")

    #tester.set_draw_on_image(False)
    tester.set_outline_color("blue")
    transformed_image: Image = tester.test(original_image, center_x, center_y, width, height)
    transformed_image.save("test_augmented.jpg", "JPEG")

    print(tester.get_augmenter_signature())


