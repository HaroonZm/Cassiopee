def check(ary):
    for i in range(1, len(ary)):
        if ary[i] < ary[i - 1]:
            return False

    return True

def dfs(a, b, c, i):
    if len(b) + len(c) == 10:
        return check(b) and check(c)

    added_b = b[:]
    added_c = c[:]
    added_b.append(a[i])
    added_c.append(a[i])

    return dfs(a, added_b, c, i + 1) or dfs(a, b, added_c, i + 1)

def main():
    n = int(input())
    for i in range(n):
        datasets = [int(i) for i in input().split(' ')]
        result = dfs(datasets, [], [], 0)
        print('YES' if result else 'NO')

if __name__ == '__main__':
    main()