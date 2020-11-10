def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    first = merge_sort(lst[:len(lst)//2])
    second = merge_sort(lst[len(lst)//2:])
    return merge(first, second)


def merge(lst1, lst2):
    out_lst = []
    lst1_index = 0
    lst2_index = 0
    while lst1_index < len(lst1) and lst2_index < len(lst2):
        if lst1[lst1_index] >= lst2[lst2_index]:
            out_lst.append(lst1[lst1_index])
            lst1_index += 1
        else:
            out_lst.append(lst2[lst2_index])
            lst2_index += 1
    for i in range(lst1_index, len(lst1)):
        out_lst.append(lst1[i])
    for i in range(lst2_index, len(lst2)):
        out_lst.append(lst2[i])
    return out_lst


if __name__ == '__main__':
    lst = list(map(int, input("Enter list of number : ").split()))
    sorted_lst = merge_sort(lst)
    print(sorted_lst)