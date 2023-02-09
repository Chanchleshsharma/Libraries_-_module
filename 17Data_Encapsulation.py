#data encapsulation/ data hiding 


# without Encapsulation
class emp:
    def __init__(self):
        self.sal=23000


e=emp()
print(e.sal)



#With Encapsulation


class Eng:
    def __init__(self):
        self.__sal=45000   ### here __ double underscore means private data member

    def getsal(self):
        return self.__sal

eg=Eng()
# print(eg.__sal)      # its error

print(eg.getsal)
