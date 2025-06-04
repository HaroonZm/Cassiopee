def main():
    from sys import stdin
    l = stdin.readline
    values = l().split()
    x = int(values[0])
    y = int(values[1])
    res = 0
    for a, v in zip([x,y], range(2)):
        if a >= 1 and a <= 3:
            res += (4 - a) * pow(10,5)
    if x == 1 and y == 1:
        res = res + (4 * 10**5)
    print(res)
main()