# Ask for imputs
purchase_amount = float(input("Enter the purchase amount: "))
is_member = input("Is the customer a member? (yes/no): ").lower()

# Determine customer discount
if is_member == "yes" and purchase_amount>= 100:
    discount = 0.15
elif is_member == "yes" and purchase_amount < 100:
    discount = 0.05
elif is_member == "no" and purchase_amount >= 150:
    discount = 0.10
else:    discount = 0.0

# Calculate final price
final_price = purchase_amount * (1 - discount)

# results
print(f"Customer Discount: {discount * 100}%")
print(f"Final Price: ${final_price:.2f}")