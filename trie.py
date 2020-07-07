class Trie:
    ar = []
    eow = False
    count = 0

    def __init__(self):
        self.ar = [None] * 26


def insert(root, word):
    for i in range(len(word)):
        idx = ord(word[i]) - 97
        if root.ar[idx] is None:
            root.ar[idx] = Trie()
        root = root.ar[idx]
        root.count += 1
    root.eow = True


def search(root, word):
    ans = 0
    for i in range(len(word)):
        idx = ord(word[i]) - 97
        if root.ar[idx] is None:
            return ans
        root = root.ar[idx]
    ans += root.count
    return ans


if __name__ == '__main__':
    n = int(input())
    rt = Trie()
    for i in range(n):
        temp = rt
        a = input()
        if a.split()[0] == "add":
            insert(temp, a.split()[1])
        else:
            print(search(temp, a.split()[1]))
