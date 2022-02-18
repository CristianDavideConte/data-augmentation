from abc import ABC, abstractclassmethod
from pathlib import Path

import os
import glob

class FileManager(ABC):

    # "/" on linux
    # "\" on windows
    os_separator = os.path.sep 

    @abstractclassmethod
    def __init__(self):
        pass

    def get_all_files_in_path(self, path: str, patterns: (str)):
        path: str = path if path[-1] == self.os_separator else path + self.os_separator
        files = []
        for ext in patterns:
           for image_rel_path in glob.iglob(pathname = path + "*" + ext):
               files.append(os.path.abspath(image_rel_path))
        
        return files

    def get_all_files_in_path_and_subdirs(self, path: str, patterns: (str)):
        path: str = path if path[-1] == self.os_separator else path + self.os_separator
        files = []
        for ext in patterns:
           for image_rel_path in glob.iglob(pathname = path + "**"+ self.os_separator + "*" + ext, recursive = True):
               files.append(os.path.abspath(image_rel_path))
        
        return files

    def get_parent_dir(self, path: str):
        return str(Path(path).parent.absolute()) + self.os_separator