#1
import os 
from os import listdir
import pathlib
path = pathlib.Path(__file__).parent.absolute()

printed_path = str(path).replace('\\',r'\\')
#2
#folder_path = path
folder_path = printed_path+'\\'
#3
end_extension = input('enter the file extension : ')

#print(end_extension)
for file_name in listdir(folder_path):
    #4
    if file_name.endswith(end_extension):
        #5
        os.remove(folder_path + file_name)