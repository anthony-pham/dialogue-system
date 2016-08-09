#Julia Isaac, Anthony Pham and Tristan Johnson
#Dialogue System - Knock Knock Joke
#Runs the two knock knock Jokes

from Jokes import *
from ConsoleRobot import ConsoleRobot
from LindseeRobot import LindseeRobot

def oneJoke():
    banana = bananaJoke().getFSM()

    robot = ConsoleRobot()
    #robot = LindseeRobot()

    keepGoing = True
    
    while keepGoing:
        banana.doAction(robot)
        userInput = robot.getUserInput(banana)
        nextTransition = banana.update(userInput)
        if nextTransition != None or banana.isDone():
            keepGoing = False

def main():
    banana = bananaJoke().getFSM()
    r2d2 = R2D2Joke().getFSM()
    
    robot = ConsoleRobot()
    #robot = LindseeRobot()
    
    FSMStack = []
    currentFSM = banana
    FSMStack.append(currentFSM)
    keepGoing = True

    while keepGoing:
        currentFSM.doAction(robot)
        userInput = robot.getUserInput(currentFSM)
        newFSM = currentFSM.update(userInput)
        if newFSM != None:
            if newFSM == "banana":
                newFSM = banana
                newFSM.setCurrent(1)
            elif newFSM == "R2D2":
                newFSM = r2d2
                newFSM.setCurrent(1)
            #push NewFSM on stack
            FSMStack.append(newFSM)
            keepGoing = popCheck(currentFSM, FSMStack)
            currentFSM = newFSM
        else:
            keepGoing = popCheck(currentFSM, FSMStack)

def popCheck(currentFSM, FSMStack):
    keepGoing = True
    if currentFSM.isDone():
        FSMStack.pop()
        if len(FSMStack) == 0:
            keepGoing = False
    return keepGoing
    
    
        





            
##    while keepGoing:
##        transition = banana.runJoke()
##        if transition == "R2D2":
##            r2d2.fsm.setCurrent(1)
##            transition = r2d2.runJoke()
##            if transition == "banana":
##                banana.fsm.setCurrent(1)
##            else:
##                keepGoing = False
##        else:
##            keepGoing = False
        
main()
#oneJoke()
