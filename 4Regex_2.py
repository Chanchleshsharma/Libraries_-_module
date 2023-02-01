import re
number=('hey bro i am a Python Guido VAN Developer Fromm Yearr 1998 1993 1999 New')
match=re.findall("[1-2][0-9][0-9][0-9]",number)
print(match)
match2=re.findall("[1-2][0-9]{3}",number) #{}means Repeatation in Regex..I put the value in {}is 3 it means repeat 3 times of justprivious char
print(match2)

match3=re.findall("[A-Z][a-z]{4}",number)
print(match3)

match4=re.findall("[A-Z][a-z]{4,6}",number) # here in {4,6} min 4 or max 6 ... in regex its start from max 
print(match4)
match5=re.findall("[A-Z][a-z]+",number)
print(match5)
match6=re.findall("[A-Z][a-z]*",number)
match7=re.findall("[A-Z][a-z]?",number)
print(match7)
print(match6)

match8=re.findall("\d\d\d\d",number) # it\d means matches number/digit
print(match8)
match9=re.findall("\D",number)  # \D means except digits (lost digits)
print(match9)
m1=re.findall("\s",number)  #\s shows space
print(m1)
m2=re.findall("\S",number) # its a except of \s
m3=re.findall("\w",number) #word character
m4=re.findall("\W",number) #except of word char
print(m2)
print(m3)
print(m4)