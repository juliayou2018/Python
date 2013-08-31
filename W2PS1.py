balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
total = 0
montlyInterestRate = annualInterestRate/12.0
for month in range(1, 13):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    montlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = montlyUnpaidBalance + (montlyInterestRate*montlyUnpaidBalance)
    total += minimumMonthlyPayment
    
    print('Month: ' + str(month))
    print('Minimum monthly payment: ' + str(round(minimumMonthlyPayment, 2)))
    print('Remaining balance: ' + str(round(balance, 2)))

print('Total paid: ' + str(round(total, 2)))
print('Remaining balance: ' + str(round(balance, 2)))
