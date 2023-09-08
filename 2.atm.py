def calculate_balance(withdrawal_amount, account_balance):
    # Check if the withdrawal amount is a multiple of 5 and account balance is sufficient
    if withdrawal_amount % 5 == 0 and (withdrawal_amount + 0.5) <= account_balance:
        # Calculate the new balance after withdrawal and bank charges
        new_balance = account_balance - (withdrawal_amount + 0.5)
        return new_balance
    else:
        # If the withdrawal is not possible, return the current balance
        return account_balance

# Input values
withdrawal_amount = int(input("Enter the withdrawal amount: "))
account_balance = float(input("Enter the account balance: "))

# Calculate and print the updated balance
new_balance = calculate_balance(withdrawal_amount, account_balance)
print("Updated account balance:", new_balance)
