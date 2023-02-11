
#### Nested class 
# class myclass:        ##Outer/toplevel class
#     class yourclass:     ##nested class
#         pass

class A:
    def show (self):
        print("this is show method")
        
    class B:
        def disp(self):
            print("this is disp method")

obj2=A()
obj2.show()    ### here called a parent class

obj=A.B()        ###  here called a nested/inner class 
obj.disp()