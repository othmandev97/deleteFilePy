#1

import os 
from os import listdir


import pathlib
path = pathlib.Path(__file__).parent.absolute()

#path.replace('\', '\\')
print(str(path))
print(str(path).replace('\\',r'\\'))
#2
folder_path = path
#3
for file_name in listdir(folder_path):
    #4
    if file_name.endswith('.sr'):
        #5
        os.remove(folder_path + file_name)