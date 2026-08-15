
CORRECT_PIN = "1234"


user_input = input("Enter your 4-digit PIN: ")

# Check if the input matches
if user_input == CORRECT_PIN:
    print("Access Granted!")
else:
    print("Access Denied. Incorrect PIN.")
