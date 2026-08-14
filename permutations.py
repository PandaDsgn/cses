n = int(input())
y=[]
x=set()
if (n==1):
    print("1")
elif (n<=3 and n!=1):
    print("NO SOLUTION")
else:
    for i in range(1,n+1):
        if (i%2==0):
            y.append(i)
        else:
            x.add(i)
y.extend(x)
print(*y)
