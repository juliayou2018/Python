def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    exposed = 0
    current = start
    while current < stop:
        exposed += f(current) * step
        current += step
    return exposed
