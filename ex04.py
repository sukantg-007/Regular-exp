import re
count = 0
#predefined character classes
#x=\s, \S, \d, \D, \w, \W, .
matcher = re.finditer(".",input("Enter a str: "))
for anymatch in matcher:
    count = count +1
    print("Start Index : ",anymatch.start())
    print("End Index : ",anymatch.end())
    print("String : ",anymatch.group())
print("No of counts : ",count)