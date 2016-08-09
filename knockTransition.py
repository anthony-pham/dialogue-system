#Anthony Pham and Julia Issac
#Dialogue System - Knock Knock Joke
#Transition Class

class Transition:

        
    def __init__(self, toState, test_function):

        self.to = toState
        self.test = test_function

    def runTransition(self):

        return self.to
