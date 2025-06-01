from sys import stdin

def main():
    num_vlines, num_wlines = map(int, (stdin.readline() for _ in range(2)))
    amida = list(range(num_vlines + 1))

    for _ in range(num_wlines):
        a, b = map(int, stdin.readline().strip().split(','))
        amida[a], amida[b] = amida[b], amida[a]

    print('\n'.join(map(str, amida[1:]))) 

if __name__ == '__main__':
    main()