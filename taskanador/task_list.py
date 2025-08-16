import os
import json

from tabulate import tabulate

from task import Task
from logger import Logger

class TaskList:
    
    # build path para o arquivo json que segura todas as tarefas
    project_name = "Final_Project"
    __dir_path = os.path.join(os.getcwd(),"data")
    __file_path = os.path.join(__dir_path,"tasks.json")

    def __init__(self):
        # create a logger 
        self.logger = Logger()
        #create the directories and files necessarios
        self.create_files()

    def create_files(self):
        if not os.path.isdir(self.__dir_path):
            self.logger.add_log(f"Success - folder [ {self.__dir_path} ] was created\n") 
            os.mkdir(self.__dir_path)
        if not os.path.isfile(self.__file_path):
            with open(self.__file_path,"w") as f:
                f.write(json.dumps({
                    "tasks": [],
                    "count": 0,
                }))  
            self.logger.add_log(f"Success - file [ {self.__file_path} ] was created\n") 

    def update_json(self,tasks:list=[],count:int=0):
        task_list = []

        for task in tasks:            
            task_list.append({
                "id": task["id"], 
                "title": task["title"],
                "status": task["status"],
            })

        try:
            # registra no json no formato devido
            with open(self.__file_path,"w") as f: 
                f.write(json.dumps({
                    "tasks": task_list,
                    "count": count,
                }))
                self.logger.add_log(f"Success - the file [ {self.__file_path} ] was updated\n") 

        except FileNotFoundError:
            self.logger.add_log(f"Failed - the file [ {self.__file_path} ] cannot be found\n")

    def get_task_list(self):
        # se nao existir ou o arquivo estiver vazio, chamamos o update que preenche com info basica
        if not os.path.isfile(self.__file_path) or os.path.getsize(self.__file_path) == 0:
            self.update_json()

        try:
            with open(self.__file_path,"r") as f:
                tasks_file = json.load(f)
                self.logger.add_log(f"Success - the file [ {self.__file_path} ] was loaded\n")
                return tasks_file["tasks"], tasks_file["count"]
            
        except FileNotFoundError:
            self.logger.add_log(f"Failed - the file [ {self.__file_path} ] cannot be found\n")
            return [] , 0

    # cria uma task e adiciona a lista
    def add_task(self,title:str):
        # pega os valores das tarefas que ja existem e o id constante atual
        tasks, count = self.get_task_list()
        count += 1
        # cria o objeto Task e sua versao json (necessaria pra serializacao durante o load)
        task = Task(count,title)
        # adiciona a lista de tasks
        tasks.append(task.to_dict())
        # atualiza o json com nova lista e contagem de id
        self.update_json(tasks,count)
        self.logger.add_log(f"Success - the task [ id: {count} | title: {task.title} ] was created\n")
    
    # remove uma task por id
    def remove_task(self,id:int):
        # grab current values
        tasks, count = self.get_task_list()
        
        for i, task in enumerate(tasks):
            if task["id"] == id:
                tasks.remove(task)
                # count -= 1
                self.update_json(tasks,count)
                self.logger.add_log(f"Success - the task [ id: {id} | title: {task["title"]} ] was removed\n")
                return

            if i == len(tasks)-1 and task["id"] != id:
                self.list()
                self.logger.add_log(f"Failed - the task with [ id:{id} ] cannot be found\n")

    def complete_task(self,id:int):       
        # grab current values
        tasks, count = self.get_task_list()
        
        for i, task in enumerate(tasks):
            if task["id"] == id:
                if task["status"] == "pending":
                    task["status"] = "done"
                    self.logger.add_log(f"Success - the task [ id: {id} | title: {task["title"]} ] is done\n")
                else:
                    self.logger.add_log(f"Failed - the task [ id: {id} | title: {task["title"]} ] is already set to done\n")
            elif i == len(tasks)-2 and task["id"] != id:
                self.logger.add_log(f"Failed - the task with [ id: {id} ] cannot be found\n")

        self.update_json(tasks,count)

    def list(self,filter:str="All"):
        
        # grab current values
        tasks, count = self.get_task_list()
        
        # placeholder para o tabulate, uma lista com  todas as tasks em formato de lista
        tasks_fmt = []

        for task in tasks:
            # tabulate nao aceita dicts então convertemos pra uma list de lists
            task_items_list = [task["id"], task["title"], task["status"]]

            # usuario pode filtrar by done or pending
            if filter == "All":
                tasks_fmt.append(task_items_list)
            if filter == "done":
                if task["status"] == filter:
                    tasks_fmt.append(task_items_list)
            if filter == "pending":
                if task["status"] == filter:
                    tasks_fmt.append(task_items_list)
           
        print(tabulate(tasks_fmt,headers=["ID","title","Status"]))
        self.logger.add_log(f"Success - list all [ {filter} ] tasks\n")
