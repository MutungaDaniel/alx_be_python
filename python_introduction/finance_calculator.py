#User input for Financial Details
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

#Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

#Project Annual Savings
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

#Display Results
print("Your monthly savings are $",monthly_savings,".")
print("Projected savings after one year, with interest, is: $",projected_savings,".")