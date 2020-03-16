dim = list(map(int, input().split()))
A = []
for i in range(dim[1]):
    A.append(0)
for i in range(dim[0]):
    temp = list(map(int, input().split()))
    for j in range(dim[1]):
        A[j] += temp[j]
for i in A:
    print(i)
