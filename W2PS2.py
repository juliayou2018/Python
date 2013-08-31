balance = 3926
annualInterestRate = 0.2
minimumMonthlyPayment = 10
while True:
    newBalance = balance
    for month in range(12):
        newBalance = (newBalance - minimumMonthlyPayment)*(1 + annualInterestRate/12.0)
    if newBalance <= 0:
        break
    else:
        minimumMonthlyPayment += 10
print 'Lowest Payment: ' + str(minimumMonthlyPayment)
