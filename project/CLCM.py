import LCG
import random

class CLCM:
    def generateCLCM(LCG1:LCG, LCG2: LCG, numberOfValues: int, *args):
        #Find number of LCGs used
        numberOfLCG = 2 + len(args)

        #Create List of LCGs being used for the CLCM
        LCGList = [LCG1, LCG2]

        for x in range(len(args)):
            LCGList.append(args[x])
        
        #Generate list of y values. Start with generating a Y0 for each LCG (Chooses between 1-M)
        YList = [[0 for y in range(numberOfValues+1)] for z in range(numberOfLCG)]
        for k in range(numberOfLCG):
            YList[k][0] = random.randint(1, LCGList[k].getM())
        
        #Generate the rest of the y values for each LCG
        for i in range(numberOfLCG):
            for j in range(numberOfValues):
                YList[i][j+1] = (LCGList[i].getA() * YList[i][j])%(LCGList[i].getM())

        #Generate x values. Subtract from the y values only if the index is an even number
        XList = [0 for l in range(numberOfValues+1)]
        for m in range(len(XList)):
            for n in range(numberOfLCG):
                if m%2==0:
                    XList[m] = XList[m] + YList[n][m]
                else:
                    XList[m] = XList[m] - YList[n][m]

        #Generate final random value list, based on piecewise function criteria
        RList = [0 for o in range(numberOfValues+1)]
        for p in range(len(RList)):
            if XList[p] > 0:
                RList[p] = XList[p]/LCGList[0].getM()
            elif XList[p] < 0:
                RList[p] = (XList[p]/LCGList[0].getM())+1
            elif XList[p] == 0:
                RList[p] = (LCGList[0].getM()-1)/LCGList[0].getM()
            else:
                print("Problem with Random List")

        return RList

