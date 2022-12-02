import os
from sys import *

def Directory_Watcher(path):
    print("Inside directory watcher method")
    print("Name of input directory :", path)

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    
    exists = os.path.isabs(path)

    if exists:
        for foldername, subfolder, Filenames in os.walk(path):
            print("Folder name is :" +foldername)

            for subf in subfolder:
                print("Subfolder name of " +foldername+ "is " +subf)
            
            for fnames in Filenames:
                print("File inside folder " +foldername+" is " +fnames+ "having size",os.path.getsize(fnames))
            print("")
    
    else:
        print("Invalid Path")

def main():
    print("Directory watcher application")

    if(len(argv) < 2):
        print("Insufficient Argument")
        exit()

    if(argv[1] == "-h"):
        print("This script will tavel the directory and display the name of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Directory_Name")
        exit()
    
    Directory_Watcher(argv[1])

if __name__ =="__main__":
    main()