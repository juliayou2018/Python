# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
# Jaskirat Singh
# 20 October, 2012


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # FILL IN YOUR CODE HERE...
    value = 0
    for index in range(0, len(poly)):
        value += (poly[index] * (x ** index))
    return float(value)


# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    # FILL IN YOUR CODE HERE...   
    if len(poly) == 1:
        return [0.0]
    deriv = []
    for index in range(1, len(poly)):
        deriv.append(poly[index] * index)
    return deriv


# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    # FILL IN YOUR CODE HERE...
    iters = 0
    root = x_0
    while abs(evaluatePoly(poly, root)) > epsilon:
        iters += 1
        derivative = computeDeriv(poly)
        root = root - (evaluatePoly(poly, root) / evaluatePoly(derivative, root))
    return [root, iters]
