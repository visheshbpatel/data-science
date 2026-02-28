class Account:

    def __init__(self, holder_name, account_number):
        self.holder_name = holder_name
        self.account_number = account_number
        self.__balance = 0
        self.__password = 0


    def deposit(self, amount):
        if amount<=0:
            raise ValueError("Amount must be positive")
        else:
            self.__balance+=amount


    def withdraw(self, amount, password):
        
        if amount>self.__balance:
            raise ValueError("unnsufficient Balance")
        elif amount<=0:
            raise ValueError("Amount must be positive")
        else:
            if self.validate_password(password):
                self.__balance-=amount
            else:
                raise ValueError("Invalid Password")


    def get_balance(self):
        return self.__balance


    def set_password(self, password):
        self.__password = password
    

    def validate_password(self, password):
        return password == self.__password


p1 = Account("vbp",1500)
p1.set_password(1234)
p1.deposit(1000)
p1.withdraw(500, 1234)
print(p1.get_balance())

