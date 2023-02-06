class human:
    def eating (self):
        print("this is eating")

    def sleeping (self):
        print ("this is for sleeping")

    
class student(human):
    def study(self):
        print ("this is study")

    def assignment(self):
        print("this is assignment")

class actor(human):
    def acting(self):
        print("this is for Acting ")

    def shooting (self):
        print("this is shoot")

class player (human):
    def play (self):
        print("this is player")

obj=player()
obj.play()
obj.eating()
obj.sleeping()
oc=actor()
oc.acting()
oc.shooting()
oc.eating()
oc.sleeping()
