n = int(input())
if (n<1 or n>(10**6)):
    print("Error")
print(n, end=' ')
while (n!=1):
    if (n%2==0):
        n=n//2
        print(n, end=' ')
    else:
        n = (n*3)+1
        print(n, end=' ')
