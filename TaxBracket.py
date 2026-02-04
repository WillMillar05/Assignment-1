def get_tax_bracket(income):
    if income < 0:
        return "Invalid income.", None

    if income < 50000:
        bracket = "Low (10%)"
        rate = 0.10
    elif income < 100000:
        bracket = "Medium (20%)"
        rate = 0.20
    else:
        bracket = "High (30%)"
        rate = 0.30

    return bracket, rate


# Main
income_input = input("What's your annual income: ")
income = float(income_input.replace(",", ""))

bracket, rate = get_tax_bracket(income)

if bracket == "Invalid income.":
    print(bracket)
else:
    estimated_tax = income * rate
    print(f"Your bracket: {bracket}. Estimated tax: {estimated_tax}")
