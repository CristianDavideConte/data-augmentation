from Workers.WorkerImpl import WorkerImpl
from FileManagers.ImageManagerImpl import ImageManagerImpl
from FileManagers.LabelManagerImpl import LabelManagerImpl 

from Augmenters.Augmenter import Augmenter
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

from threading import Thread

import random 


# Global variables
#dataset_dir: str = "../dataset/"
#yolo_labels_dir: str = "../dataset/Labels/YOLO/"
dataset_dir: str = "/content/dataset/"
yolo_labels_dir: str = "/content/dataset/Labels/YOLO/"

image_manager: ImageManagerImpl = ImageManagerImpl()
label_manager: LabelManagerImpl = LabelManagerImpl(yolo_labels_dir, image_manager)



def __get_random_int_avoiding_zero__(lower_bound: int, upper_bound: int, threshold_from_zero: int):
    return random.choice([random.randint(lower_bound, -threshold_from_zero), random.randint(threshold_from_zero, upper_bound)])

def __get_random_float_avoiding_zero__(lower_bound: float, upper_bound: float, threshold_from_zero: float):
    return round(random.choice([random.uniform(lower_bound, -threshold_from_zero), random.uniform(threshold_from_zero, upper_bound)]), 2)

def __execute_job__(augmenter: Augmenter, image_path: str):
    global image_manager, label_manager
    WorkerImpl(augmenter, image_manager, label_manager).transform_image_and_YOLO_label(image_path)
    print(augmenter.get_augmenter_signature(), image_path)

def spawn_worker(subject_dir: str, subject_num: str):
    global dataset_dir, yolo_labels_dir, image_manager, label_manager

    workers = []
    images_paths = image_manager.get_all_images_in_path_and_subdirs(dataset_dir + subject_dir)
 
    for image_path in images_paths:
        contrast: AugmenterContrastBrightness = AugmenterContrastBrightness(__get_random_int_avoiding_zero__(-90, 90, 10), __get_random_int_avoiding_zero__(-90, 90, 10))
        traslate: AugmenterTraslate = AugmenterTraslate(__get_random_int_avoiding_zero__(-70, 70, 20), __get_random_int_avoiding_zero__(-70, 70, 20))
        rotate_up: AugmenterRotate = AugmenterRotate(__get_random_int_avoiding_zero__(-45, 45, 20))
        rotate_down: AugmenterRotate = AugmenterRotate(random.randint(135, 225))
        h_shear: AugmenterHShear = AugmenterHShear(__get_random_float_avoiding_zero__(-0.40, 0.40, 0.1))
        v_shear: AugmenterVShear = AugmenterVShear(__get_random_float_avoiding_zero__(-0.40, 0.40, 0.1))
        h_flip: AugmenterHFlip = AugmenterHFlip()
        v_flip: AugmenterVFlip = AugmenterVFlip()
        grayscale: AugmenterGrayscale = AugmenterGrayscale()
        scale: AugmenterScale = AugmenterScale(round(random.uniform(0.4, 1.4), 2))
        blur: AugmenterBlur = AugmenterBlur(random.randint(10, 15))
        noise: AugmenterNoise = AugmenterNoise(random.randint(10, 20)) # <--------------------------YET TO BE TESTED

        workers.append(Thread(target = __execute_job__, args = (contrast, image_path)))
        workers.append(Thread(target = __execute_job__, args = (traslate, image_path)))
        workers.append(Thread(target = __execute_job__, args = (rotate_up, image_path)))
        workers.append(Thread(target = __execute_job__, args = (rotate_down, image_path)))
        workers.append(Thread(target = __execute_job__, args = (h_flip, image_path)))
        workers.append(Thread(target = __execute_job__, args = (v_flip, image_path)))
        workers.append(Thread(target = __execute_job__, args = (h_shear, image_path)))
        workers.append(Thread(target = __execute_job__, args = (v_shear, image_path)))
        workers.append(Thread(target = __execute_job__, args = (scale, image_path)))
        workers.append(Thread(target = __execute_job__, args = (grayscale, image_path)))
        workers.append(Thread(target = __execute_job__, args = (blur, image_path)))
        workers.append(Thread(target = __execute_job__, args = (noise, image_path)))

    for worker in workers:
        worker.start()

    for worker in workers:
        worker.join()
    
    print("Done with Subject", subject_num)




# Main Script:
# for each subject'image
# create N augmenters
# create N threads
# each thread should spawn 1 worker
# each worker should augment 1 image with 1 augmenter 
for i in range(1, 43):
    print("Subject", i)
    subject_dir: str = "Subject {}/".format(i)
    spawn_worker(subject_dir, i)