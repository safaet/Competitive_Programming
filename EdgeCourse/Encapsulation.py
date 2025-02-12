class Account:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    

acc = Account(1000)


print(acc.__balance)
print(acc.get_balance())