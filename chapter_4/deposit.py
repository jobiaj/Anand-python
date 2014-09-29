balance = 0

def deposit(int amount):
    global balance
    balance += amount
    return balance

def withdraw(int amount):
    global balance
    balance -= amount
    return balance


print deposit(100)
print balance(50)
