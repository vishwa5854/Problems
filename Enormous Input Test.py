T, k = list(map(int, input().split()))
count = 0
for i in range(T):
    if int(input()) % k == 0:
        count += 1
print(count)
