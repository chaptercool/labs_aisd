class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    def size(self):
        return len(self.items)

def onp(zd):
    s = Stack()
    for a in zd:
        if a.isdigit():
            s.push(int(a))
        else:
            l2 = s.pop()
            l1 = s.pop()
            if a == "+":
                w = l1 + l2
            elif a == "-":
                w = l1 - l2
            elif a == "*":
                w = l1 * l2
            elif a == "/":
                w = l1 / l2
            elif a == "^":
                w = l1 ** l2
            s.push(w)
    return s.pop()


d = "73+52-2^*="
print(onp(d))
