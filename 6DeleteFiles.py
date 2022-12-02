import os
from sys import *
import hashlib
import time

def DeleteFiles(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    iCnt = 0

    if(len(results)>0):
        for result in results:
            for subresult in result:
                iCnt+=1
                if iCnt >= 2:
                    os.remove(subresult)
            iCnt = 0
    else:
        print("No duplicate files found.")

def hashfile(path, blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def findDup(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)
    
    exists = os.path.isdir(path)      

    dups = {}

    if exists:
        for dirName, subdirs, fileList in os.walk(path):          
            print("Current folder is :"+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        
        return dups  
    else:
        print("Invalid Path")

def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicate Found:")
        print("The following files are duplicate")
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
    else:
        print("No duplicate files found")

def main():
    print("----Siddhesh Kamble----")

    print("Application name :"+argv[0])

    if(len(argv) != 2):
        print("Error : Insufficient number of argument")
        exit()

    if((argv[1]=="-h") or (argv[1]=="-H")):
        print("This script will tavel the specific directory and display size of file")
        exit()

    if((argv[1]=="-u") or (argv[1]=="-U")):
        print("Usage : Application_name AbsolutePath_Of_Directory Extension")
        exit()

    try:
        arr = {}
        startTime = time.time()
        arr = findDup(argv[1])
        printResults(arr)
        DeleteFiles(arr)
        endTime = time.time()

        print('Took %s seconds to evaluate.'% (endTime - startTime))

    except ValueError:
        print("Error : Invalid datatypes of input")
    
    except Exception as E:
        print("Error : Invalid Input", E)

if __name__ =="__main__":
    main()