class Stack:
    stack = []
    top = -1

    def push(self, element):
        self.top += 1
        self.stack.insert(self.top, element)

    def pop(self):
        self.top -= 1


if __name__ == '__main__':
    t = int(input())
    for z in range(t):
        n = int(input())
        brackets = input()
        s = Stack()
        for i in brackets:
            if i == '(':
                s.push(i)
            elif i == ")" and s.top > -1:
                s.pop()
        print(s.top + 1)
