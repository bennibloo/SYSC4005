class Inspector:

    def __init__(self, inspectorType):
        self.inspectorType = inspectorType

    def inspectComponent(self, component):
        # Expect that each inspector type will only 
        # call this method on the appropriate 
        # component type
        if(self.inspectorType == 1): 
            if(component.value == 1):
                print("Inspecting Component1")
                # Check time from servinsp1
        elif(self.inspectorType == 2): 
            if(component.value == 2):
                print("Inspecting Component2")
                # Check time from servinsp22
            elif(component.value == 3):
                print("Inspecting Component3")
                # Check time from servinsp23
        # Maybe return the time from the file in this method
