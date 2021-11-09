class Account:
    def __init__(self, id=0, balance=100, annual_interest_rate=0):
        self.__id = int(id)
        self.__balance = float(balance)
        self.__annual_interest_rate = float(annual_interest_rate)

    @property
    def id(self):
        return self.__id
    @property
    def balance(self):
        return self.__balance
    @property
    def annual_interest_rate(self):
        return self.__annual_interest_rate
    
    @id.setter
    def id(self, value):
        self.__id = value
    @balance.setter
    def balance(self, value): 
        self.__balance = value
    @annual_interest_rate.setter
    def annual_interest_rate(self, value):
        self.__annual_interest_rate = value
    
    def get_monthly_interest_rate(self):
        return self.annual_interest_rate / 12

    def get_monthly_interest(self):
        return self.balance * (self.get_monthly_interest_rate() / 100)
        
    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


def main():
    account = Account(1122, 20000, 4.5)
    account.id = 101
    account.withdraw(2500)
    account.deposit(3000)

    print("Account id: ", account.id)
    print("Account balance: ", account.balance)
    print(f"Monthly interest rate: {account.get_monthly_interest_rate()}%")
    print("Monthly interest: ", account.get_monthly_interest())
    

if __name__ == "__main__":
    main()
