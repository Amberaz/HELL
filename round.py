l=[1,2,3,4,5]
# 数据切片[::-1]
# mylist[start:end:step]
# 从start开始到end（不包含第end个元素）,每隔step个取一个元素
# 当start,end,step为负数时，表示从反方向遍历
print(l[::-1])
print('\n')

for i in range(len(l),0,-1):
    print(i,end=' ')  
print('\n')

i=0
while i<len(l):
    print(l[len(l)-i-1],end=' ')
    i+=1
print('\n')