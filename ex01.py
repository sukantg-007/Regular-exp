from ast import pattern
from itertools import count
import re
count = 0
pattern = re.compile("a")
matcher = pattern.finditer("abababab")
for anymatch in matcher:
    count = count +1
    print("Start Index : ",anymatch.start())
    print("End Index : ",anymatch.end())
    print("String : ",anymatch.group())
print("No of counts : ",count)