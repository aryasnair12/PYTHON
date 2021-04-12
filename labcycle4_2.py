class Bank_ac:

    def __init__(self,ac_no,Name,Type_of_ac):
        self.ac_no=ac_no
        self.Name=Name
        self.Type_of_ac=Type_of_ac
        self.Balence=0

    def deposit(self):
        Amount=float(input("Enter the amount to deposit"))
        self.Balence=self.Balence+Amount
        print("you are deposited amount is",Amount)

    def display(self):
        print("Available balence in your Account is",self.Balence)

    def withdraw(self):
        Amount=float(input("Enter the amount to withdarw"))
        if(self.Balence>Amount):
            self.Balence=self.Balence-Amount
        else:
            print("Insufficient balence")


arya=Bank_ac(198009876556,"Arya","saving")
arya.deposit()
arya.display()
arya.withdraw()
arya.display()


abhi=Bank_ac(198765553422,"Abhi Dev","current")
abhi.deposit()
abhi.display()
abhi.withdraw()
abhi.display()
