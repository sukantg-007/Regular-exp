import imp


import re
l1 = ['cat','dog','god','act','tac']
list2 = []
list3 = []
for i in l1:
    count=0
    matcher=re.finditer(f'[{l1[0]}]',i)
    for j in matcher:
        count=count+1
    list2.append(i) if count>0 else list3.append(i)
print(list2)
print(list3)

