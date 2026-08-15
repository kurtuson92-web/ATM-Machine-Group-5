# Ultra-Simple Withdrawal Code
balance = 5000.00

# 1. Input amount
amount = float(input("Enter withdrawal amount: $"))

# 2. Check and deduct
if amount > balance:
    print("Insufficient funds!")
elif amount <= 0:
    print("Invalid amount!")
else:
    balance -= amount
    print(f"Success! Remaining balance: ${balance}")
