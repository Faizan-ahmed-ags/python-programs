import os 
import sys
import pathlib
import zipfile 
dirName = input("Enter the directory name to backup: ")
if not os.path.isdir(dirName):
    print("Directory does not exist")
    sys.exit()
curDir = pathlib.Path (dirName)
with zipfile.ZipFile("myzip.zip,mode='w'") as archive:
    for file_path in curDir.rglob('**/*'):
        print(file_path)
        archive.write(file_path)
        if os.path.isfile("myfile.zip"):
         print("archive myzip.zip created successfully")
        else:  
         print("Error creating zip archive")
