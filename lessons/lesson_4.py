# принципы ооп инкасуляция абстракция множ наследование

class Bank:
    def __init__(self, name, balance, pin):
        self.name = name
        self._balance = balance
        self.__pin = pin

    def details(self):
        print(f'pin is {self.__pin}')

    def __str__(self):
        return f'name: {self.name}\nbalance: {self._balance}'

    def sbalance(self, new):
        self._balance += new
        print(self._balance)



beka = Bank('bekbolot', 0, '1111')
Bank.details(beka)
beka.__pin = 1222
beka.details()
print(beka.__pin)
beka.details()