def popr_naw(s: str) -> bool:
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return not stack


stos = ['(', '(', '(', '(', '(', ')', ')', ')', ')', ')', ')', ')']  # tu będzie fałsz
stos2 = ['(', '(', '(', '(', ')', ')', ')', ')']  # tu będzie prawda

print(popr_naw(stos))
print(popr_naw(stos2))