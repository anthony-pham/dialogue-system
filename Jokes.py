#Julia Isaac, Anthony Pham and Tristan Johnson
#Dialogue System - Knock Knock Joke
#Sets up two knock knock jokes

from knockFSM import FSM
from knockTransition import Transition as T
from knockState import DialogueState as S
        
class bananaJoke():
    fsm = FSM()
    name = 'banana'
    
    def __init__(self):
        self.fsm.addState(S("Knock knock"), 1)

        self.fsm.addState(S("Banana"), 2)

        self.fsm.addState(S("Knock knock"), 3)
        
        self.fsm.addState(S("Orange"), 4)

        self.fsm.addState(S("Orange you glad I didn't say banana \nDo you want another joke?"), 5)

        self.fsm.addState(S("You're suppose to say who's there... \nKnock Knock"), 6)

        self.fsm.addState(S("You're suppose to say banana who..."), 7)

        self.fsm.addState(S("You're suppose to say who's there... \nKnock Knock"), 8)

        self.fsm.addState(S("You're suppose to say orange who..."), 9)

        transList = [T(3, matches("stop")),
                     T(2, matches("who")),
                     T(6, matches(""))]
        self.fsm.states[1].addTransitions(transList)

        transList = [T(1, matches("who")),
                     T(3, matches("stop")),
                     T(7, matches(""))]
        self.fsm.states[2].addTransitions(transList)

        transList = [T(4, matches("who")),
                     T(8, matches(""))]
        self.fsm.states[3].addTransitions(transList)

        transList = [T(5, matches("who")),
                     T(9, matches(""))]
        self.fsm.states[4].addTransitions(transList)

        transList = [T("R2D2", matches("yes"))]
        self.fsm.states[5].addTransitions(transList)

        transList = [T(4, matches("stop")),
                     T(2, matches("who")),
                     T(6, matches(""))]
        self.fsm.states[6].addTransitions(transList)

        transList = [T(1, matches("who")),
                     T(3, matches("stop")),
                     T(7, matches(""))]
        self.fsm.states[7].addTransitions(transList)

        transList = [T(4, matches("who")),
                     T(8, matches(""))]
        self.fsm.states[8].addTransitions(transList)

        transList = [T(5, matches("who")),
                     T(9, matches(""))]
        self.fsm.states[9].addTransitions(transList)



        self.fsm.setCurrent(1)

    def getFSM(self):
        return self.fsm
        
    def runJoke(self):
        while self.fsm.current_state != None:
           # print self.name + ":" + str(self.fsm.current_state)
            last = self.fsm.update()
        return last

class R2D2Joke():
    fsm = FSM()
    name = "R2D2"
    
    def __init__(self):
        self.fsm.addState(S("Knock knock"), 1)

        self.fsm.addState(S("art"), 2)

        self.fsm.addState(S("R2-D2 \nDo you want another joke?"), 3)
        
        self.fsm.addState(S("You're suppose to say who's there... \nKnock Knock"), 4)

        self.fsm.addState(S("You're suppose to say art who... \n"), 5)

        transList = [T(2, matches("who")),
                     T(4, matches(""))]
        self.fsm.states[1].addTransitions(transList)

        transList = [T(3, matches("art who")),
                     T(5, matches(""))]
        self.fsm.states[2].addTransitions(transList)
        
        transList = [T("banana", matches("yes"))]
        self.fsm.states[3].addTransitions(transList)

        transList = [T(2, matches("who")),
                     T(4, matches(""))]
        self.fsm.states[4].addTransitions(transList)

        transList = [T(3, matches("art who")),
                     T(5, matches(""))]
        self.fsm.states[5].addTransitions(transList)

        self.fsm.setCurrent(1)

        
    def runJoke(self):
        while self.fsm.current_state != None:
            print self.name + ":" + str(self.fsm.current_state)
            last = self.fsm.update()
        return last

    def getFSM(self):
        return self.fsm

def matches(toMatch):
    return lambda(r) :toMatch in r
