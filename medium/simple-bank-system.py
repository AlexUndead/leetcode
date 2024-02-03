import pdb
from typing import List


class Bank:
    def __init__(self, balance: List[int]):
        self.balance = {index:balance[index - 1] for index in range(1, len(balance) + 1)}

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        balance_1 = self.balance.get(account1)
        balance_2 = self.balance.get(account2)
        if balance_1 is None or balance_2 is None:
            return False

        if balance_1 < money:
            return False

        self.balance[account1] -= money
        self.balance[account2] += money
        return True
        
    def deposit(self, account: int, money: int) -> bool:
        if self.balance.get(account) is not None:
            self.balance[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        balance = self.balance.get(account)
        if balance is not None and balance >= money:
            self.balance[account] -= money
            return True
        return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

#obj = Bank([12, 25, 100, 35])
#assert obj.withdraw(1, 20) == False
#assert obj.withdraw(1, 10) == True
#assert obj.withdraw(5, 10) == False
#assert obj.deposit(5, 10) == False
#assert obj.withdraw(3, 110) == False
#assert obj.deposit(3, 10) == True
#assert obj.withdraw(3, 110) == True
#assert obj.transfer(4, 2, 20) == True
#assert obj.balance[2] == 45
#assert obj.transfer(5, 2, 20) == False
#assert obj.transfer(2, 5, 20) == False
#assert obj.transfer(2, 1, 100) == False
#obj = Bank([10, 100, 20, 50, 30])
#assert obj.withdraw(3, 10) == True
#assert obj.transfer(5, 1, 20) == True
#assert obj.deposit(5, 20) == True
#assert obj.transfer(3, 4, 15) == False
#assert obj.withdraw(10, 50) == False
#obj = Bank([0])
#assert obj.deposit(1, 0) == True
#assert obj.deposit(1, 10) == True
#assert obj.transfer(1, 1, 0) == True
#assert obj.transfer(1, 1, 10) == True
obj = Bank([0])
assert obj.deposit(1, 1000000000000) == True
assert obj.transfer(1, 1, 1000000000000) == True
assert obj.withdraw(1, 1000000000000) == True
assert obj.deposit(1, 0) == True
print(obj.balance)
assert obj.transfer(1, 1, 0) == True
assert obj.withdraw(1, 0) == True
