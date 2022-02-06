from Testers.Tester import Tester
from Workers.Worker import Worker
from Workers.WorkerImpl import WorkerImpl
from FileManagers.ImageManagerImpl import ImageManagerImpl
from FileManagers.LabelManagerImpl import LabelManagerImpl 

from Augmenters.AugmenterContrastBrightness import AugmenterContrastBrightness
from Augmenters.AugmenterHFlip import AugmenterHFlip
from Augmenters.AugmenterVFlip import AugmenterVFlip
from Augmenters.AugmenterRotate import AugmenterRotate
from Augmenters.AugmenterTraslate import AugmenterTraslate
from Augmenters.AugmenterHShear import AugmenterHShear
from Augmenters.AugmenterVShear import AugmenterVShear
from Augmenters.AugmenterScale import AugmenterScale

from PIL import Image

contrast: AugmenterContrastBrightness = AugmenterContrastBrightness(30, 30)
traslate: AugmenterTraslate = AugmenterTraslate(-50, -50)
rotate: AugmenterRotate = AugmenterRotate(-90)
h_flip: AugmenterHFlip = AugmenterHFlip()
v_flip: AugmenterVFlip = AugmenterVFlip()
h_shear: AugmenterHShear = AugmenterHShear(0.3)
v_shear: AugmenterVShear = AugmenterVShear(-0.3)
scale: AugmenterScale = AugmenterScale(0.5)

dataset_dir: str = "../dataset/"
test_subject_dir: str = "Subject 1/"
yolo_labels_dir: str = "../dataset/Labels/YOLO/"

image_manager: ImageManagerImpl = ImageManagerImpl()
label_manager: LabelManagerImpl = LabelManagerImpl(yolo_labels_dir, image_manager)
worker: Worker = WorkerImpl(traslate, image_manager, label_manager)

images_paths = image_manager.get_all_images_in_path_and_subdirs(dataset_dir + test_subject_dir)
test_image_path: str = images_paths[1]
yolo_file_path: str = label_manager.get_YOLO_file_from_image_path(test_image_path)
augmented_image_path, augmented_yolo_file_path = worker.transform_image_and_YOLO_label(test_image_path)

print(test_image_path, augmented_image_path,yolo_file_path, augmented_yolo_file_path, sep = "\n")

tester: Tester = Tester(traslate, 3) 

with Image.open(test_image_path) as image:
    image = image.rotate(worker.__get_initial_rotation__(image), expand = True)
    #tester.set_draw_on_image(True)
    tester.set_outline_color("red")
    original_image: Image = tester.test_original_values(image, 0.526933, 0.510320, 0.518814, 0.501350)
    original_image.save("test_image_draw.jpg", "JPEG")

with Image.open(augmented_image_path) as image:
    #tester.set_draw_on_image(False)
    tester.set_outline_color("red")
    original_image: Image = tester.test_original_values(image, 0.526933, 0.510320, 0.518814, 0.501350)
    tester.set_outline_color("blue")
    transformed_image: Image = tester.test_original_values(original_image, 0.526933, 0.510320, 0.518814, 0.617779)
    transformed_image.save("test_augmented.jpg", "JPEG")

