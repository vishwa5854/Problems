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


def solve(root, ans, s, leaf):
    if leaf:
        ans.append(s)
        return
    elif root is None:
        return

    s += root.data
    if not root.right:
        if not root.left:
            leaf = True

    solve(root.right, ans, s, leaf)
    solve(root.left, ans, s, leaf)

    return ans


def hasPathSum(A, B):
    a = solve(A, [], 0, False)
    print(a)
    if B in a:
        return 1
    return 0


if __name__ == '__main__':
    T = int(input())
    for z in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        K = int(input())
        t = Tree(arr[0])
        for i in range(1, N):
            rt = t.insert(t.root, arr[i])
        print(hasPathSum(rt, K))


