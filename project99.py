import os
import shutil


path = input("enter the path")

list_of_files = os.listdir(path)

ctime = os.stat(path).st_ctime

return ctime
