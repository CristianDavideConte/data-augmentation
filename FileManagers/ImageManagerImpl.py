from FileManagers.FileManager import FileManager
from FileManagers.ImageManager import ImageManager

class ImageManagerImpl(ImageManager):
    
    def __init__(self, valid_exts: (str) = (".jpg", ".jpeg",)):
        self.__valid_exts__: (str) = valid_exts

    def get_all_images_in_path(self, path: str):
        return self.get_all_files_in_path(path, self.__valid_exts__)

    def get_all_images_in_path_and_subdirs(self, path: str):
        return self.get_all_files_in_path_and_subdirs(path, self.__valid_exts__)

    def get_image_name_from_path(self, path: str):
        return path.split(self.os_separator)[-1]

    def get_image_name_from_path_no_ext(self, path: str):
        return self.get_image_name_from_path(path).split(".")[0]
    


    