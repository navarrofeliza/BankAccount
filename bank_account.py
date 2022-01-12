class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.interest = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("ERROR: Insufficient funds!")
            
    def display_account_info(self):
        print(f"Balance is: ${self.balance}")
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance += round(self.balance*self.interest)
        else:
            print("Unable to pay interest due to lack of funds.")
            
aethel = BankAccount(1.2, 1400)
connor = BankAccount(0.5, 500)

aethel.deposit(5000).deposit(10).deposit(50).withdraw(500).yield_interest().display_account_info()

connor.deposit(3500).deposit(200).withdraw(100).withdraw(300).withdraw(70).withdraw(160).yield_interest().display_account_info()
