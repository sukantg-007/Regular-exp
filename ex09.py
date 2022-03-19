import re 
s = 'abc@123w95*'
m =re.findall("[0-9]",s)
print(m)