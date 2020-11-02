# Please fill the wallet class according to the writeup.
class Wallet():
    def __init__(self):
        self.amount = 0

    def addAmount(self, amount):
        if(amount < 0):
            return "Amount can't be negative"
        else:
            self.amount = self.amount +amount
            return float(self.amount)

    def payAmount(self, amount):
        if(amount < 0):
            return "Amount can't be negative"
        elif(self.amount >= amount):
            self.amount = self.amount - amount
            return float(self.amount)
        else:
            return "Insufficient funds"

    def checkBalance(self):
        return float(self.amount)


# Don't change the below code
n = int(input())
w = Wallet()
for i in range(n):
    s = input().split(" ")
    if(s[0] == 'payAmount'):
        print(w.payAmount(float(s[1])))
    elif(s[0] == 'addAmount'):
        print(w.addAmount(float(s[1])))
    elif(s[0] == 'checkBalance'):
        print(w.checkBalance())



