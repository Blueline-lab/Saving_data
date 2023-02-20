"""Config file for Saverscript"""
from datetime import date 


os = "/" # / for unix systems, \ for Windows systems

mount = "" 
mount2 = ""                 #r"X:\(type str) for windows
source_path =""                                                    #r"D:\(type str)" for windows
destination_path = f"{mount}/Backup_from_{date.today()}"
destination_path2 = f"{mount2}/Backup_from_{date.today()}"

day_before_delete_data = 86000000   # = timestamp 10 days



