import re
s = "ravi$"
m = re.search(s,"ravikiran ravi")
if m!= None:
    print(m.start())
    print(m.end())