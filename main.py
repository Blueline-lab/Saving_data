## This Python file uses the following encoding: utf-8
#Saver 07.06.2021
#saving files periodically
#Main script
#run this script with RW privilèges

import datetime
import saver

if __name__== "__main__":

    rool = saver.Saving()
    start = rool.log(f"{datetime.datetime.now()}____start_routine____")
    tree = rool.tree()
    hashtree = str(rool.generate_hash_path(tree))
    read = str(rool.read_csv())
    
    if hashtree != read:
        rool.write_csv(hashtree)
        rool.copy_machine()
    rool.remove_old_backup()   
    end = rool.log("End of routine")



