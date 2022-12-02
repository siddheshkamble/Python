# Filter Map Reduse
def CheckEven(No):
    return(No % 2 == 0)

def Increment(No):
    return No+2

def FilterX(Arr,Function_Name):
    Result = []
    for no in Arr:
        if(Function_Name(no)):
            Result.append(no)
    return Result

def MapX(Arr,Function_Name):
    Result = []
    for no in Arr:
        value = Function_Name(no)
        Result.append(value)
    return Result

def ReduseX(Arr):
    Sum = 0
    for no in Arr:
        Sum = Sum + no
    return Sum

def main():
    Data = [2,3,1,6,4,5,11,16,20]
    
    print("Original data :", Data)

    Data_Filter = list(FilterX(Data,CheckEven))

    print("Data after filter :", Data_Filter)

    Data_Map = list(MapX(Data_Filter, Increment))

    print("Data after map :", Data_Map)

    Ret = ReduseX(Data_Map)

    print("Data after reduce :", Ret)

if __name__ == "__main__":
    main()