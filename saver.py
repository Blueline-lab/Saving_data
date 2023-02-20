## This Python file uses the following encoding: utf-8
#Saver 07.06.2021
#saving files periodically

#--------------------------------------------

#modules
import os
from shutil import copytree, rmtree
from filecmp import dircmp
import config
import hashlib
import csv
import zlib
import time


class Saving:

    def __init__(self):
        self.dest = config.destination_path
        self.source = config.source_path
        self.dest2 = config.destination_path2
        #destination path from config file


    def log(self, value):      #some logs, find it in LOGS.txt
        with open("logs.txt", "a") as logs:
            logs.writelines(f"{value}\n")
            logs.close()

    def compress(self, data):
        return zlib.compress(data)

    def copy_machine(self):         #Copy Fucntion
       
        try:
            copytree(self.source, self.dest)
            self.log(f"Copy from {self.source} on {self.dest}")
        except:
            self.log(f"______________________Error in copy_disk to backup1")

        try:
            copytree(self.dest, self.dest2)
            self.log(f"Copy from {self.dest} on {self.dest2}")
        except:
            self.log(f"Error in copy_disk to backup2___________________________")

    

    def tree(self):     #tree command 
        tree = os.path.getmtime(self.source)
        return str(tree)


    def generate_hash_path(self, tree_to_hash):        #generate hash 
        hash1 = hashlib.sha256(str(tree_to_hash).encode(encoding="UTF-8"))
        return str(hash1.digest())

    def write_csv(self,value):      #write the hash
        with open('key.csv', 'w', newline='') as s:
            field = ['hash = ']
            write = csv.DictWriter(s, fieldnames=field)
            write.writeheader()
            write.writerow({'hash = ':str(value)})

    def read_csv(self):         #read the last hash for compare
      with open('key.csv', 'r') as key:
        read = csv.DictReader(key)
        for i in read:
            hash = i['hash = ']
        return str(hash)

    def remove_old_backup(self):
        backup = config.mount
        listsource = os.listdir(backup)
        time_stamp = time.time()
        for i in listsource:
            timestamp_modification = os.path.getmtime(f"{backup}{config.os}{i}")     ###  / a changer sous windows pour \
            days_past = time_stamp - config.day_before_delete_data
            if timestamp_modification < days_past:
                try :
                    rmtree(f"{config.mount}{config.os}{i}")
                    rmtree(f"{config.mount2}{config.os}{i}")
                    self.log("Remove backup 10days old from backup1 and backup2")
                except:
                    self.log("ERROR Cannot remove data 10days old")
 


       
    
        

   
            
       
            


    
        



        





    






