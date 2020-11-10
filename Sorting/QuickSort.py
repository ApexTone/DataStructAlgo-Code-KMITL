def partition(lst, left, right, mode=0):
    if mode == 0:  # pivot last element
        i = left-1
        pivot = lst[right]  # pivot from the last element
        for j in range(left, right):  # from [left, right)
            if lst[j] < pivot:  # if current item is lesser than pivot
                i += 1
                lst[i], lst[j] = lst[j], lst[i]  # swap j element to the left side (i element will be >= pivot)
        lst[i+1], lst[right] = lst[right], lst[i+1]  # swap i index with the pivot (put pivot in correct place)
        print(lst)
        return i+1
    elif mode == 1:  # pivot first element
        i = right+1
        pivot = lst[left]
        for j in range(right, left-1, -1):
            if lst[j] > pivot:
                i -= 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i-1], lst[left] = lst[left], lst[i-1]
        print(lst)
        return i-1
    else:
        print("Invalid mode (0=pivot last,1=pivot first)")
        return



def quick_sort(lst, left, right):
    if left < right:
        partition_index = partition(lst, left, right, 1)  # partition (get pivot in the right position)
        quick_sort(lst, left, partition_index-1)  # sort left side of pivot
        quick_sort(lst, partition_index+1, right)  # sort right side of pivot


if __name__ == '__main__':
    lst = list(map(int, input("Enter list of number : ").split()))
    quick_sort(lst, 0, len(lst)-1)
    print(lst)
