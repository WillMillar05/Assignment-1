# Ask for credit score
credit_score = int(input("Enter your credit score: "))

# Ranges
if credit_score < 300 or credit_score > 850:
    print("Invalid credit score.")
elif credit_score >= 750:
    print("Excellent credit - Loan Approved. Interest rate: Low")
elif 700 <= credit_score < 750:
    print("Good - Loan Approved with Review. Interest rate: Low")
elif 650 <= credit_score < 700:
    print("Fair credit - Loan Approved with Review. Interest rate: Medium")
elif 600 <= credit_score < 650:
    print("Fair - Loan Conditional. Seek credit improvement.")
else:
    print("Very poor credit - Loan Denied.")
