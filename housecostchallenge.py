# Calculate the EMI

def loan_emi(amount, duration, rate, down_payment = 0):
    loan_amount = amount - down_payment
    emi = loan_amount * rate * ((1 + rate) ** duration) / (((1 + rate) ** duration) - 1)
    return emi

print(round(loan_emi(1260000, 8 * 12, 0.1/12, 3e5)))
print(round(loan_emi(1260000, 10 * 12, 0.08/12)))