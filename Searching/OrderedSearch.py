def linear_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1


def binary_search(lst, key):
    left = 0
    right = len(lst)-1
    while left <= right:
        mid = (left+right)//2
        if lst[mid] > key:
            right = mid-1
        elif lst[mid] < key:
            left = mid+1
        else:
            return mid
    return -1


if __name__ == '__main__':
    lst = [2, 5, 7, 8, 10, 12, 15, 18, 20, 22]
    key_lst = [1, 56, 56, 8, 9, 1, 0, 20, 2, 26, 22, 3, 5, 25, 25, 25, 4, 40]
    for key in key_lst:
        print(linear_search(lst, key))
        print(binary_search(lst, key))
        print('-'*30)
