# Ask for user imputs
credit_score = int(input("Enter your credit score: "))
annual_income = float(input("Enter your annual income: "))

# Loan Risk Classification
if credit_score >= 720 and annual_income >= 60000:
    risk = "Low Risk"
elif credit_score >= 650 and annual_income >= 40000:
    risk = "Medium Risk"
else:
    risk = "High Risk"

print(f"Loan Risk Classification: {risk}")
