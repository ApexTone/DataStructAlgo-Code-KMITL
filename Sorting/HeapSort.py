def make_heap(lst, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and lst[i] < lst[l]:
        largest = l
    if r < n and lst[largest] < lst[r]:
        largest = r

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        make_heap(lst, n, largest)


def heap_sort(lst):
    n = len(lst)
    for i in range(n//2-1, -1, -1):
        make_heap(lst, n, i)
    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        make_heap(lst, i, 0)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    heap_sort(arr)
    print(arr)
