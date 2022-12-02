import os
from sys import *

def Directory_Watcher(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    
    exists = os.path.isdir(path)      

    if exists:
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder name is :" +foldername)

            for subf in subfolder:
                print("Subfolder name of " +foldername+ "is "+subf)
            
            for filen in filname:
                print("File inside folder " +foldername+" is "+filen)
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
    try:
        Directory_Watcher(argv[1])

    except ValueError:
        print("Error : Invalid datatypes of input")
    
    except Exception:
        print("Error : Invalid Input")

if __name__ =="__main__":
    main()