# T = int(input())
# for z in range(T):
#     waste = input()
#     arr = list(map(int, input().split()))
#     uniq = []
#     ans = []
#     for i in arr:
#         if i not in uniq:
#             uniq.append(i)
#         else:
#             ans.append(i)
#     ans = sorted(ans)
#     for i in ans:
#         print(i, end=" ")
#     print()


T = int(input())
for z in range(T):
    N = int(input())
    ans = []
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    for i in range(N):
        if i + 1 <= N - 1:
            if arr[i + 1] - arr[i] == 0:
                ans.append(arr[i + 1])
    ans = sorted(ans)
    for i in ans:
        print(i, end=" ")
    print()
