def insertion_sort(in_list):
    lst = in_list.copy()
    for i in range(1, len(lst)):  # start from index 1 (skip 0)
        curr_value = lst[i]
        for j in range(i, -1, -1):  # traverse from right to left
            if curr_value <= lst[j-1] and j > 0:  # if not where to insert... (j>0 prevent access to [-1] index)
                lst[j] = lst[j-1]  # shift data to the right
            else:
                lst[j] = curr_value  # "insert"
                break
    return lst


if __name__ == '__main__':
    lst = list(map(int, input("Enter list of number : ").split()))
    sorted_lst = insertion_sort(lst)
    print(sorted_lst)
