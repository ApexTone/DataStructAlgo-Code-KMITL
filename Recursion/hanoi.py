def hanoi(disks, start, end, filler):
    if disks != 1:
        hanoi(disks-1, start, filler, end)  # move all smaller disks to filler pole first so you can move biggest disk
        print(f'move {disks} from {start} to {end}')  # move biggest disk to ending pole
        hanoi(disks-1, filler, end, start)  # move all smaller disks to ending pole
    else:
        print(f'move {disks} from {start} to {end}')


if __name__ == '__main__':
    disks = 2
    hanoi(disks, 'A', 'C', 'B')
