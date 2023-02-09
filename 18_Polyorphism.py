###polymorphism

##poly-----> many
#morphism----> forms
#
#ability an entity to show mltiple behaviours of one direction

# In python there are implementation of Polymorphism  
# method Overiding
# method Overloading


class Over:
    def M1(self):
        print("this is M1")



        def M2(self):
            print("thisis me")


class Over2(Over):
    def M3(self):
        print("this is m3")


        super().M1 ()


ob=Over2()
ob.M1()
ob.M2()
ob.M3()