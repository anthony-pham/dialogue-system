#Julia Isaac, Anthony Pham and Tristan Johnson
#Dialogue System - Knock Knock Joke
#FSM

class FSM:

    def __init__(self):

        self.states = {}
        self.current_state = None
        self.oldCurrent = None

    def addState(self, newState, stateName):
        '''add parameter to states'''
        self.states[stateName] = newState

    def setCurrent(self, state):
        self.oldCurrent = self.current_state
        self.current_state = state

    def getOldCurrent(self):
        return self.oldCurrent

    def getCurrent(self):
        return self.current_state

    def update(self, userInput):
        if self.current_state != None:
            transition = self.states[self.current_state].runState(userInput)
            if self.states.has_key(transition):
                self.oldCurrent = self.current_state
                self.current_state = transition
            else:
                self.oldCurrent = self.current_state
                self.current_state = None
                return transition

    def doAction(self, robot):
        if self.current_state != None:
            robot.outputMessage(self.states[self.current_state].stateMessage())

    def isDone(self):
        if self.current_state == None: #self.states[self.current_state].hasTransitions():
            return True
        else:
            return False

##    def transition(self, userInput):
##        nextTransition
##        newTransition = update
##        if newTransition = None:
##            return self
##        else:
##            return newTransition
