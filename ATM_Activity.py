# Simple ATM Withdrawal Simulator

# Initial balance setup
account_balance = 5000.00

print(f"Welcome. Your current available balance is: ${account_balance:.2f}")

try:
    # Prompt the user for the withdrawal amount
    withdraw_amount = float(input("Enter the amount you wish to withdraw: $"))
    
    # Validation checks
    if withdraw_amount <= 0:
        print("Error: Invalid amount. Please enter a value greater than zero.")
        
    elif withdraw_amount > account_balance:
        print("Transaction Declined: Insufficient funds available.")
        
    else:
        # Deduct money and update balance
        account_balance -= withdraw_amount
        print(f"\nSuccess: ${withdraw_amount:.2f} has been dispensed.")
        print(f"Your remaining account balance is: ${account_balance:.2f}")

except ValueError:
    print("Error: Invalid input. Please enter numbers only.")
