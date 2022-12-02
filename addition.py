#Addition of twon numbers by command line arguments

from sys import *

def Addition(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()

#   print("Application name is :",argv[0])
    X = (int(argv[1]))
    Y = (int(argv[2]))
    Ret = 0

    Ret = Addition(X,Y)

    print("Addition is :",Ret)

if __name__ =="__main__":
    main()
