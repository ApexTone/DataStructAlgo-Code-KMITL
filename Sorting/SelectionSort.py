def selection_sort(in_list):
    lst = in_list.copy()
    for i in range(len(lst)):
        min_value = 99999999999999999
        min_index = i
        for j in range(i, len(lst)):
            if lst[j] <= min_value:
                min_index = j
                min_value = lst[j]
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


if __name__ == '__main__':
    lst = list(map(int, input("Enter list of number : ").split()))
    sorted_lst = selection_sort(lst)
    print(sorted_lst)
