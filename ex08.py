import re
list = ['ravi', 'ravikiran']
s = 'ravi'
for i in list:
    m = re.fullmatch(s,i)
    print(m)
    if m!= None:
        print("string found")
    else :
        print("string not found")
