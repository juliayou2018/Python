import pylab

##pylab.figure(1)
##pylab.plot([1,2,3,4],[1,2,3,4])
##pylab.figure(2)
##pylab.plot([1,4,2,3],[5,6,7,8])
##pylab.savefig('Figure-Eric')
##pylab.figure(1)
##pylab.plot([5,6,10,3])
##pylab.savefig('Figure-Grimson')

principal = 10000
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * interestRate
pylab.plot(range(years + 1), values)
pylab.title('5% Growth, Compounded Annually')
pylab.xlabel('Years of Compounding')
pylab.ylabel('Value of Principal')
pylab.show()
