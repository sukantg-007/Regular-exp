import re
count = 0
matcher = re.finditer("ab","abababab")
for anymatch in matcher:
    count = count +1
    print("Start Index : ",anymatch.start())
    print("End Index : ",anymatch.end())
    print("String : ",anymatch.group())
print("No of counts : ",count)