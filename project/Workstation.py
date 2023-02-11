import queue

class Workstation:

    def __init__(self, component1, component2 = None):
        self.buffer1 = queue.Queue(2)
        self.buffer2 = queue.Queue(2)
        self.componentA = component1
        self.componentB = component2

    def receiveComponent1(self, component):
        if(self.componentA != component):
            print("Workstation cannot accept this component in the first buffer")
            return
        if(self.buffer1.full()):
            print("queue is full")
            return False
        
        self.buffer1.put(component)
        print("component added")
        return True

    def receiveComponent2(self, component):
        if(self.componentB == None):
            print("Workstation only has 1 component type")
            return
        if(self.componentB != component):
            print("Workstation cannot accept this component in the second buffer")
            return
        if(self.buffer2.full()):
            print("queue is full")
            return False
        
        self.buffer2.put(component)
        print("component added")
        return True
    
    def createProduct(self):
        if(self.componentB != None and not self.buffer1.empty() and not self.buffer2.empty()):
            # Add processing time here
            # Increment number of products added here
            self.buffer1.get()
            self.buffer2.get()
            print("Product created")
        elif(self.componentB == None and not self.buffer1.empty()):
            # Add processing time here
            # Increment number of products added here
            self.buffer1.get()
            print("Product created")
        else:
            print("Insufficient components to create product")

    def printBuffer(self):
        print(list(self.buffer1.queue))
        print(list(self.buffer2.queue))

