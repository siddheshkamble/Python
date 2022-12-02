import os
from sys import *

def Directory_Watcher(path,extention):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    
    exists = os.path.isdir(path)        

    if exists:
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder name is :" +foldername)
       
            for filen in filname:
                if filen.lower().endswith(extention):
                    print(filen)
    
    else:
        print("Invalid Path")

def main():
    print("Directory watcher application")

    if(len(argv) < 3):
        print("Insufficient Argument")
        exit()

    if(argv[1] == "-h"):
        print("This script will tavel the directory and display the size of file")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Directory_Name")
        exit()
    try:
        Directory_Watcher(argv[1],argv[2])

    except ValueError:
        print("Error : Invalid datatypes of input")
    
    except Exception:
        print("Error : Invalid Input")

if __name__ =="__main__":
    main()