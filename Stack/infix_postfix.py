from Stack.stack import Stack


def infix_to_postfix_no_prior(exp):
    s = Stack()
    postfix = ''
    for i in exp:
        if i in '0123456789':
            postfix += i
        elif i in '+-*/(':
            s.push(i)
        elif i == ')':
            while s.peek() != '(':
                postfix += s.pop()
            s.pop()
    while not s.is_empty():
        postfix += s.pop()
    return postfix


def infix_to_postfix(exp):  # code this -> bug
    s = Stack()
    postfix = ''
    priority = {
        '(': -99,
        '+': 0,
        '-': 0,
        '*': 2,
        '/': 2,
    }
    for i in exp:
        # print(s)
        if i in '0123456789':
            postfix += i
        elif i in '+-*/':  # interesting part
            if s.is_empty():
                s.push(i)
            else:
                while not s.is_empty():
                    if s.peek() == '(':
                        break
                    else:
                        if priority.get(s.peek(),-2) < priority.get(i,-2):
                            break
                        else:
                            postfix += s.pop()
                s.push(i)
        elif i == '(':
            s.push(i)
        elif i == ')':
            while s.peek() != '(':
                postfix += s.pop()
            s.pop()
    while not s.is_empty():
        postfix += s.pop()
    return postfix


def postfix_cal(exp, is_postfix=False):
    # 6523+8*-3+* = -192
    if not is_postfix:
        postfix = infix_to_postfix(exp)
    else:
        postfix = exp
    # print(postfix)
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
        # print(s)
    return s.pop()


def compare(exp):
    # 1+2*3-(4/5+6)*7
    print("no prior:", infix_to_postfix_no_prior(exp))
    print("prior:", infix_to_postfix(exp)) # infinite loop

"""
Test input
2+3-1 -> 23+1-
2+3*1 -> 231*-
3*(4+5)-6/(1+2) -> 345+*612+/-
"""
if __name__ == '__main__':
    inp = input('Input expression: ')
    # compare(inp)
    print(postfix_cal(inp))

