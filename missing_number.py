n = int(input())
s={0}
y = list(map(int, input().split()))
for i in y:
   s.add(i)
for i in range(n+1):
    if (i not in s):
        print(i)
