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

contrast: AugmenterContrastBrightness = AugmenterContrastBrightness(+50, 0)
rotate: AugmenterRotate = AugmenterRotate(-70)
traslate: AugmenterTraslate = AugmenterTraslate(50, 70)
h_flip: AugmenterHFlip = AugmenterHFlip()
v_flip: AugmenterVFlip = AugmenterVFlip()
h_shear: AugmenterHShear = AugmenterHShear(0.3)
v_shear: AugmenterVShear = AugmenterVShear(0.3)
scale: AugmenterScale = AugmenterScale(0.5)

dataset_dir: str = "../dataset/"
test_subject_dir: str = "Subject 1/"
yolo_labels_dir: str = "../dataset/Labels/YOLO/"

image_manager: ImageManagerImpl = ImageManagerImpl()
label_manager: LabelManagerImpl = LabelManagerImpl(yolo_labels_dir, image_manager)
worker: Worker = WorkerImpl(scale, image_manager, label_manager)

images_paths = image_manager.get_all_images_in_path_and_subdirs(dataset_dir + test_subject_dir)
test_image_path: str = images_paths[10]
worker.transform_image_and_YOLO_label(test_image_path)

print(test_image_path)
