#Greeting Program for LINDSEE
#cafebot Research: Dialog Systems
#Julia and Anthony 

import time
from continuous_google_speech import listen_for_speech
from maryclient_http import runMary
from Weather_Program import reportingWeather

def greeting():
    greetingMessage = 'Hello, my name is LINDSEE.'
    runMary(greetingMessage)
    print greetingMessage
    time.sleep(1)
    InformationOptions()

def InformationOptions():
    beginningMessage = 'I can tell you information about myself or the weather. What would you like to learn about? Please say you or weather.'
    runMary(beginningMessage)
    print beginningMessage
    time.sleep(6)
    choice = listen_for_speech()
    while choice == None:
        misunderstandMessage = 'Sorry, I did not hear that, can you please repeat what you would like to learn about.'
        runMary(misunderstandMessage)
        print misunderstandMessage
        time.sleep(3)
        choice = listen_for_speech()
    if choice == 'weather':
        reportingWeather('short')
    else:
        lindseeInfo()

def lindseeInfo():
    infoMessage = 'LINDSEE stands for Learning Interactive Navigator and Developmental Social Engagement Engine, which means that I am a social robot.'
    runMary(infoMessage)
    print infoMessage


greeting()       
    
