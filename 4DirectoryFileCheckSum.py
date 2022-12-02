import os
from sys import *
import hashlib

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()

    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def DisplayCheckSum(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    
    exists = os.path.isdir(path)      

    if exists:
        for dirName, subfolder, fileList in os.walk(path):
            print("Current folder name is :" +dirName)
            
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print('')
    
    else:
        print("Invalid Path")

def main():
    print("Directory watcher application")

    if(len(argv) < 2):
        print("Insufficient Argument")
        exit()

    if(argv[1] == "-h"):
        print("This script will tavel the directory and display Checksum")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Directory_Name")
        exit()
    try:
        arr = DisplayCheckSum(argv[1])

    except ValueError:
        print("Error : Invalid datatypes of input")
    
    except Exception:
        print("Error : Invalid Input")

if __name__ =="__main__":
    main()