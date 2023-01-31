import queue

class Workstation:
    # buffer1
    # buffer2

    # def __init__(self, component1):
    #     self.buffer1 = queue.Queue(2)

    def __init__(self, component1, component2):
        self.buffer1 = queue.Queue(2)
        self.buffer2 = queue.Queue(2)

    def receiveComponent1(self, component):
        if(self.buffer1.full()):
            print("queue is full")
            return False
        
        self.buffer1.put(component)
        print("component added")
        return True

    def receiveComponent2(self, component):
        if(self.buffer2.full()):
            print("queue is full")
            return False
        
        self.buffer2.put(component)
        print("component added")
        return True

    def printBuffer(self):
        print(list(self.buffer1.queue))
