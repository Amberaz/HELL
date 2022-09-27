#法一：循环迭代，逐步逼近
def sqrt_1():
    c=2
    i=0  #记录迭代多少次
    g=0  #记录最终求得的近似值
    for j in range(0,c+1):
        if (j*j>c and g==0):  #
            g=j-1
    while(abs(g*g-c)>0.0001):
        g+=0.00001
        i=i+1
        print(" %d:g = %.5f "%(i,g))
sqrt_1()

#法二：二分查找，折半返回
def sqrt_2():
    i=0
    c=2
    max=c
    min=0
    g=(max+min)/2
    while(abs(g*g-c)>0.0000000000001):
        if (g*g<c):
            min=g
        else:
            max=g
        g=(min+max)/2
        i=i+1
        print(" %d:g=%.12f "%(i,g))
sqrt_2()

#法三：曲线切线，线性逼近，牛顿迭代
def sqrt_3():
    c=2
    i=0
    g=c/2
    while(abs(g*g-c)>0.000000000000001):
        g=(g+c/g)/2
        i=i+1
        print(" %d:g=%.14f "%(i,g))
sqrt_3()
    