# Exercise 1: Profit Margin Calculator with float inputs
# Prompt the user for inputs
revenue = float(input("Enter revenue: "))
cost = float(input("Enter cost: "))

# Calculate profit
profit = revenue - cost

# Calculate margin safely
if revenue > 0:
    margin = (profit / revenue) * 100
    print(f"Profit: ${profit:.2f} | Margin: {margin:.2f}%")
else:
    print("Invalid revenue.")
