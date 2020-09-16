def eat1(number):
    print(f'Eat {number}')  # print before recursion
    if number <= 1:  # base case
        return 1
    else:  # recursive case
        return 1 + eat1(number-1)


def eat2(number):
    if number <= 1:  # base case
        result = 1
    else:  # recursive case
        result = 1 + eat2(number-1)  # recursion before print
    print(f'Eat: {number}')
    return result


if __name__ == '__main__':
    print(eat1(5))  # will print from n-1
    print('-----------------------------------')
    print(eat2(5))  # will print from 1-n0
