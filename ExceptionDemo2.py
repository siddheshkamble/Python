import time
import threading

def main():
    try:
        print("Enter 1st Number")
        iNo1 = int(input())

        print("Enter 2nd number")
        iNo2 = int(input())

        Ans = iNo1/iNo2
        print("Division is", Ans)

    except ZeroDivisionError:
        print("Inside zero division error")

    except ValueError:
        print("Inside Value Error")

    except Exception:
        print("Inside last except block")
        
    finally:
        print("Inside finaaly block")

if __name__=="__main__":
    main()
   
