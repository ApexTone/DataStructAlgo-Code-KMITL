def sum_list_rec(lst, start, end):  # up to but not including end index
    if start == end-1:  # base case
        return lst[start]
    else:  # recursive case
        return lst[start] + sum_list_rec(lst, start+1, end)  # up to but not including end index


def sum_list_iter(lst, start, end):
    res = 0
    for i in range(start, end):
        res += lst[i]
    return res


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 50, 6, 7, 8, 9, 10, 99]
    print(sum_list_iter(lst, 0, len(lst)), sum_list_rec(lst, 0, len(lst)))
