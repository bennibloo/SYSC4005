from Component import *
from Inspector import *
from Product import *
from Workstation import *
import csv
import os

class Simulation:
    
    def scheduleArrival():
        #Create and put arrival event into FEL
        pass

    def processArrival():
        #Check workstation buffer of inspector's associated workstations. If the buffer is full, inspector waits

        #If component needs to be inspected, send to inspector

        #If component has been inspected, send to workstation
        pass

    def processDeparture():
        #If the product is completed, then schedule the next component in the FEL
        #Increment the number of depatures (products made)
        pass

    def simulation():
        #while number of departures (products made) is less than the total number of (components/2)

        #Retrieve imminent event

        #Update clock based on the time scheduled for the event

        #If the event is an arrival
            #Process arrival

            #Schedule arrival

        #Otherwise, the event is a departure
            #Process departure
        pass

def main():
    print("Hello World")
    w1 = Workstation(Component.TYPE_1)
    w2 = Workstation(Component.TYPE_1, Component.TYPE_2)
    w3 = Workstation(Component.TYPE_1, Component.TYPE_3)
    i1 = Inspector(1)
    i2 = Inspector(2)
    c1 = Component.TYPE_1
    c2 = Component.TYPE_2
    c3 = Component.TYPE_3

    # Testing methods
    i1.inspectComponent(c1)
    i2.inspectComponent(c2)
    i2.inspectComponent(c3)

    w2.receiveComponent1(c1)
    w2.receiveComponent2(c2)
    w2.receiveComponent1(c1)
    w2.receiveComponent2(c2)
    w2.receiveComponent1(c1)
    w2.receiveComponent2(c2)
    w2.printBuffer()

    #Converts dat files to CSV files
    #NOTE: the extracted project folder has to be on the same directory level as main.py
    convertFileToCsv("./Project/servinsp1.dat")
    convertFileToCsv("./Project/servinsp22.dat")
    convertFileToCsv("./Project/servinsp23.dat")
    convertFileToCsv("./Project/ws1.dat")
    convertFileToCsv("./Project/ws2.dat")
    convertFileToCsv("./Project/ws3.dat")

    #Parse and return lists of data from CSV files
    servinsp1Data = parseCsvToList("./CSV/servinsp1.csv")
    servinsp22Data = parseCsvToList("./CSV/servinsp22.csv")
    servinsp23Data = parseCsvToList("./CSV/servinsp23.csv")
    ws1Data = parseCsvToList("./CSV/ws1.csv")
    ws2Data = parseCsvToList("./CSV/ws2.csv")
    ws3Data = parseCsvToList("./CSV/ws3.csv")

'''
Converts a dat file into a csv file and creates it in a CSV directory
@param file The dat file
'''
def convertFileToCsv(file):
    #Get the filename to be used to create the corresponding CSV file
    filename = (os.path.basename(file).split("."))[0]

    #open, store and read from dat file
    datFile = [i.strip().split() for i in open(file).readlines()]

    #create csv folder for csv converted dat files
    if not os.path.exists("./CSV"):
        os.makedirs("./CSV")

    with open("./CSV/" + filename + ".csv", "w") as csvDatFile:
        csvWriter = csv.writer(csvDatFile)
        csvWriter.writerows(datFile)
'''
Returns a list of the content in a csv file
@param file The CSV file
@return Returns a list of data
'''
def parseCsvToList(file):
    data = list()

    with open(file) as csvFile:
        csvReader = csv.reader(csvFile)

        for row in csvReader:
            data.append(row)

    return data

if __name__ == "__main__":
    main()
