
from helper.helper import *
import os


class Database():
    DATABASE_PATH = 'data/'

    def __init__(self, file_name):
        self.file = os.path.abspath(self.DATABASE_PATH + file_name)
        self.type = os.path.splitext(file_name)[0]
        
    def open_connection(self):
        self.file = Helper.open_file(self.file)

        if None != self.file:
            return Helper.fill_list(self.file, self.type)
        return None

    def close_connection(self):
        if not None == self.file:
            self.file.close()