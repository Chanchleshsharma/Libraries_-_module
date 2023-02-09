class account:
    ifsc="abc984"            # class data member

    def __init__(self):
        self.sal=10000             #instance data  member

a=account()
b=account()
print(a.sal,b.sal)
print(a.ifsc,b.ifsc)


# dir(set())