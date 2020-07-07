class QueueDataStructure:
    queue = []
    front = -1
    rear = -1

    def isEmpty(self):
        return self.front == -1

    def enqueue(self, element):
        if self.rear == -1:
            self.rear = 0
            self.front = 0
        else:
            self.rear += 1
        self.queue.insert(self.rear, element)

    def dequeue(self):
        if self.isEmpty():
            print("Empty")
            return

        print(self.queue[self.front])
        self.front += 1


n = int(input())
for i in range(n):
    a = input().split()
    q = QueueDataStructure()
    if a[0][0] == "E":
        q.enqueue(a[1])
    else:
        q.dequeue()
