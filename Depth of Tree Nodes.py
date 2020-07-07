class Node:
    left = None
    right = None
    depth = -1

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

    def depth(self, root, d):
        if root is None:
            return
        # print(root.data, d)
        root.depth = d
        self.depth(root.left, d + 1)
        self.depth(root.right, d + 1)

        return root

    def search(self, root, data):
        if root is None:
            return -1

        if data > root.data:
            return self.search(root.right, data)
        elif data < root.data:
            return self.search(root.left, data)
        else:
            return root.depth


if __name__ == '__main__':
    T = int(input())
    for z in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        t = Tree(arr[0])
        for i in range(1, N):
            rt = t.insert(t.root, arr[i])
        rt = t.depth(rt, 0)
        for i in arr:
            temp = rt
            print(t.search(temp, i), end=" ")
        print()
