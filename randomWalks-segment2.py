class Location(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distForm(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Field(object):

    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new Location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name

import random

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = \
            [(0.0,1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(start.distForm(f.getLoc(d)))

def simWalks(numSteps, numTrials):
    homer = UsualDrunk('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances

def drunkTests(numTrials = 20):
    #random.seed(0) ## debug case for same random numbers
    for numSteps in [10, 100, 1000, 10000]:
    #for numSteps in [0, 1]: ## test cases
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps) + ' steps'
        print ' Mean =', sum(distances)/len(distances)
        print ' Max =', max(distances), 'Min =', min(distances)

import pylab
#pylab.rcParams['lines.linewidth'] = 6
#pylab.rcParams['axes.titlesize'] = 20
#pylab.rcParams['axes.labelsize'] = 20
#pylab.rcParams['xtick.major.size'] = 5
#pylab.rcParams['ytick.major.size'] = 5
#pylab.rcParams['lines.markersize'] = 10

def drunkTestP(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    meanDistances = []
    for numSteps in stepsTaken:
        distances = simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
    pylab.plot(stepsTaken, meanDistances)
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.show()

def drunkTestP1(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    meanDistances = []
    squareRootOfSteps = []
    for numSteps in stepsTaken:
        distances = simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
        squareRootOfSteps.append(numSteps**0.5)
    pylab.plot(stepsTaken, meanDistances, 'b-',
                label = 'Mean distance')
    pylab.plot(stepsTaken, squareRootOfSteps, 'g-.',
                label = 'Square root of steps')
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.legend()
    pylab.show()

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = \
            [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = \
            [(0.0, 0.95), (0.0, -1.0), (1.0, 0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        deltaX = random.random()
        if random.random() < 0.5:
            deltaX = - deltaX
        deltaY = random.random()
        if random.random() < 0.5:
            deltaY = - deltaY
        return (deltaX, deltaY)

def simWalksNew(numSteps, numTrials, dClass):
    homer = dClass('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances

def drunkTestP(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    for dClass in (UsualDrunk, ColdDrunk, EDrunk):
        meanDistances = []
        for numSteps in stepsTaken:
            distances = simWalksNew(numSteps, numTrials, dClass)
            meanDistances.append(sum(distances)/len(distances))
        pylab.plot(stepsTaken, meanDistances,
                    label = dClass.__name__)
        pylab.title('Mean Distance from Origin')
        pylab.xlabel('Steps Taken')
        pylab.ylabel('Steps from Origin')
        pylab.legend(loc = 'upper left')
    pylab.show()

#drunkTestP()
drunkTestP1()