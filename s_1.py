s=input()
n=s.lower()
max=1
num=1
result=[]
tmp=[s[0]]
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        num+=1
        if max<num:
           max=num
           tmp=[s[i]]
        elif max==num:
            tmp.append(s[i+1])
    else:
        num=1
for i in tmp:
    print(i*max)
