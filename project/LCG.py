class LCG:
    
    def __init__(self, a, c, m):
        self.a = a
        self.c = c
        self.m = m

    def generateLCG(self, xo, numberOfValues):
        listOfRandomValues = list()
        listOfRandomValues[0] = xo
        for i in range(numberOfValues):
            listOfRandomValues[i+1] = (self.a*listOfRandomValues[0])%self.m

        return listOfRandomValues
    
    def getA(self):
        return self.a
    
    def getC(self):
        return self.c
    
    def getM(self):
        return self.m
