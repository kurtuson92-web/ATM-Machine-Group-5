def main_menu():
    print("==========ATM MACHINE ==========")
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