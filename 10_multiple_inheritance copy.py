# multiple inheritance means any child class have multiple parent class

class telephone:
    def call(self):
        print("this is for call")
class mobile ():
    def msg (self):
        print("this is for Msg")
    
class camera:
    def pics(self):
        print("this is for pics")

class smartphone (mobile,camera,telephone):
    def download(self):
        print("this is for Download")

obj=smartphone()
obj.call()
obj.msg()
obj.download()
obj.pics()