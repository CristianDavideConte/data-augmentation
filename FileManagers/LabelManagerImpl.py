from FileManagers.LabelManager import LabelManager
from FileManagers.ImageManager import ImageManager

from typing import Callable

class LabelManagerImpl(LabelManager):

    def __init__(self, labels_path: str, image_manager: ImageManager):
        self.__labels_path__ = labels_path
        self.__image_manager__ = image_manager
    
    def get_YOLO_file_from_image_path(self, path: str):
        yolo_filename: str = self.__image_manager__.get_image_name_from_path_no_ext(path) + ".txt"
        return self.get_all_files_in_path_and_subdirs(self.__labels_path__, (yolo_filename,))[0] #the comma makes it a tuple      

    def get_YOLO_file_name(self, path: str):
        return path.split("/")[-1] 
    
    def get_YOLO_file_name_no_ext(self, path: str):
        return self.get_YOLO_file_name(path).split(".")[0]

    def read_YOLO_file(self, path: str, on_file_opened: Callable, on_line_read: Callable, on_eof: Callable):
        with open(path) as yolo_file:
            on_file_opened()
            for line in yolo_file:
                on_line_read(line)

        on_eof()