# is a CBT
# current >= child nodes
# implementation using arrays and one based indexing


class MinHeap:
    a = []

    def __init__(self):
        self.a.append("Garbage")

    def getMin(self):
        return self.a[1]

    def size(self):
        return len(self.a)

    def insert(self, x):
        self.a.append(x)
        pos = len(self.a) - 1
        while (pos != 1) and (self.a[pos] < self.a[pos // 2]):
            self.a[pos], self.a[pos // 2] = self.a[pos // 2], self.a[pos]
            pos = pos // 2

    def deleteMin(self):
        self.a[1] = self.a.pop(len(self.a) - 1)
        pos = 1
        while pos < len(self.a) - 1:
            idx = 2*pos if self.a[2*pos] > self.a[2*pos + 1] else 2*pos + 1
