#Instance cariable: Name, Amount, Address, Account No
# Instance method: CreateAccount(), DisplayAccountInfo()
# Class variable : Bank_Name, ROI_On_FD

class Bank_Account:

    Bank_Name = "HDFC Bank PVT LTD"
    ROI_On_FD = 6.7

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your name :")
        self.Name = input()

        print("Enter your initial amount :")
        self.Amount = int(input())

        print("Enter your Address :")
        self.Address = input()

        print("Enter your Account Number :")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("----Your Account Information is as below :----")
        print("Name of Account Holder :", self.Name)
        print("Account Number of Account Holder :", self.AccountNo)
        print("Address of Account Holder :", self.Address)
        print("Current Amount of Account Holder :", self.Amount)
             
def main():

    print("Name of the Bank :", Bank_Account.Bank_Name)
    print("Rate of Interest on Fixed Deposit :", Bank_Account.ROI_On_FD)

    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating the 1st account")
    User1.CreateAccount()

    print("Creating the 2nd account")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

if __name__=="__main__":
    main()