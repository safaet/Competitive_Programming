class Account:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def update_balance(self, bal):
        self.__balance = bal
    

acc = Account(1000)


# print(acc.__balance)

print(acc.get_balance())

acc.update_balance(200)

print(acc.get_balance())