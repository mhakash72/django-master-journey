class BankAccount:
    def __init__(self,holder, initial_balance=1000):
        self.holder_name = holder
        self.balance = initial_balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposit: {amount} \nBalance: {self.balance} ")
        else:
            print("Input valid number")
    def withdraw(self,amount):
        if amount>0:
            if self.balance>=amount:
                self.balance-=amount
                print(f'Withdraw : {amount}\nBalance: {self.balance}')
            else:
                print('Insufficient balance')
    def get_balance(self):
        return self.balance
        
acc = BankAccount("Mehedi")
acc.deposit(500)
acc.withdraw(200)

