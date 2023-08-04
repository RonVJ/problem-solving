from collections import deque


def balance_brackets(self, s):
    n = len(s)
    i = 0
    stack = deque()

    while i < n:
        c = s[i]
        if (c == '(') or (c == '[') or (c == '{'):
            stack.append(c)
        else:
            top = stack.pop()
            if c == ')':
                if top != '(':
                    return False
            elif c == ']':
                if top != '[':
                    return False
            elif c == '}':
                if top != '{':
                    return False
            else:
                return False
        i = i + 1

    if len(stack) == 0:
        return True
    return False
