class Inspector:
    
    inspectionTimeLeft
    currentComp = null

    def getState():
        if(currentComponent.isReady()):

        elif (this.currentComp.isReady()) :
            return "blocked"
        else:
            return "working"
        
    

    # Try to move Component to workstation buffer
    def tryToMoveComponentToBuffer(comp):

    # Should create/get new component and set it as the current Component
    def getNewComponent():

    def addEventToFEL(delay, description):
        # Need to have the runner in the constructor for this class
        # such that you're able to add events to the FEL

    def passTime(delay):
        # If currently inspecting state
        if(currentComp != null && currentComp.isReady()):
            # This should be the main space where inspectionTimeLeft is used
            inspectionTimeLeft = inspectionTimeLeft - delay
            if(inspectionTimeLeft == 0):
                currentComp.markAsReady()

    def maybeAct():
        if(currentComp != None && currentComp.isReady()):
            got_rid = this.tryToMoveComponentToBuffer(currentComp)
            if(got_rid):
                currentComp = null
                # This event happens immediately (no delay)
                addEventToFEL(0.0, "buffer got new component")
            
        if(currentComp != null):
            # Return because you would be still working
            return 
        
        currentComp = this.getNewComponent
        inspectionTimeLeft = currentComp.getInspectionTime()
        addEventToFEL(currentComp.getInspectionTie(), "Finished inspecting")
