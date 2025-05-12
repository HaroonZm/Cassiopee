def read_input():
    w, a, b = map(int, input().split())

    return (a, a + w), (b, b + w)

def submit():
    a, b = read_input()

    if a[0] < b[0]:
        print(max(b[0] - a[1], 0))
    else:
        print(max(a[0] - b[1], 0))

if __name__ == '__main__':
    submit()