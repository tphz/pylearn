a,b=map(int,input().split())
c = a**2+b**2
if c > 100:
    print (c)
    print((c // 100) % 10)
else:
    print(a+b)
    