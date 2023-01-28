import re
file=open("e:/stud.txt")

s=file.read()
file.close()
# print(s)
match=re.findall("[6-9]\d{9}",s)
print(match)
file=open("e:/sas.txt","w")
for mob in match:
    file.write(mob)
file.close