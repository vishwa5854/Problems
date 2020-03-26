a = int(input())
count = 0
for i in range(1,a):
    if i % 3 == 0 or i % 5 == 0:
        count += 1
print(count)
