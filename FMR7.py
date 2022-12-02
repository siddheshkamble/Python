from functools import reduce

CheckEven = lambda No : (No % 2 == 0)     

Doubles = lambda No: No*2

Sum = lambda A,B : A + B


def main():
    print("Number of element you want to enter :")
    iSize = int(input())

    Data_Input = []
    print("Please enter the element :")

    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is :",Data_Input)

    Data_Filter = list(filter(CheckEven, Data_Input))

    print ("Data after filter is :", Data_Filter)

    Data_Map = list(map(Doubles, Data_Filter))

    print ("Data after Map is :", Data_Map)

    Data_Sum = reduce(Sum, Data_Map)

    print ("Addition is :", Data_Sum)

if __name__ =="__main__":
    main()