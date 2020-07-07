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

    def inOrder(self, root):
        if root is None:
            return

        self.inOrder(root.left)
        print(root.data, end=" ")
        self.inOrder(root.right)

    def preOrder(self, root):
        if root is None:
            return
        print(root.data, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def postOrder(self, root):
        if root is None:
            return

        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=" ")


def postOrder(root):
    stack = [root]
    ans = []
    while len(stack) != 0:
        x = stack.pop()
        if x is not None:
            ans.append(x)
            stack.append(root.left)
            stack.append(root.right)
    return ans[::-1]


if __name__ == '__main__':
    T = int(input())
    for z in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        t = Tree(arr[0])
        for i in range(1, N):
            rt = t.insert(t.root, arr[i])

        temp = t.root
        a = postOrder(temp)
        for i in a:
            print(i.data, end=" ")
        # t.preOrder(temp)
        # print()
        # temp = t.root
        # t.inOrder(temp)
        # print()
        # temp = t.root
        # t.postOrder(temp)

        print()
        print()
