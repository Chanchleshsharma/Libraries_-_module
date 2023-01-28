# Regular Expression is manly used in data cleaning
#uses of regex

# pattern based matching 
# datavalidation 
# datacleaning
# regular expressionis a case sensitive
import re
s="Python is simple language invented by Guido VAN Rossum and I study python"
match=re.findall("i.",s)   # here i means that in the avobe string s who word is starting with "i" we will got output as a list
# and . means that recognize any character 
#OUT PUT ['is', 'im', 'in', 'id']
print(match)
match2=re.findall("i[a-z]",s)
match3= re.findall("[a-z][aeiou][a-z]",s)
print(match2)

print(match3)

match4= re.findall("[a-z][^aeiou][a-z]",s)    # here ^ this means except in Regular expration ,which means we negelat this [^aeiou] alphavates on string s
print(match4)