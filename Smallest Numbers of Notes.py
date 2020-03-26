T = int(input())
# 100 50 10 5 2 1
for i in range(T):
    lol = int(input())
    count = 0
    count += int(lol/100)
    lol = lol % 100
    count += int(lol/50)
    lol = lol % 50
    count += int(lol/10)
    lol = lol % 10
    count += int(lol/5)
    lol = lol % 5
    count += int(lol/2)
    lol = lol % 2
    count += int(lol/1)
    lol = lol % 1
    print(count)
