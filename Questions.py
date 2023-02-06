# 1.write a program to concatenate two list ,ListA=[1,2,3,4] listB=[5,6,7,8]?
listA=[1,2,3,4]
listB=[5,6,7,8]
print(listA+listB)
## OUTPUT : [1, 2, 3, 4, 5, 6, 7, 8]

#2.Write a programa to slice on this listc=[1,"krishna",10.0,0j,(4+2j)]
listc=[1,"krishna",10.0,0j,(4+2j)]
print(listc[2:4])
## OUTPUT :[10.0, 0j]

#3. write a program to convert a string str1=("A-Z") using method of string into small laters?
str1=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(str1.lower())
print(str1.swapcase())
## OUTPUT :abcdefghijklmnopqrstuvwxyz


#4. Write a program to convert a string  a= "NnKrishna714@gmail.com" into lower case without using lower() method?
a= "NnKrishna714@gmail.com"
print(a.casefold())
## OUTPUT :nnkrishna714@gmail.com


# 5. Write a program to remove spaces given in a string   a= "        NnKrishna714@gmail.com        "   ?
a= "        NnKrishna714@gmail.com       "
print(a.strip())
## OUTPUT :NnKrishna714@gmail.com

#6. Write three program to get this result="Krishnakumar"  from given string d="krishna" e="kumar" ?
d="krishna" 
e="kumar" 
print(d+e)
print(d,e,sep="")
print("".join([d,e]))
## 6 : OUTPUT :krishnakumar


# # 7. Write a program to get result="krishnakumar",from given string stra="        NnKrishnakumar"  strb="krishna" , strc="    kumar" ?
stra="        NnKrishnakumar" 
strb="krishna"  
strc="    kumar"
# rs=strc.removeprefix("    ")
# print(strb+rs)
result=(strc.strip())
print(strb+result)

## 7 : OUTPUT :krishnakumar