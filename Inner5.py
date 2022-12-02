def Substraction(No1,No2):      #200
    Ans = 0
    Ans = No1 - No2
    return Ans

def Decorated_Function(Function_Name):      #Function_Name =200
    def Inner(A,B):     #300
        if(A<B):
            A,B = B,A
        Output = Function_Name(A,B)       #200(12,8)
        return Output
    return Inner        #retun 300

def main():     #100`
    Value1 = int(input("Enter 1st number : "))      #8
    Value2 = int(input("Enter 2nd number : "))      #12

    New_Function = Decorated_Function(Substraction)     #Decorated_Function(200)
    Ret = New_Function(Value1,Value2)    #Ret = print(300(8,12))
    print("Substraction is :", Ret)
if __name__=="__main__":
    main()      #call 100()
