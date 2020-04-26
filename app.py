import time
import sys
from textmagic.rest import TextmagicRestClient

class Main:
    def __init__(self, phoneNumber, timeBetweenTexts, script, username, token):
        # This is the number that the program will send messages to
        self.phoneNumber = phoneNumber
        #This is the ammount of time in between texts sent 
        self.timeBetweenTexts = timeBetweenTexts
        # This is the script or string of text that will be sent word for word to the user
        self.script = script
        # This is your username from textmagic
        self.username = username
        # This is the token that comes with your TextMagic account
        self.token = token
    
    def startTextMagic(self):
        script = self.script
        phone = self.phoneNumber
        sleepTime = self.timeBetweenTexts
        username = self.username
        token = self.token

        # initializes the client to use your user credentials
        client = TextmagicRestClient(username, token)

        with open(script, 'r') as file:
            data = file.read().replace('\n', '')
            for word in data.split():
                message = client.messages.create(
                                                  phones = self.phoneNumber,
                                                  text = word
                                                 )
                time.sleep(self.sleepTime)

    # This function will be for the twilio users
    def startTwilio(self):
        pass
        
