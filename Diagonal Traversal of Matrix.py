def rotate(matrix):
    res = []
    for i in range(dim):
        temp = []
        for j in range(dim):
            temp.append(0)
        res.append(temp)
    for i in range(dim):
        for j in range(dim):
            res[j][i] = matrix[dim - i - 1][j]
    return res


T = int(input())
for z in range(T):
    dim = int(input())
    matrix = []
    for i in range(dim):
        matrix.append(list(map(int, input().split())))
    Sum = []
    s = 0


    for x in range(1, dim + 1):
        i = 0
        j = x
        tap = True
        while i < dim and j < dim:
            tap = False
            s += matrix[i][j]
            i += 1
            j += 1
        if not tap:
            Sum.append(s)
            s = 0

    Sum = Sum[::-1]

    for i in range(dim):
        s += matrix[i][i]
    Sum.append(s)
    s = 0

    matrix = rotate(rotate(matrix))

    for x in range(1, dim + 1):
        i = 0
        j = x
        tap = True
        while i < dim and j < dim:
            tap = False
            s += matrix[i][j]
            i += 1
            j += 1
        if not tap:
            Sum.append(s)
            s = 0

    for i in Sum:
        print(i, end=" ")
