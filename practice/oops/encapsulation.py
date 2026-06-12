class BankAccount:
    def __init__(self, balance, name):
        self.__balance = balance
        self._name = name

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
    

bank = BankAccount(5000, "Rahul")
bank.deposit(1000)
print(bank.get_balance())
print(bank._name)
# print(bank.__balance) -> will give an error

'''
no underscore = public
single underscore = protected [can be accessed in the same file]
double underscore = private [can only be accessed in the class only]
'''