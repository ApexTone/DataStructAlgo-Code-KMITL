def binary_search_rec(lst, key, left, right):
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == key or lst[left] == key or lst[right] == key:  # base case
            # print('Found')
            return True
        elif lst[mid] < key:  # recursive case
            # print('Too low', lst[mid])
            return binary_search_rec(lst, key, mid+1, right)
        else:  # recursive case
            # print('Too high', lst[mid])
            return binary_search_rec(lst, key, left, mid)
    return False


def binary_search_iter(lst, key):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left+right)//2
        if lst[mid] == key or lst[left] == key or lst[right] == key:  # only for found or not found the key(cheese)
            # print('Found')
            return True
        elif lst[mid] < key:
            # print('Too low', lst[mid])
            left = mid+1
        else:
            # print('Too high', lst[mid])
            right = mid
    return False


if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 10, 8858]
    for item in lst:
        print("Iterative:", binary_search_iter(lst, item), "\tRecursive:", binary_search_rec(lst, item, 0, len(lst)-1))
