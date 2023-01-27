#Exception Handling  is a process ? technique to avoid abnormal program termination.

#  print("Hey developer")
# x=[1,2,3,4,5,8,9]
# try:                     # here we will write multiple except with one try:
#     index=int(input('Enter Your Index no.:'))
#     print(x[index])
# except (IndexError , ValueError):
#     print("invalid index")
#     pass
# print("bye")


print("Hey developer")
x=[1,2,3,4,5,8,9]
try:                     # here we will write multiple except with one try:
    index=int(input('Enter Your Index no.:'))
    print(x[index])
except :                           #Except- by default all Error handle by one except
    print("invalid index")
    pass
print("bye")


