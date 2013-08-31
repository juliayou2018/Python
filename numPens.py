def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    # Your Code Here
    if n == 0:
        return True
    for i in (5, 8, 24):
        if n >= i and numPens(n - i):
            return True
    return False
