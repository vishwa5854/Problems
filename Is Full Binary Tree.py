class Node:
    left = None
    right = None

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


def check(root):
    if root is None:
        return True

    if root.right:
        if not root.left:
            return False

    if not root.right:
        if root.left:
            return False

    if not root.right:
        if not root.left:
            return True

    if root.right:
        if root.left:
            return check(root.left) and check(root.right)


if __name__ == '__main__':
    T = int(input())
    for z in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        t = Tree(arr[0])
        for i in range(1, N):
            rt = t.insert(t.root, arr[i])
        print(check(rt))

