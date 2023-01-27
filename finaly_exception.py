
try:
    file=open("e:/msg_1.txt","w")
    file.write("hello bye")
    file.write("chanchlesh")
    print("lol")
except:
    print("something went wronge")
finally:
    file.close()




