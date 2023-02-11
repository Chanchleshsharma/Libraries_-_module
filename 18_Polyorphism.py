###polymorphism

##poly-----> many
#morphism----> forms
#
#ability an entity to show mltiple behaviours of one direction

# In python there are implementation of Polymorphism  
# method Overiding
# method Overloading


class Over1:
    def M1(self):
        print("this is M1")



    def M2(self):
        print("this is me2")


class Over2(Over1):
    def M1(self):
        print("this is m1")


        super().M1 ()


ob=Over2()
ob.M1()
ob.M2()



class poly:
    def Father (self):
        print("this is Father method")

    def Mother(self):
        print("this is Mother method")

class morphism(poly):
    def child(self):
        print("this is Child")
        
    def Father(self):
        print("this is Fatherr")


        super().Father()


object=morphism()
object.child()
object.Mother()
object.Father()