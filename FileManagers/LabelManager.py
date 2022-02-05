from FileManagers.FileManager import FileManager

from abc import abstractclassmethod
from typing import Callable


class LabelManager(FileManager):

    @abstractclassmethod
    def get_YOLO_file_from_image_path(self, path: str):
        pass

    @abstractclassmethod
    def get_YOLO_file_name(self, path: str):
        pass 
    
    @abstractclassmethod
    def get_YOLO_file_name_no_ext(self, path: str):
        pass 
    
    @abstractclassmethod
    def read_YOLO_file(self, path: str, on_file_opened: Callable, on_line_read: Callable, on_eof: Callable):
        pass