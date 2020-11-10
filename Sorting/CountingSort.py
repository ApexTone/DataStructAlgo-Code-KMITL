# extra
def counting_sort(in_lst):
    tmp = [0]*(max(in_lst)+1)
    for item in in_lst:
        tmp[item] += 1
    print(tmp)
    out = []
    for i in range(len(tmp)):
        for j in range(tmp[i]):
            out.append(i)
    return out


if __name__ == '__main__':
    lst = list(map(int, input("Enter list of number : ").split()))
    sorted_lst = counting_sort(lst)
    print(sorted_lst)