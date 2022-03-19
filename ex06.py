import re
s = "ravi"
m = re.match(s,"ravikiran ravi")
if m!= None:
    print(m.start())
    print(m.end())
