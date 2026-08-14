string = input()
count=0
count_max=0
for i in range(len(string)-1):
    if (string[i]==string[i+1]):
        count+=1
        if (count>=count_max):
            count_max = count
    else:
        count = 0
print(count_max+1)
