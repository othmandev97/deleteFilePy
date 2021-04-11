import os 
from os import listdir
import pathlib
path = pathlib.Path(__file__).parent.absolute()

printed_path = str(path).replace('\\',r'\\')
folder_path = printed_path+'\\' 

end_extension = input('enter the file extension : ')

for file_name in listdir(folder_path):
    if file_name.endswith(end_extension):
        os.remove(folder_path + file_name)
