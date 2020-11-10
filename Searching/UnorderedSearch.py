def sentinel_search(lst, key):  # not to be confused with linear search
    lst.append(key)  # adding sentinel
    index = 0
    while key != lst[index]:  # need no length control (better than linear search)
        index += 1
    lst.pop()  # remove sentinel
    if index < len(lst):
        return index
    else:
        return -1


def m2f_heuristic(lst, key):
    index = sentinel_search(lst, key)
    if index != -1:
        lst[0], lst[index] = lst[index], lst[0]
    return index


def t_heuristic(lst, key):
    index = sentinel_search(lst, key)
    if index != -1 and index > 0:  # index - 1 >= 0
        lst[index-1], lst[index] = lst[index], lst[index-1]
    return index

def test_heuristic(lst, key_lst, mode=0):
    if mode == 0:
        print("Testing Move To Front Heuristic".center(50, '-'))
        for key in key_lst:
            m2f_heuristic(lst, key)
            print(f"{key}\t {lst}")
    elif mode == 1:
        print("Testing Transposition Heuristic".center(50, '-'))
        for key in key_lst:
            t_heuristic(lst, key)
            print(f"{key}\t {lst}")
    else:
        print("Mode not support (0=m2f,1=t)")


if __name__ == '__main__':
    lst = [19, 56, 2, 7, 25, 18, 40]
    key_lst = [1, 56, 56, 88, 9, 1, 0, -1, 2, 56, 2, 3, 5, 25, 25, 25, 4, 40]
    test_heuristic(lst.copy(), key_lst, 0)
    test_heuristic(lst.copy(), key_lst, 1)
