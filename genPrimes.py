def genPrimes():
    listOfPrimes = []
    prime = 1
    while True:
        prime += 1
        for i in listOfPrimes:
            if prime % i == 0:
                break
        else:
            listOfPrimes.append(prime)
            yield prime
            
