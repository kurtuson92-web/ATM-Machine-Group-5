# PIN Feature
CORRECT_PIN = "1234"

# User input
user_input = input("Enter your 4-digit PIN: ")

# Checks if matches the PIN
if user_input == CORRECT_PIN:
    print("Access Granted!")
else:
    print("Access Denied. Incorrect PIN.")


# Withdraw
def withdraw(self):
    amount = float(input("Enter amount to be Withdrawn: "))
    if self.balance >= amount:
        self.balance -= amount
        print("\nYou Withdrew:", amount)
    else:
        print("\nInsufficient balance")


# Deposit
def deposit(self):
    amount = float(input("Enter amount to be Deposited: "))
    self.balance += amount
    print("\nAmount Deposited:", amount)
