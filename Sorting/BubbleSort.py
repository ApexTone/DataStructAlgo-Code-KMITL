def bubble_sort(in_list):
    lst = in_list.copy()
    for i in range(len(lst)):
        swapped = False
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                swapped = True
        if not swapped:
            break
    return lst


if __name__ == "__main__":
    lst = list(map(int, input("Enter list of number : ").split()))
    sorted_lst = bubble_sort(lst)
    print(sorted_lst)
