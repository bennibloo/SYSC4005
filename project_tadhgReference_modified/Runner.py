from Component import *
from Inspector import *
# from Product import *
# from Workstation import *
import queue

class Runner: 
    fel = queue.PriorityQueue()
    c1 = Component.TYPE_1
    c2 = Component.TYPE_2
    c3 = Component.TYPE_3
    i1 = Inspector(1)
    i2 = Inspector(2)
    w1 = Workstation(c1)
    w2 = Workstation(c1, c2)
    w3 = Workstation(c1, c3)

    entities = [i1, i2, w1, w2, w3]

    def sendMaybeAct():
        for e in entities:
            e.maybeAct()
    
    while(True):
        fel.get()

