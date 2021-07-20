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
from commonutils.constants import _Const


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

    @staticmethod
    def get_environment_config(*args):
        """ Method to read yaml config file
        for nested yaml pass the argument one by one separated with comma
        example: Utils.read_environment_config('environment', 'browser')"""
        with open(FileUtils.get_absolute_file_path(FileUtils.CONST.ENVIRONMENT_CONF_FILE_PATH, 'Environment_conf.yaml'),
                  'r') as doc:

            f_config = yaml.safe_load(doc.read())

            # get section
            section = args[0]

            # check if config file has section
            if not f_config.keys():
                raise ValueError('Key is missing in the conf file')
                quit()

            # get values
            arg_list = list(args)
            arg_list.pop(0)  # remove section from list

            # create lookup path
            parse_path = "f_config['" + section + "']"

            for arg in arg_list:
                parse_path = parse_path + "['" + arg + "']"

            doc.close()
            return eval(parse_path)