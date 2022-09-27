i=1
sum=0
while i<101:
    if i%2==1:
        print(i)
        if i<51:
            sum+=i
    i+=1
print(sum)