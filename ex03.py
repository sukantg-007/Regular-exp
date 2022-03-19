import re
count = 0
#character classes
#x=[abc] [a-z] [^a-z] [^a-zA-z0-9]
matcher = re.finditer("[^a-zA-z0-9]",input("Enter a mail: "))
for anymatch in matcher:
    count = count +1
    print("Start Index : ",anymatch.start())
    print("End Index : ",anymatch.end())
    print("String : ",anymatch.group())
print("No of counts : ",count)