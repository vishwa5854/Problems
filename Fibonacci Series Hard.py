T = int(input())
fib = [0, 1, 1]
for i in range(3, 10**18):
    fib.append(fib[i - 1] + fib[i - 2])
for z in range(T):
    N = int(input())
    print(fib[N])

