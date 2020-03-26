withdraw, available = map(float, input().split())
if withdraw % 5 == 0:
    if available > withdraw + 0.5:
        print(available - withdraw - 0.5)
else:
    print(available)
