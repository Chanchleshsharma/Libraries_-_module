# multilevel inheritance 
class telephone:
    def call(self):
        print("this is for call")
class mobile (telephone):
    def msg (self):
        print("this is for Msg")
    

class smartphone (mobile):
    def download(self):
        print("this is for Download")

obj=smartphone()
obj.call()
obj.msg()
obj.download()