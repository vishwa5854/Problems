T = int(input())
a = 1000000007
dp0 = [1]
dp1 = [1]
for i in range(1, 100000):
    dp0.append(dp0[i - 1] + dp1[i - 1])
    dp1.append(dp0[i - 1])
for z in range(T):
    N = int(input())
    print((dp0[N - 1] + dp1[N - 1]) % a)
