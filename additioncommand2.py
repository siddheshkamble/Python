#Addition of twon numbers by command line arguments

from sys import *

def Addition(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    print("Welcome to :", argv[0])

    if(len(argv) == 2):
        if (argv[1] =="--U"):
            print("Use the application as :")
            print("python Name_Of_Application First_number Second_number")
            exit()

        if (argv[1] =="--H"):
            print("Help : This application use to perform addition of two numbers :")
            exit()

    if(len(argv) != 3):
        print("Invalid number of arguments")
        print("Please use --U flag to get the usage")
        exit()

#   print("Application name is :",argv[0])
    X = (int(argv[1]))
    Y = (int(argv[2]))
    Ret = 0

    Ret = Addition(X,Y)

    print("Addition is :",Ret)
    print("THANK YOU FOR USING THE APPLICATION")
    print("SIDDHESH KAMBLE")
    
if __name__ =="__main__":
    main()
