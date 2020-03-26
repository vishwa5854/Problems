T = int(input())
for z in range(T):
    dim = int(input())
    matrix = []
    for i in range(dim):
        matrix.append(input().split())
    i = 0
    j = 0
    while True:
        if j == dim - 1:
            print(matrix[i][j], end=" ")
            i += 1
        if i == dim - 1:
            print(matrix[i][j], end=" ")
            j += 1
        else:
            print(matrix[i][j], end=" ")
            j += 1
