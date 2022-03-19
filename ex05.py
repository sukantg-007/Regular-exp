import re
count = 0
#Qualifier
#x=a, a+, a*, a?, a{3}, a{m,n}
matcher = re.finditer("[A-Z]{3}","AabBBBcdef")
for anymatch in matcher:
    count = count +1
    print("Start Index : ",anymatch.start())
    print("End Index : ",anymatch.end())
    print("String : ",anymatch.group())
print("No of counts : ",count)