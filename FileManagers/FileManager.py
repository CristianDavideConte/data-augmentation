from abc import ABC, abstractclassmethod
from pathlib import Path

import os
import glob

class FileManager(ABC):

    @abstractclassmethod
    def __init__(self):
        pass

    def get_all_files_in_path(self, path: str, patterns: (str)):
        path: str = path if path[-1] == "/" else path + "/"
        files = []
        for ext in patterns:
           for image_rel_path in glob.iglob(pathname = path + "*" + ext):
               files.append(os.path.abspath(image_rel_path))
        
        return files

    def get_all_files_in_path_and_subdirs(self, path: str, patterns: (str)):
        path: str = path if path[-1] == "/" else path + "/"
        files = []
        for ext in patterns:
           for image_rel_path in glob.iglob(pathname = path + "**/*" + ext, recursive = True):
               files.append(os.path.abspath(image_rel_path))
        
        return files

    def get_parent_dir(self, path: str):
        return str(Path(path).parent.absolute()) + "/"