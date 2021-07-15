# *****------------------------------------------------------------------------------------------------------*****
# Description : File contains of common methods related to read, write files and folder manipulations
# Author      : Mohamed Yasik
# Created     : Sep 2021
#
# *****----------------------------------------------------------------------

import os
import json
import logging
import shutil
from _datetime import datetime
from commonUtils.constants import _Const


class FileUtils:
    CONST = _Const

    @staticmethod
    def get_absolute_path(dir_path, file_name):
        pass

    @staticmethod
    def copy_and_move_files_to_other_folder(source, destination):
        """ This method copy and move files from one folder to another folder with timestamp"""
        curr_time = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
        filename = destination + "Reports_" + curr_time
        shutil.move(source, filename)

    @staticmethod
    def logger():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
