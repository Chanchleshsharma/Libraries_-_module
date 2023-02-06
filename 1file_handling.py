# file=open("e:/msg_1.txt","r")
# s=file.read()  
#  # s=file.read(3) in read funtion , we can gave index no. of string who's exists on file data

# print(s)
file=open("e:/sas.txt","r")
file.seek(10)   # seek method is used to cursur position
s=file.read()  # (-1) is read all remaining character
               # -1 by default value

#s=file.read(3) in read funtion ,we can gave index no.of string who's exists on file data

print(s)
file.close()

