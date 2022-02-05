from Augmenters.Augmenter import Augmenter
from FileManagers.ImageManager import ImageManager
from FileManagers.LabelManager import LabelManager
from Workers.Worker import Worker
from PIL import Image

class WorkerImpl(Worker):
    
    def __init__(self, augmenter: Augmenter, image_manager: ImageManager, label_manager: LabelManager):
        self.__augmenter__: Augmenter = augmenter
        self.__image_manager__: ImageManager = image_manager
        self.__label_manager__: LabelManager = label_manager

    #transformation steps:
    # 1) get the image path
    # 2) get the corresponding yolo file path
    # 3) open the image
    # 4) transform the image
    # 5) read the yolo file and transform the lines
    # 6) save the image
    # 7) save the new yolo file
    def transform_image_and_YOLO_label(self, path: str):
        image_dir: str = self.__image_manager__.get_parent_dir(path)
        image_name: str = self.__image_manager__.get_image_name_from_path_no_ext(path) 
        
        yolo_file_path: str = self.__label_manager__.get_YOLO_file_from_image_path(path)
        yolo_dir: str = self.__label_manager__.get_parent_dir(yolo_file_path)
        
        augmenter_signature: str = "_" + self.__augmenter__.get_augmenter_signature()
        augmented_image_path: str = image_dir + image_name + augmenter_signature + ".jpg"

        augmented_yolo_file_name: str = image_name + augmenter_signature + ".txt"
        augmented_yolo_file_path: str = yolo_dir + augmented_yolo_file_name
        augmented_yolo_lines = []
                 
        with Image.open(path) as image:
            augmented_image: Image = self.__augmenter__.get_image_from_array(self.__augmenter__.transform(image))            
            augmented_image.save(augmented_image_path, "JPEG")

        self.__label_manager__.read_YOLO_file(path = yolo_file_path, 
                                                on_file_opened = lambda: self.__create_new_YOLO_file__(augmented_yolo_file_path), 
                                                on_line_read = lambda line: augmented_yolo_lines.extend(self.__get_transformed_YOLO_line__(line)),
                                                on_eof = lambda: self.__write_transformed_YOLO_lines__(augmented_yolo_lines))

    def __create_new_YOLO_file__(self, path: str):
        pass

    def __get_transformed_YOLO_line__(self, original_line: str):
        return []
    
    def __write_transformed_YOLO_lines__(self, lines):
        pass