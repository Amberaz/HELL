import random
import math
s=2
n=10000000
c=0
for i in range(n):
    x=random.uniform(0.0,1.0)
    y=random.uniform(0.0,2.0)
    if y<=x**3+x**2:
        c+=1
result=c*s/n
print(result)        