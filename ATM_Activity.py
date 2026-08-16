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


# Main Menu
def main_menu():
    print("========== ATM MACHINE ==========")
    print("1. Balance Check")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Select Option (1-4): "))

    if choice == 1:
        print("You selected Balance Check")
    elif choice == 2:
        print("You selected Deposit")
    elif choice == 3:
        print("You selected Withdraw")
    elif choice == 4:
        print("Goodbye")
    else:
        print("Invalid")


main_menu()