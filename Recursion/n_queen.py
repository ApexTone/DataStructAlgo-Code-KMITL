n = 4
num_sol = 0
b = n * [-1]
col_free = n * [1]
up_free = (2*n-1) * [1]
down_free = (2*n-1) * [1]


def print_board(b):
    print(b)


def put_queen(r, b, col_free, up_free, down_free):  # bug?
    global n
    global num_sol
    for i in range(n):
        if col_free[i] and up_free[i+r] and down_free[r-i+n-1]:
            b[r] = i
        col_free[i] = up_free[i+r] = down_free[r-i+n-1] = 0
        if r == n-1:
            print_board(b)
            num_sol += 1
        else:
            put_queen(r + 1, b, col_free, up_free, down_free)
        col_free[i] = up_free[i+r] = down_free[r-i+n-1] = 1


if __name__ == '__main__':
    put_queen(0, b, col_free, up_free, down_free)