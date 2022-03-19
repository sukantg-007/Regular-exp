from ntpath import join
import re
k = ['ac','bg','96','35$']
l = (',').join(k)
print(l)
m = re.split(",",l)
print(m)