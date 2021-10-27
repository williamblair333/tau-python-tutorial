#################################################################################
'''
https://testautomationu.applitools.com/python-tutorial/chapter8.html
https://stackoverflow.com/questions/625083/what-init-and-self-do-in-python
https://www.geeksforgeeks.org/__init__-in-python/

'''
import random

class Person:
    def __init__(self, firstname, lastname, health, status):
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        print("My name is {} {}".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print(" {} is happy".format(self.firstname))
        elif emotion == 2:
            print(" {} is sad".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is in perfect health".format(self.firstname))
        elif self.health > 1:
            print("{} is not dead but not in perfect health".format(self.firstname))
        elif self.health < 1:
            print("{} is dead or dying".format(self.firstname))

Maria = Person("Maria", "Gonzalez", 88, status=True)
Joe = Person("Joe", "Blow", 72, status=False)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Joe.firstname, Joe.status))

Maria.introduce()
Joe.introduce()

Maria.status_change()
Joe.status_change()