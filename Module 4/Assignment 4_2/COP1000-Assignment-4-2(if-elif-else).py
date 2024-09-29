# Input from the user
employee_name = input("Enter the Employee's Name: ")
number_of_shifts = int(input("Enter the Number of Shifts: "))
number_of_transactions = int(input("Enter the Number of Transactions: "))
transactions_dollar_value = float(input("Enter the Total Transaction Dollar Value: "))

# Calculate productivity score
productivity_score = (transactions_dollar_value/number_of_transactions)/number_of_shifts

# Calculate (Employee Bonus) based on their productivity score
if productivity_score <= 30:
    bonus = 50.00
elif 31 <= productivity_score <= 69:
    bonus = 75.00
elif 70 <= productivity_score <= 199:
    bonus = 100
else:
    bonus = 200

# Output for Employee Bonus
print(f"Employee Name: {employee_name}")
print(f"Employee Bonus: ${bonus:.1f}")