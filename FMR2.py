
def main():
    print("Number of element you want to enter :")
    iSize = int(input())

    Data_Input = []
    print("Please enter the element :")

    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is :",Data_Input)

if __name__ =="__main__":
    main()
