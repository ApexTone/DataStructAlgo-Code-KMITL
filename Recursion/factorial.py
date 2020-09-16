def fac_rec(n):
    if n == 2:  # base case
        return 2
    elif n <= 1:  # base case
        return 1
    else:  # recursive case
        return n * fac_rec(n-1)


def fac_iter(n):
    res = 1
    if n == 2:
        res = 2
    for i in range(2, n+1):
        res *= i
    return res


if __name__ == '__main__':
    number = 5
    print(fac_iter(number))
    print(fac_rec(number))
