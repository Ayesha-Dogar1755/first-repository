class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number=account_number
        self.owner_name=owner_name
        self.balance=balance

        def deposit(self,amount):
            if amount>0:
                self.balance += amount
                print("Amount deposited:",amount)
            else:
                print("Invalid deposit amount")
        def withdraw(self,amount):
            if amount<=self.balance:
             self.balance -= amount
             print("Withdraw successful")
            else:
             print("Insufficient balance")
        def check_balance(self):
           print("Current balance:",self.balance)

Customer1=BankAccount("123456","John Doe",1000)
print("Account Number:",Customer1.account_number)
print("Owner Name:",Customer1.owner_name)
print("Initial Balance:",Customer1.balance)
Customer1.deposit(500)
Customer1.withdraw(200)
Customer1.check_balance()