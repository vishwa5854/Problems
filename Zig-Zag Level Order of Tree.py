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


def bottomUpLevelOrder(root):
    container = [root, "*"]
    temp = 0
    while temp < len(container):
        if container[temp] == "*":
            if container[temp - 1] == "*":
                container.pop(temp)
                break
            temp += 1
            container.append("*")
        if container[temp].left:
            container.append(container[temp].left)
        if container[temp].right:
            container.append(container[temp].right)

        temp += 1
        if container[temp] == "*":
            if container[temp - 1] == "*":
                break
            temp += 1
            container.append("*")
    answer = []
    temp = ""
    for x in range(len(container)):
        if container[x] == "*":
            answer.append(temp[:len(temp) - 1])
            temp = ""
        else:
            temp += str(container[x].data) + " "
    for x in range(len(answer)):
        if (x + 1) % 2 == 1:
            print(" ".join(answer[x].split()[::-1]), end=" ")
        else:
            print(answer[x], end=" ")
    print()


if __name__ == '__main__':
    T = int(input())
    for z in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        t = Tree(arr[0])
        for i in range(1, N):
            rt = t.insert(t.root, arr[i])
        bottomUpLevelOrder(rt)
