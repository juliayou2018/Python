def isPrime(n):
    if n <= 0:
        raise ValueError()
    if type(n) != int:
        raise TypeError()
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True

    
