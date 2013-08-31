balance = 999999
annualInterestRate = 0.18

low = balance/12.0
high = (balance*(1+ annualInterestRate/12.0)**12)/12.0

epsilon = .01
while True:
    newBalance = balance
    minimumMonthlyPayment = (low + high)/2.0
    for month in range(12):
        newBalance = (newBalance - minimumMonthlyPayment)*(1 + annualInterestRate/12.0)
    if round(newBalance,2) < epsilon:
        high =  minimumMonthlyPayment
    elif round(newBalance, 2) > epsilon:
        low = minimumMonthlyPayment
    else:
        break

print 'Lowest Payment: ' + str(round(minimumMonthlyPayment,2))
