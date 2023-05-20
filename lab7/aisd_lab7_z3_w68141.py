class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self): #inaczej top - ostatni element
        return  self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


def znaki(znak: str) -> bool:
    s = Stack()
    popr = True
    index = 0
    while index < len(znak) and popr:
        a = znak[index]
        if a == "(" or a == "{" or a == "[" or a == "<":
            s.push(a)
        else:
            if s.size() == 0:
                popr = False
            elif a == ")" or a == "}" or a == "]" or a == ">":
                    s.pop()

        index += 1

    if s.size() == 0 and popr:
        return True
    else:
        return False


znak = "<[([<{>>]}])"
znak2 = "((({{{[[[))]]]>>)))"

print(znaki(znak))  # tu będzie prawda
print(znaki(znak2))  # tu będzie fałsz
