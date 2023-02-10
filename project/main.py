from Component import *
from Inspector import *
from Product import *
from Workstation import *

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
    w1.printBuffer()
    

if __name__ == "__main__":
    main()
