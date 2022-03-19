import re
s = "ab"
m = re.search(s,"cababaab ")
if m!= None:
    print(m.start())
    print(m.end())