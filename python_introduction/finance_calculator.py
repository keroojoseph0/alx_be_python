monthly_income = int(input("Enter your monthly incoe: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_saving = monthly_income - monthly_expenses
projected_savings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)

print(f"Your monthly savings are ${monthly_saving}")
print(f"Projected saavings after one year, with interst, is: ${projected_savings}")
