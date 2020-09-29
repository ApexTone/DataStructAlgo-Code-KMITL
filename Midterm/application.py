class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return 'Stack is Empty'

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Empty Stack")
            return -1

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


def paren_matching(line):
    def is_match(p_close, p_open):
        closing = {')': '(',
                   '}': '{',
                   ']': '['}
        opening = {y: x for x, y in closing.items()}
        return closing.get(p_close, None) == p_open or opening.get(p_open, None) == p_close

    s = Stack()
    for character in line:
        if character in '({[':
            s.push(character)
        elif character in ')}]':
            if not s.is_empty():
                buffer = s.pop()
                if not is_match(character, buffer):
                    print(f'Parenthesis not match: {buffer} {character}')
                    break
            else:
                print("Excessive closing parenthesis")
                break
    else:  # do when loop end without break
        if s.is_empty():
            print('Balanced parenthesis')
        else:
            print('Excessive opening parenthesis')


def infix_to_postfix(exp):
    s = Stack()
    postfix = ''
    priority = {'(': -99, '+': 0, '-': 0, '*': 2, '/': 2}
    for i in exp:
        if i in '+-*/':
            if s.is_empty():
                s.push(i)
            else:
                while not s.is_empty():
                    if s.peek() == '(':
                        break
                    else:
                        if priority.get(s.peek(), -2) < priority.get(i, -2):
                            break
                        else:
                            postfix += str(s.pop())
                s.push(i)
        elif i == '(':
            s.push(i)
        elif i == ')':
            while s.peek() != '(':
                postfix += str(s.pop())
            s.pop()
        else:
            postfix += i
    while not s.is_empty():
        postfix += str(s.pop())
    return postfix


def postfix_cal(exp, is_postfix=False):
    if not is_postfix:
        postfix = infix_to_postfix(exp)
    else:
        postfix = exp
    s = Stack()
    for i in postfix:
        if i in '0123456789':
            s.push(int(i))
        else:
            a = s.pop()
            b = s.pop()
            if i == '+':
                s.push(b+a)
            elif i == '-':
                s.push(b-a)
            elif i == '*':
                s.push(b*a)
            elif i == '/':
                s.push(b/a)
    return s.pop()


def stack_calculation():
    """
    Test input
    2+3-1 -> 23+1-
    2+3*1 -> 231*-
    3*(4+5)-6/(1+2) -> 345+*612+/-
    """
    inp = input('Input expression: ')
    postfix = infix_to_postfix(inp)
    print(postfix)
    print(postfix_cal(postfix))


if __name__ == '__main__':
    stack_calculation()
