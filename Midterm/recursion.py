def rec_factorial(n):
    if 0 <= n <= 1:
        return 1
    else:
        return n * rec_factorial(n-1)


def iter_factorial(n):
    if 0 <= n <= 1:
        return 1
    else:
        ans = 1
        for i in range(1, n+1):
            ans *= i
        return ans


def permute(lst, start_index, end_index):
    if start_index == end_index:
        print(lst)
    else:
        for i in range(start_index, end_index+1):
            lst[start_index], lst[i] = lst[i], lst[start_index]  # swap
            permute(lst, start_index+1, end_index)  # permutation after swap
            lst[start_index], lst[i] = lst[i], lst[start_index]  # backtrack


def hanoi(n, start, filler, dest):
    if n == 1:
        print(f"move {n} from  {start} to {dest}")
    else:
        hanoi(n-1, start, dest, filler)
        print(f"move {n} from  {start} to {dest}")
        hanoi(n-1, filler, start, dest)


def rec_min(lst, acc_min=99999999):
    if len(lst) == 0:
        return acc_min
    else:
        num = lst.pop()
        if acc_min > num:
            acc_min = num
        return rec_min(lst, acc_min)


def rec_sum_list(lst, value=0):
    if len(lst) == 0:
        print('Empty List')
        return -1
    elif len(lst) == 1:
        return value + lst[0]
    else:
        value += lst[0]
        return rec_sum_list(lst[1:], value)


if __name__ == '__main__':
    x = int(input())
    print(rec_factorial(x))
    print(iter_factorial(x))

    permute([1, 2, 3, 4], 0, 3)

    hanoi(3, 'A', 'B', 'C')

    print(rec_sum_list([-99, 99, 100, 2, 3, 4]))
