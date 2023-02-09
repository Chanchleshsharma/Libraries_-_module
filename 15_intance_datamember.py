# class account:
#     def __init__(self):   #instance data member
#         self.bal=10000

# obj=account()
# print(obj.bal)


class account:
    def __init__(self):
        self.bal=20000
        self.acn=201


a1=account()
print(a1.bal)
print(a1.acn)


class bank:
    def __init__(self,a,b):
        self.sal=a
        self.id=b

b2=bank(30000,301)
b3=bank(35000,302)
print(b2.sal,b2.id)
print(b3.sal,b3.id)


# Type of methods:-->
# instance Method
# Class Method
# Static Method


# Constructor----> representedd by @ symbol
#MOdify   funtion/method  meaning


# class test :
#     def N1(self):
#         print("this is N1")
     

    
#     def N2(cls) :
#         print("This is N2")

#     # @ static method
    # def N3(self):
    #     print("this is N3")


# obj=test()
# test.N1()
# test.N2()
# Obj=test()
# Obj.N1()
# Obj.N2()
# Obj.N3()



