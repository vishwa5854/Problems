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


def inOrder(root, ans):
    if root is None:
        return

    inOrder(root.left, ans)
    ans.append(root.data)
    inOrder(root.right, ans)
    return ans


def isBST(root, p):
    # get in order traversal and see of it is sorted
    # iorder = inOrder(root, [])
    # if sorted(rootData) == iorder:
    #     return True
    # return False
    if root is None:
        return True
    if not isBST(root.left, p):
        return False
    if root.data < p:
        return False
    else:
        p = root.data
    if not isBST(root.right, p):
        return False

    return True


def BST(root, temp, left):
    if root is None:
        return True

    if left:
        if root.data <= temp:
            temp = root.data
        else:
            return False
    else:
        if root.data > temp:
            temp = root.data
        else:
            return False
    return BST(root.left, temp, True) and BST(root.right, temp, False)


if __name__ == '__main__':
    T = int(input())
    for z in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        t = Tree(arr[0])
        for i in range(1, N):
            rt = t.insert(t.root, arr[i])
        p = -1000000007
        print(BST(rt, rt.data, True))
