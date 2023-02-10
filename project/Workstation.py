import queue

class Workstation:

    def __init__(self, component1, component2 = None):
        self.buffer1 = queue.Queue(2)
        self.buffer2 = queue.Queue(2)
        self.componentA = component1
        self.componentB = component2

    def receiveComponent1(self, component):
        if(self.buffer1.full()):
            print("queue is full")
            return False
        
        self.buffer1.put(component)
        print("component added")
        return True

    def receiveComponent2(self, component):
        if(self.componentB == None):
            return
        if(self.buffer2.full()):
            print("queue is full")
            return False
        
        self.buffer2.put(component)
        print("component added")
        return True

    def printBuffer(self):
        print(list(self.buffer1.queue))
        print(list(self.buffer2.queue))

