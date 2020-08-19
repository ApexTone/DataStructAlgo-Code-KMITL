from Stack.stack import Stack  # importing stack
import time


def is_match(p_close, p_open):
    closing = {')': '(',
               '}': '{',
               ']': '['}
    opening = {y: x for x, y in closing.items()}
    # print(opening)
    return closing.get(p_close, None) == p_open or opening.get(p_open, None) == p_close


def parenthesis_matching(line):
    start = time.time()
    s = Stack()
    error_code = 0
    index = 0
    buffer = ''
    for character in line:
        buffer = character
        if character in '({[':
            s.push(character)
        elif character in ')}]':
            if not s.is_empty():
                if not is_match(character, s.pop()):
                    error_code = 1  # open/close not match
                    break
            else:
                error_code = 2  # no prior open parenthesis (stack empty)
                break
        index += 1

    if not s.is_empty():  # there are open parenthesis left in stack
        error_code = 3
    print('Total time:', time.time()-start)
    return error_code, buffer, index, s


def test_parenthesis_matching(line):
    # text = '[{a+b-c}'
    text = line
    err, c, i, s = parenthesis_matching(text)
    if err == 1:
        print(text, 'unmatched open/close')
    elif err == 2:
        print(text, 'excessive closing parenthesis')
    elif err == 3:
        print(text, 'excessive open parenthesis', s.size, ':', end="")
        for item in s.items:
            print(item, sep="", end="")
        print()
    else:
        print(text, 'match')


def my_paren_matching(line):
    start = time.time()
    s = Stack()
    for character in line:
        if character in '({[':
            s.push(character)
        elif character in ')}]':
            buffer = s.pop()
            if not is_match(character, buffer):
                print(f'Parenthesis not match: {buffer} {character}')
                break
    else:  # do when loop end without break
        if s.is_empty():
            print('Balanced parenthesis')
        else:
            print('Parenthesis is not balance')
    print('Total time:', time.time() - start)


if __name__ == '__main__':
    inp = input('Input checking parenthesis : ')
    test_parenthesis_matching(inp)
    my_paren_matching(inp)
