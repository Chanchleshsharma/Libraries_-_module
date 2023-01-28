# file=open("e:/msg_1.txt","r")
# s=file.read()  
#  # s=file.read(3) in read funtion , we can gave index no. of string who's exists on file data

# print(s)
file=open("e:/msg_1.txt","r")
file.seek(10)
s=file.read()  
#s=file.read(3) in read funtion ,we can gave index no.of string who's exists on file data

print(s)
file.close()

