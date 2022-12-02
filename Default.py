
def Area(Radius, PI = 3.14):
    Result = PI * Radius * Radius
    return Result

def main():
    RValue = 10.5
    PIValue = 3.14

    Ans = Area(RValue, PIValue)              # positional argument
    print("Area of Circle is :", Ans)
   
    Ans = Area(PI = PIValue, Radius = RValue)  # Keyword argument
    print("Area of Circle is :", Ans)

    Ans = Area(10.5)                        #postional & default
    print("Area of Circle is :", Ans)

    Ans = Area(Radius = 10.5)                #keyword & default
    print("Area of Circle is :", Ans)

    Ans = Area(PI = 7.10, Radius = 10.5)    #keyword
    print("Area of Circle is :", Ans)

if __name__=="__main__":
    main()