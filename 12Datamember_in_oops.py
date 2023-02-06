#1 Instance data member:--> a) represent property of individual Object 
#b) Constructor is used initialize instance data member

# 2) Class data member --> a) Represents property of class and shared to all object 
# b) WE can directly initialize in class indented block 
# 
class account:
    ifsc='abc 123'

print(account.ifsc)
account.ifsc="new 345"
print(account.ifsc)