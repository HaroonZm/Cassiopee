def main():
    while True:
        line = input()
        n_m = line.split()
        n = int(n_m[0])
        m = int(n_m[1])
        if n == 0 and m == 0:
            break

        a_line = input().split()
        b_line = input().split()
        c_line = input().split()
        a = []
        b = []
        c = []
        for i in range(1, len(a_line)):
            a.append(int(a_line[i]))
        for i in range(1, len(b_line)):
            b.append(int(b_line[i]))
        for i in range(1, len(c_line)):
            c.append(int(c_line[i]))
        a.insert(0, 0)
        b.insert(0, 0)
        c.insert(0, 0)

        queue = []
        queue.append([a, b, c, 0, -1])
        tmp = []
        for i in range(n+1):
            tmp.append(i)

        while len(queue) > 0:
            state = queue.pop()
            a = state[0]
            b = state[1]
            c = state[2]
            d = state[3]
            t = state[4]

            if d > m:
                print(-1)
                break

            if a == tmp or c == tmp:
                print(d)
                break

            # a to b
            if a[-1] > b[-1] and t != 1 and t != 0:
                new_a = a[:-1]
                new_b = b + [a[-1]]
                new_c = c[:]
                queue.insert(0, [new_a, new_b, new_c, d+1, 0])
            # b to a
            if b[-1] > a[-1] and t != 0 and t != 1:
                new_a = a + [b[-1]]
                new_b = b[:-1]
                new_c = c[:]
                queue.insert(0, [new_a, new_b, new_c, d+1, 1])
            # b to c
            if b[-1] > c[-1] and t != 3 and t != 2:
                new_a = a[:]
                new_b = b[:-1]
                new_c = c + [b[-1]]
                queue.insert(0, [new_a, new_b, new_c, d+1, 2])
            # c to b
            if c[-1] > b[-1] and t != 2 and t != 3:
                new_a = a[:]
                new_b = b + [c[-1]]
                new_c = c[:-1]
                queue.insert(0, [new_a, new_b, new_c, d+1, 3])

if __name__ == '__main__':
    main()