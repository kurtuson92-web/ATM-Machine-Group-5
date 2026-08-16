#pin value
CORRECT_PIN = "1234"

#acc balance
balance = 10000


#input for pin
user_input = input("Enter your 4-digit PIN: ")

#for matching pin and input pin
if user_input == CORRECT_PIN:
    print("Access Granted!")

    # Main Menu
    while True:
        print("========== ATM MACHINE ==========")
        print("1. Balance Check")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Select Option (1-4): "))

        # Balance Check
        if choice == 1:
            print("Current Balance:", balance)

        # Deposit
        elif choice == 2:
            amount = float(input("Enter amount to be Deposited: "))

            if amount > 0:
                balance += amount
                print("Amount Deposited:", amount)
                print("New Balance:", balance)
            else:
                print("Invalid amount")

        # Withdraw
        elif choice == 3:
            amount = float(input("Enter amount to be Withdrawn: "))

            if balance >= amount:
                balance -= amount
                print("You Withdrew:", amount)
                print("Remaining Balance:", balance)
            else:
                print("Insufficient balance")

        # Exit
        elif choice == 4:
            print("Goodbye")
            break

        else:
            print("Invalid")

else:
    print("Access Denied. Incorrect PIN.")