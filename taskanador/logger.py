import os

from datetime import datetime

class Logger:
    
    project_name = "Final_Project"

    __dir_path = os.path.join(os.getcwd(),"logs")
    __file_path = os.path.join(__dir_path,"log.txt")
    
    def __init__(self):
        self.create_files()

    def create_files(self):
        if not os.path.isdir(self.__dir_path):
            os.mkdir(self.__dir_path)
   
        if not os.path.isfile(self.__file_path):
            with open(self.__file_path,"w") as f:
                f.write("\n")

    def add_timestamp(self):
        now = datetime.now()#
        return now.strftime("%Y-%m-%d [ %H:%M:%S ]")

    def add_log(self,log_msg:str):
        try:
            with open(self.__file_path,"a") as  f:
                f.write(f"{self.add_timestamp()} => {log_msg}")
        except FileNotFoundError:
            print("Logs file não encontrado\n")
