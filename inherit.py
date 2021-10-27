#################################################################################
'''Inheritance example

'''

import person as human

class Enemy(human.Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def introduce(self):
        print("You are my mortal enemy!")

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <=80:
            print("{}, you are tired and weak!".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your junk!".format(other.firstname))
        if other.status == True:
            other.status == False

Joker = Enemy('rock', 'Mr.', 'Joker', 75, status = False)
Joker.introduce()
Joker.hurt(human.Maria)
Joker.insult(human.Joe)
Joker.insult((human.Maria))
Joker.steal(human.Maria)


