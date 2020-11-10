def shell_sort(in_lst, dimIncrement):
    lst = in_lst.copy()
    for d in dimIncrement:  # sort smaller section
        for i in range(d, len(lst)):  # insertion sort
            ith_elem = lst[i]
            for j in range(i, -1, -d):
                if ith_elem < lst[j-d] and j >= d:
                    lst[j] = lst[j-d]
                else:
                    lst[j] = ith_elem
                    break
    return lst


if __name__ == '__main__':
    lst = list(map(int, input("Enter list of number : ").split()))
    # Sedgewick: dim_inc should be 9*(4^i)-9*(2^i)+1 or (d^i)-3*(2^i)+1
    diminishing_increment = [5, 3, 1]  # Shell: ht = n//2, hk = hk+1 // 2
    sorted_lst = shell_sort(lst, diminishing_increment)
    print(sorted_lst)