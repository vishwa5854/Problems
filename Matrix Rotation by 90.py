T = int(input())
for z in range(T):
    print("Test Case #" + str(z+1) + ":")
    dim = int(input())
    matrix = []
    for i in range(dim):
        matrix.append(input().split())
    res = []
    for i in range(dim):
        temp = []
        for j in range(dim):
            temp.append(0)
        res.append(temp)

    for i in range(dim):
        for j in range(dim):
            res[j][i] = matrix[dim - i - 1][j]
    for i in res:
        for j in i:
            print(j, end=" ")
        print()
