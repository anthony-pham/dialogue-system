#Anthony Pham and Julia Issac
#Dialogue System - Knock Knock Joke
#The purpose of this class is to construct state objects for our finite state machine.

class DialogueState():

    # Constructor
    def __init__(self, toBeSaid):
        self.toBeSaid = toBeSaid
        self.transitions = []

    def addTransitions(self, transList):
        '''adds the given list of transitions to the current'''
        self.transitions+=transList
        
    def runState(self, userResponse):
        #Get input (google speech ... eventually)
        #userResponse = raw_input(self.toBeSaid + "\n")
        
        #Respond (mary ... eventually)
        for t in self.transitions:
            if t.test(userResponse):
                next = t.runTransition()
                return next

    def hasTransitions(self):
        if len(self.transitions) == 0:
            return False
        else:
            return True

    def stateMessage(self):
        return self.toBeSaid
