class Entity {
    # Note: Should only be able to update own state
    #       rather than other components as well
    
    # description is only used for logs
    def addEventToFEL(delay, description){

    }
    # Need way to event runner to give timestamp
    timeOfLastUpdate
    # Could have map to measure 
    timespentInStates = map() 
    def passTime(delay){

    }
    def maybeAct(){}
    def update(absoluteTimestamp){
        delay = absoluteTimestamp - timeOfLastUpdate
        stateSinceLastUpdate = getState()
        timeAlreadySpentInThisState = timespentInStates.get(stateSinceLastUpdate, 0.0)
        timeSpentInStates.set(stateSinceLastUpdate, timeAlreadySpentInThisState + delay)
        timeOfLastUpdate = absoluteTimestamp
        passTime(delay)
        # maybeAct()
    }
    # This is primarily used for logging purposes
    # or tracking time in each state
    def getState(){}

}