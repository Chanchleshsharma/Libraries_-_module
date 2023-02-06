#Inheritance is a class code reusablity
# # proces of getting  method of a  existing class into a newly created class
# Existing class is known as parent/super/base class
# new created class is known as child class/sub /derived class 
  
# TYPE OF INHERITANCE
# 1.single level 
# 2.multilevel 
# 3.multiple
# 4. hybrid
# 5. hierarchical

#single level inhertance
class telephone:
    def call(self):
        print('this is for call')

class mobile(telephone):

    def msg(self):
        print("this is for msg")

obj=mobile()
obj.msg()
obj.call()



