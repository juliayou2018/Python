import pylab

inFile = open('julyTemps.txt')
highTemp = []
lowTemp = []
diffTemps = []
average = []
for line in inFile:
    fields = line[:-1].split(' ')
    if (len(fields) < 3) or not fields[0].isdigit():
        continue
    else:
        highTemp.append(fields[1])
        lowTemp.append(fields[2])

for i in range(31):
        average.append((int(highTemp[i]) + int(lowTemp[i]))/2)

def producePlot(lowTemps, highTemps):
    for i in range(31):
        diffTemps.append(int(highTemp[i]) - int(lowTemp[i]))
producePlot(highTemp, lowTemp)

pylab.figure('Day by Day Ranges in Temperature in Boston in July 2012')
pylab.title('Day by Day Ranges in Temperature in Boston in July 2012') 
pylab.xlabel("Days")
pylab.ylabel("Temperature Ranges")
pylab.plot(range(1,32), highTemp, 'r', label="High")
pylab.plot(range(1,32), lowTemp, 'b', label="Low")
pylab.plot(range(1,32), average,'m--', label = "Average")
pylab.plot(range(1,32), diffTemps,'g', label = "Difference")
pylab.legend(loc=2, borderaxespad=0.)
pylab.axis([0, 32, 0, 120])
pylab.show()

