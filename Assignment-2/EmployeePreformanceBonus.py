salary = float(input("Enter employee's salary: "))
score = int(input("Enter employee's performance score (0-100): "))

# Bonus Calculation
if 90 <= score <= 100: 
    bonus_rate = .20
elif 80 <= score < 89:
    bonus_rate = .10
elif 70 <= score < 79:
    bonus_rate = .05
else:
    bonus_rate = 0

# Calculate final bonus amount 
bonus_amount = salary * bonus_rate

# results
print(f"Performance Bonus: {int(bonus_rate * 100)}%")
print(f"Bonus Amount: ${bonus_amount:.2f}")