class user():
    def __init__(self,Name,Age,Gender,CNIC):
        self.Name = Name
        self.Age = Age
        self.Gender = Gender
        self.CNIC = CNIC
    def showdetails(self):
        print("The name is:",self.Name, "\nAge :", str(self.Age), "\nGender: ", self.Gender, "\nCNIC is: " , str(self.CNIC))
class Bank(user):
    def __init__(self, Name, Age, Gender, CNIC):
        super().__init__(Name, Age, Gender, CNIC)
        self.balance = 0
    def Deposite(self):
        amount = int(input("Please enter the amount you want to deposite: "))
        self.amount = amount
        self.balance = self.balance+self.amount
        print("Updated balance is:", self.balance)
    def Withdraw(self):
        amount = int(input("Please enter the amount you want to withdraw: "))
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Balance | Available Balance: ", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Your Balance has been updated to : ", self.balance)
    def viewbalance(self):
        self.showdetails()
        print("Account balance is: ", self.balance)




