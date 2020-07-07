n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
if max(max(x[1:]), max(y[1:])) > n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
