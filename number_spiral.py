n = int(input())
answers=[]
for i in range(n):
    y, x = map(int, input().split())
    k=max(x,y)
    if (k%2==0):
        ans = (k**2)-(x-1) if k==y else ((k-1)**2)+y
    else:
        ans = ((k-1)**2)+x if k==y else (k**2)-(y-1)
    answers.append(ans)

for i in range(n):
    print(answers[i])
