from Augmenters.Augmenter import Augmenter
from Augmenters.AugmenterRotate import AugmenterRotate
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
            image = image.rotate(self.__get_initial_rotation__(image), expand = True)
            augmented_image: Image = self.__augmenter__.get_image_from_array(self.__augmenter__.transform(image))            
            augmented_image.save(augmented_image_path, "JPEG")

        self.__label_manager__.read_YOLO_file(path = yolo_file_path, 
                                                on_file_opened = lambda: self.__create_new_YOLO_file__(augmented_yolo_file_path), 
                                                on_line_read = lambda line: augmented_yolo_lines.extend(self.__get_transformed_YOLO_line__(line)),
                                                on_eof = lambda: self.__write_transformed_YOLO_lines__(augmented_yolo_file_path, augmented_yolo_lines))

        return augmented_image_path, augmented_yolo_file_path

    def __create_new_YOLO_file__(self, path: str):
        open(path, "w")

    def __get_transformed_YOLO_line__(self, original_line: str):
        original_line_parts = original_line.split(" ")
        center_x, center_y, width, height = self.__augmenter__.get_transformed_YOLO_values(center_x = float(original_line_parts[1]), 
                                                                                           center_y = float(original_line_parts[2]), 
                                                                                           width    = float(original_line_parts[3]), 
                                                                                           height   = float(original_line_parts[4]))
        return [original_line_parts[0] + " " +  "{:.6f}".format(center_x) + " " + "{:.6f}".format(center_y) + " " + "{:.6f}".format(width) + " " + "{:.6f}".format(height)]
        
    def __write_transformed_YOLO_lines__(self, path: str, lines):
        with open(path, "w") as yolo_file:
            for line in lines:
                yolo_file.write(line + "\n")

    def __get_initial_rotation__(self, image: Image):
            try:
                initial_rotation: int = int(dict(image._getexif().items())[274])
                if initial_rotation == 6:
                    return -90
                elif initial_rotation == 8:
                    return 90
            except:
                pass

            return 0