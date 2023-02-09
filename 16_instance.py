# class calc:
#     def __init__(self):
#         self.x=3
#         self.y=4

#     def mult(self):
#         print(self.x*self.y)

# obj=calc()
# obj.mult()

class calc:
    def __init__(self,a,b):
        self.x=a
        self.y=b

    def mult(self):
        print(self.x*self.y)

obj=calc(2,4)
obj.mult()
# print(obj.x,obj.y)

############    Decorator            ########################3
class test:
    def M1(self):
        print("this is M1")            # instance method

    @ classmethod                       # class method   in this method ,,, class is run without creating an object
    def M2(cls):
        print("this is M2")


    @ staticmethod
    def M3 ():
        print("this is M3")


# obj=test()
# obj.M1()
# obj.M3()
# test.M1()
test.M2()
test.M3()

class calc:
    x=3
    y=4
 
    @classmethod

    def mul(cls):
        print(calc.x*calc.y)


calc.mul()


class new:
     
    @ staticmethod
    def add(a,b):
        print(a+b)

new.add(3,8)