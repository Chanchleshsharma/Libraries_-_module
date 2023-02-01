
mob=input("enter mob:")
import re
match=re.fullmatch('[6-9]\d{9}',mob)
if(match==None):
    print("no.is invalid")
else:
    print("valid")