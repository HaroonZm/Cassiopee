'''
CODE FESTIVAL 2016 Final
B - Exactly N points
'''

if __name__ == "__main__":
    N = int(input())
    ans = list()
    res = N
    tmp = 1
    while True:
        if res <= 0:
            if res == 0:
                break
            else:
                ans.pop(ans.index(abs(res)))
                break
        ans.append(tmp)
        res -= tmp
        tmp += 1

    for a in ans:
        print(a)