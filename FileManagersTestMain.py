from FileManagers.ImageManagerImpl import ImageManagerImpl
from FileManagers.LabelManagerImpl import LabelManagerImpl

dataset_dir: str = "../dataset/"
test_subject_dir: str = "Subject 1/"
images_exts: (str) = (".jpg", ".png") 

yolo_labels_dir: str = "../dataset/Labels/YOLO/"

image_manager: ImageManagerImpl = ImageManagerImpl(images_exts)
label_manager: LabelManagerImpl = LabelManagerImpl(yolo_labels_dir, image_manager)

images_paths = image_manager.get_all_images_in_path_and_subdirs(dataset_dir + test_subject_dir)
test_image_path: str = images_paths[0]
yolo_file: str = label_manager.get_YOLO_file_from_image_path(test_image_path)

label_manager.read_YOLO_file(path = yolo_file, 
                             on_file_opened = lambda path: print("opened yolo file -> " + path + "\n"), 
                             on_line_read = lambda line: print("read line -> " + line), 
                             on_eof = lambda: print("---> EOF <---"))
