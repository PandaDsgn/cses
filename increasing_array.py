n = int(input())
moves=0
m = list(map(int, input().split()))
for i in range(len(m)-1):
    if (m[i]>m[i+1]):
        moves+=(m[i]-m[i+1])
        m[i+1]=m[i]
print(moves)
