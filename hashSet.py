class hashSet(object):
    def __init__(self, numBuckets):
        '''
        numBuckets: int. The number of buckets this hash set will have. 
        Raises ValueError if this value is not an integer, or if it is not greater than zero.
        Sets up an empty hash set with numBuckets number of buckets.
        '''
        if type(numBuckets) != int: 
            raise ValueError(str(numBuckets) + ' must be an integer')
        if numBuckets <= 0:
            raise ValueError(str(numBuckets) + ' must be greater than zero')
        self.numBuckets = numBuckets
        self.hashSet = []
        for b in range(numBuckets):
            self.hashSet.append([])

    def hashValue(self, e):
        '''
        e: an integer
        
        returns: a hash value for e, which is simply e modulo the number of 
        buckets in this hash set. Raises ValueError if e is not an integer.
        '''
        if type(e) != int:
            raise ValueError
        return e % self.getNumBuckets()

    def member(self, e):
        '''
        e: an integer
        Returns True if e is in self, and False otherwise. Raises ValueError if e is not an integer.
        '''
        bucket = self.hashValue(e) # self.hashValue(e) will throw ValueError if not int; don't need to double check.
        return e in self.hashSet[bucket]

    def insert(self, e):
        '''
        e: an integer
        Inserts e into the appropriate hash bucket. Raises ValueError if e is not an integer.
        '''
        if not self.member(e): # self.member(e) will throw ValueError if not int; don't need to double check.
            bucket = se`lf.hashValue(e)
            self.hashSet[bucket].append(e)

    def remove(self, e):
        '''
        e: is an integer 
        Removes e from self
        Raises ValueError if e is not in self or if e is not an integer.
        '''
        try:
            bucket = self.hashValue(e) # self.hashValue(e) will throw ValueError if not int; don't need to double check.
            self.hashSet[bucket].remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def getNumBuckets(self):
        '''Getter method for the number of buckets this hashSet has'''
        return self.numBuckets

    def __str__(self):
        """Returns a string representation of self"""
        output = '['
        for b in range(self.getNumBuckets()):
            vals = self.hashSet[b]
            vals.sort()
            output += '{' + ','.join([str(e) for e in vals]) + '},\n'
        return output[:-2] + ']'

        