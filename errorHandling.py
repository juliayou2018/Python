try:
    fout = open('trip.py', 'r')
    val = fout.readline()
    x = int(val)
    print "Rate: " + str(101. / x)
except IOError, e:
    print "Error reading file: " + str(e)
print "Continuing..."