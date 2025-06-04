def solve():

    initial_orientation, toggle_command = input().split()

    if initial_orientation == 'H':
        print(toggle_command)
    else:
        if toggle_command == 'H':
            print('D')
        else:
            print('H')


if __name__ == "__main__":
    solve()