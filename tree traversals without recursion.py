class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return TreeNode(data)

    elif data <= root.data:
        root.left = insert(root.left, data)

    else:
        root.right = insert(root.right, data)

    return root


def inOrder(root):
    stack = []

    while True:
        if root is not None:
            stack.append(root)
            root = root.left
        elif len(stack) == 0:
            break
        else:
            root = stack.pop()
            print(root.data)
            root = root.right


def postOrder(root):
    stack = [root]
    ans = []
    while len(stack) != 0:
        x = stack.pop()
        if x is not None:
            ans.append(x)
            stack.append(root.left)
            stack.append(root.right)
    return stack[::-1]


if __name__ == '__main__':
    T = int(input())
    for z in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        t = TreeNode(arr[0])
        for i in range(1, N):
            rt = insert(t.root, arr[i])

        temp = t.root
        a = postOrder(temp, N)
        for i in a:
            print(i.data, end=" ")