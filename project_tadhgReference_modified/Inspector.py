class Inspector {
    inspectionTimeLeft
    currentComp = null

    def getState(){
        if(currentComponent.isReady()){

        } elif (this.currentComp.isReady()) {
            return "blocked"
        } else {
            return "working"
        }
    }

    def tryToMoveComponentToBuffer(comp){

    }

    def getNewComponent(){}

    def addEventToFEL(delay, description){

    }

    def passTime(delay){
        # If currently inspecting state
        if(currentComp != null && currentComp.isReady()){
            # This should be the main space where inspectionTimeLeft is used
            inspectionTimeLeft = inspectionTimeLeft - delay
            if(inspectionTimeLeft == 0){
                currentComp.markAsReady()
            }
        }
    }

    def maybeAct(){
        if(currentComp != None && currentComp.isReady()){
            got_rid = this.tryToMoveComponentToBuffer(currentComp)
            if(got_rid){
                currentComp = null
                # This event happens immediately (no delay)
                addEventToFEL(0.0, "buffer got new component")
            }
        }
        if(currentComp != null){
            # Return because you would be still working
            return 
        }
        currentComp = this.getNewComponent
        inspectionTimeLeft = currentComp.getInspectionTime()
        addEventToFEL(currentComp.getInspectionTie(), "Finished inspecting")

    }
}