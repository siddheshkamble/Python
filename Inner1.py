
def Hello():
    print("Inside Hello")

    def Demo():                 #inner function
        print("Inside Demo")

    Demo()

Hello()