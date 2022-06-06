#one prision class


class Prision:
    def __init__(self, name, inmates):
        self.name = name
        self.inmates = inmates 
        self.tracts = ['high security', 'low security']
        self.locations = ['cantine', 'yard', 'corrections', 'infirmary', 'visitor hall', 'cells']

   

    def lunch():
        print("It is lunchtime! All inmates are requested to appear in the cantine.")
        #how to alter attribute "location" of all objects of different class?
    
    def prisionfight(prisioner1, prisioner2):
        print("Tonight the wardens are turning a blind eye! For the occasion, {name1} and {name2} have assembled in the yard.".format(name1=prisioner1.name, name2=prisioner2.name))
        if(prisioner1.danger > prisioner2.danger):
            print("Yikes, {name2}, that hurt to watch! You should probably refrain from any trouble in the next few weeks... assuming you will get out of the infirmary.".format(name2=prisioner2.name))
            prisioner1.inventory.append("cigarettes")
        elif(prisioner1.danger < prisioner2.danger):
            print("Yikes, {name1}, that hurt to watch! You should probably refrain from any trouble in the next few weeks... assuming you will get out of the infirmary.".format(name1=prisioner1.name))
            prisioner2.inventory.append("cigarettes")
        else:
            print("Lucky fighters! They seem to match each other in every step of the way and today both can go back to their cells unscathed. What a shame...")
            prisioner1.inventory.append("cigarettes")
            prisioner2.inventory.append("cigarettes")
        

    def __repr__(self):
        print("This is the {name} facility. We host {inmates} inmates over {cells} cells.".format(name=self.name, inmates=self.inmates, cells=self.cells))

#3 methods

#one Prisioner class
class Prisioner:
    def __init__(self, name, age, gender, crime, prision, sentence, friendly=True):
        self.name = name
        self.age = age 
        self.gender = gender 
        self.crime = crime
        self.location = ""
        self.prision = prision
        self.tract = ""
        self.number = prision.inmates +1
        self.danger = 0
        self.sentence = sentence
        self.inventory = []
        self.friendliness = friendly
        self.friends = []


   

    def imprisioned(self):
        if(self.crime == "murder" or self.crime == "manslaughter" or self.crime == "aggravated assault"):
            self.tract = "high security"
            self.danger = 1
        else:
            self.tract = "low security"
        print("Inmate number {number}. Proceed to the {tract} tract and wait in your cell until furhter notice.".format(number=self.number, tract=self.tract))
        self.location = "cells"
    
    def make_friends(self, prisioner2):
        if( prisioner2.friendliness==True ):
            print("{name1} approached {name2} and whilst chatting they became good friends.".format(name1=self.name, name2=prisioner2.name))
            self.friends.append(prisioner2.name)
            prisioner2.friends.append(self.name)
        else:
            print("{name1} approached {name2}, who did not appreciate the sentiment and instead used the chance to reinforce their reputation, beating inmate number {number} to a pulp. Better be careful who you trust.".format(name1=self.name, name2=prisioner2.name, number=self.number))
            self.location = 'infirmary'

    def trade(self, prisioner2, item):
        if(self.friends.includes(prisioner2.name)):
            print("Whilst sitting together, {name1} and {name2} exchanged small packages without anyone noticing.".format(name1=self.name, name2=prisioner2.name))
            offer = self.inventory.pop(item)
            payment = prisioner2.inventory.pop(-1)
            print("What a bargain! {name1} exchanged a {offer} in return for an {payment}".format(name1=self.name, offer=offer, payment=payment))


    def __repr__(self):
        print("This is inmate number {number}. {name} is {age} years old and ".format(number=self.number, name = self.name, age = self.age))
        print("for committing {crime} they will spend {sentence} years in the {prision} facility.".format(crime=self.crime, sentence=self.sentence, prision = self.prision))
            


    

#3 methods
   # def imprisioned(gender):

