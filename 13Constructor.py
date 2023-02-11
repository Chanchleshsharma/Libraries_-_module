# Constructor :--> It is a special method of class 
#__init__():
#it is executed after object creation
class account:
    def __init__(self):
        print("this is Constructor")
    def new(self):
        print("This is new:")
        
a=account()
b=account()
a.new()