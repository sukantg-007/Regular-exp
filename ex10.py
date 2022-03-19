import re 
s = 'abc@123w95*'
m =re.sub("[0-9]",'#',s)
n =re.subn("[0-9]",'#',s)
print(m)
print(n)