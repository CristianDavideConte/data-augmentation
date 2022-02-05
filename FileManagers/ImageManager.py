from FileManagers.FileManager import FileManager
from abc import abstractclassmethod

class ImageManager(FileManager):
    
    @abstractclassmethod
    def get_all_images_in_path(self, path: str):
        pass

    @abstractclassmethod
    def get_all_images_in_path_and_subdirs(self, path: str):
        pass
        
    @abstractclassmethod
    def get_image_name_from_path(self, path: str):
        pass

    @abstractclassmethod
    def get_image_name_from_path_no_ext(self, path: str):
        pass


    