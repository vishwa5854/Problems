class Stack:
    stack = []
    top = -1

    def push(self, element):
        self.top += 1
        self.stack.insert(self.top, element)

    def pop(self):
        self.top -= 1


if __name__ == '__main__':
    T = int(input())
    stack = Stack()
    for z in range(T):
        a = input().split()
        if a[0] == "push":
            stack.push(int(a[1]))
        if a[0] == "pop":
            if stack.top == -1:
                print("Empty")
            else:
                print(stack.stack[stack.top])
                stack.pop()
