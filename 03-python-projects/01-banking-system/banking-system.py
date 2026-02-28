class Bank:

    def __init__(self):
        self.accounts={}    
        self.next_account_number=1001


    def create_account(self,holder_name, password):
        account_number = self.next_account_number
        self.next_account_number+=1

        account = Account(holder_name, account_number)
        account.set_password(password)

        self.accounts[account_number] = account

        return account


    def find_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        else:
            return self.accounts[account_number]




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



bank = Bank()
acc1 = bank.create_account("vbp", 1234)
acc2 = bank.create_account("buddy", 1234)

print(acc1.account_number)
print(acc2.account_number)

found = bank.find_account(acc1.account_number)
print(found.get_balance())
print(found.holder_name)
