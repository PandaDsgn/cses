import sys

n = int(input())
total_sum = (n * (n + 1)) // 2

if total_sum % 2 != 0:
    print("NO")
    sys.exit()

print("YES")
set1 = []
set2 = []

if n % 4 == 0:
    for i in range(1, (n // 2) + 1):
        if i % 2 == 1:
            set1.extend([i, n - i + 1])
        else:
            set2.extend([i, n - i + 1])

elif n % 4 == 3:
    set1.extend([1, 2])
    set2.append(3)

    for i in range(1, ((n - 3) // 2) + 1):
        left = 3 + i
        right = n - i + 1
        if i % 2 == 1:
            set1.extend([left, right])
        else:
            set2.extend([left, right])

print(len(set1))
print(*set1)
print(len(set2))
print(*set2)
