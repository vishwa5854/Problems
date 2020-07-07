class Node:
    next = None

    def __init__(self, data):
        self.val = data


def insert(data):
    a = Node(data[0])
    temp = a
    for i in range(1, len(data)):
        a.next = Node(data[i])
        a = a.next
    return temp


def removeDuplicates(head):
    a = head
    while head.next is not None:
        if head.val == head.next.val:
            if head.next.next is not None:
                head.next = head.next.next
            else:
                head.next = None
        head = head.next
    return a


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    a = insert(arr)
    a = removeDuplicates(a)
    while a is not None:
        print(a.val)
        a = a.next
