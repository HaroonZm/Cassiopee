def main():
    import sys
    # On n'utilise pas deque, on fait simple avec une liste comme pile
    while True:
        n_m = input().split()
        n = int(n_m[0])
        m = int(n_m[1])
        if n == 0 and m == 0:
            return
        line1 = input().split()
        line2 = input().split()
        line3 = input().split()
        a = [int(x) for x in line1[1:]]
        b = [int(x) for x in line2[1:]]
        c = [int(x) for x in line3[1:]]
        a = [0] + a
        b = [0] + b
        c = [0] + c

        stack = []
        stack.append([a, b, c, 0, -1])
        target = []
        for i in range(0, n+1):
            target.append(i)

        while len(stack) > 0:
            state = stack.pop()
            a = state[0]
            b = state[1]
            c = state[2]
            d = state[3]
            t = state[4]

            if d > m:
                print(-1)
                break
            if a == target or c == target:
                print(d)
                break

            # a vers b
            if a[-1] > b[-1] and t != 1:
                new_a = a[:-1]
                new_b = b + [a[-1]]
                new_c = c[:]
                stack.append([new_a, new_b, new_c, d+1, 0])
            # b vers a
            if b[-1] > a[-1] and t != 0:
                new_a = a + [b[-1]]
                new_b = b[:-1]
                new_c = c[:]
                stack.append([new_a, new_b, new_c, d+1, 1])
            # b vers c
            if b[-1] > c[-1] and t != 3:
                new_a = a[:]
                new_b = b[:-1]
                new_c = c + [b[-1]]
                stack.append([new_a, new_b, new_c, d+1, 2])
            # c vers b
            if c[-1] > b[-1] and t != 2:
                new_a = a[:]
                new_b = b + [c[-1]]
                new_c = c[:-1]
                stack.append([new_a, new_b, new_c, d+1, 3])

if __name__ == "__main__":
    main()