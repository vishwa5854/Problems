class Node:
    left = None
    right = None
    level = ""

    def __init__(self, data):
        self.data = data


class Tree:

    def __init__(self, data):
        self.root = Node(data)

    def insert(self, root, data):

        if root is None:
            return Node(data)

        elif data <= root.data:
            root.left = self.insert(root.left, data)

        else:
            root.right = self.insert(root.right, data)

        return root


def insertLevel(root, v):
    if root is None:
        return

    root.level = v

    insertLevel(root.left, v - 1)
    insertLevel(root.right, v + 1)

    return root


def traverse(root, A):
    if root is None:
        return

    try:
        x = A[root.level]
        x.append(root.data)
        A[root.level] = x
    except KeyError:
        A[root.level] = [root.data]

    traverse(root.left, A)
    traverse(root.right, A)

    return A


if __name__ == '__main__':
    T = int(input())
    for z in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        t = Tree(arr[0])
        for i in range(1, N):
            rt = t.insert(t.root, arr[i])
        rt = insertLevel(rt, 0)
        a = traverse(rt, {})
        for i in sorted(a.keys()):
            for j in sorted(a[i]):
                print(j, end=" ")
            print()
        print()
