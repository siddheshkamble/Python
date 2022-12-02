from functools import reduce

def main():
    print("Number of element you want to enter :")
    iSize = int(input())

    Data_Input = []
    print("Please enter the element :")

    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is :",Data_Input)

    Data_Filter = list(filter(lambda No : (No % 2 == 0) , Data_Input))

    print ("Data after filter is :", Data_Filter)

    Data_Map = list(map(lambda No: No*2, Data_Filter))

    print ("Data after Map is :", Data_Map)

    Data_Sum = reduce(lambda A,B : A + B, Data_Map)

    print ("Addition is :", Data_Sum)

if __name__ =="__main__":
    main()