#Weather Program
#cafebot Research: Learning about Dialog Systems
#Julia, Anthony, and Tristan

import pywapi
import time
from maryclient_http import runMary
from continuous_google_speech import listen_for_speech

def getZip():
    '''Prompts user for zip code'''
    opener = 'Tell me your zip code for the weather in your area.'
    runMary(opener)
    print opener + '\n'
    time.sleep(5)
    zipcode = listen_for_speech()
    keepAsking = True
    while keepAsking:
        if not validZip(zipcode):
            invalidMessage = 'The zip code given is not a valid zip code. Please enter a new zip code.'
            runMary(invalidMessage)
            print invalidMessage + '\n'
            time.sleep(6)
            zipcode = listen_for_speech()
        else:
            checkMessage = 'You said ' + zipcode + '. Is this the correct zip code? (Please answer with a "yes" or "no")'
            runMary(checkMessage)
            print checkMessage + '\n'
            time.sleep(7)
            answer = listen_for_speech()
            if answer == 'no':
                inputMessage = 'Please enter a new zip code.'
                runMary(inputMessage)
                print inputMessage + '\n'
                time.sleep(2)
                zipcode = listen_for_speech()
            else:
                keepAsking = False
    return zipcode 

def findWeather(zipcode):
    '''Gets weather using pywapi'''
    weather =  pywapi.get_weather_from_weather_com(str(zipcode), units = 'imperial')
    return weather

def reportingWeather(version):
    '''Main method to inform a person of the weather through a dialogue system'''
    zipcode = getZip()
    weather = findWeather(zipcode)
    if weather.has_key('error'):
        errorMessage = 'Error, no station available.'
        runMary(errorMessage)
        print errorMessage
        time.sleep(1)
        startOverMessage = 'If you would like to start the program over say "start", otherwise say nothing' 
        runMary(startOverMessage)
        print startOverMessage + '\n'
        time.sleep(2)
        startOver = listen_for_speech()
        if startOver == "start":
            reportingWeather()
    else:
        if version == 'short':
            shortDiscussWeather(weather['current_conditions'])
        else:
            answer = fullDiscussWeather(weather['current_conditions'])
            if answer != None:
                print answer
                runMary(answer)

def fancyFormat(weatherDict):
    '''Outputs condensed weather information from pywapi'''
    weatherString = ''
    for pair in weatherDict.items():
        key,val = pair[0],pair[1]
        if type(val)==dict:
            weatherString += key+':\n'+fancyFormat(val) + '\n'
        else:
            weatherString += key+':\n'+ str(val) + '\n'
    return weatherString

def validZip(zipcode):
    '''Determines if zipcode can be used in pywapi'''
    return (not zipcode is None) and len(zipcode) == 5 and zipcode.isdigit() and int(zipcode) >= 10

def shortDiscussWeather(weather):
    weatherMesssge = 'It is ' + weather['text'] + ' and ' + weather['temperature'] + 'F now in ' + weather['station'] + '.'
    runMary(weatherMesssge)
    print weatherMesssge

def fullDiscussWeather(weather, message = 'weather'):
    '''Allows a user to ask questions about the weather'''
    choiceMessage = 'Do you want a full description of the '+message+', or be able to investigate on your own? (say yes for full version and no for investigate)'
    runMary(choiceMessage)
    print  choiceMessage + '\n'
    time.sleep(7)
    choice = listen_for_speech()
    while not (choice=='yes' or choice=='no'):
        tryAgain = 'Try again (yes/no)'
        runMary(tryAgain)
        print tryAgain + '\n'
        time.sleep(2)
        choice = listen_for_speech()
        
    if choice == 'yes':
        return fancyFormat(weather)
    else:
        response = ''
        options = ''
        while response == None or response.lower() != 'goodbye':
            responseMessage= options + 'What would you like to know about? (say "options" for your choices or "goodbye" to exit)'
            runMary(responseMessage)
            print responseMessage + '\n'
            time.sleep(8)
            response = listen_for_speech()
            options = ''
            if response != None:
                if response.lower() == 'goodbye':
                    pass
                elif response.lower() == 'options':
                    options = concatDict(weather)
                else:
                    if (' ' in response):
                        response = twoWordOption(response)
                    if weather.has_key(response):
                        answer = weather[response]
                        if type(answer)==dict:
                           return discussWeather(answer, response)
                        else:
                            return answer
                    else:
                        misunderstandMessage = "Sorry, I didn't understand that."
                        runMary(misunderstandMessage)
                        time.sleep(2)
                        print misunderstandMessage

def concatDict(weather):
    keys = ''
    for key in weather.keys():
        keys += key + '\n'
    return keys

def twoWordOption(option):
    wordList = option.split(' ')
    return wordList[0] + '_' + wordList[1]

    
    

#reportingWeather('short')


