n = int(input())
s = input()
ans = ['S'] * n
ani0 = ['S', 'S', 'W', 'W']
ani1 = ['S', 'W', 'S', 'W']
anim1 = ['S', 'W', 'W', 'S']
for i in range(4):
    ans[0] = ani0[i]
    if s[0] == 'o':
        ans[-1] = anim1[i]
        ans[1] = ani1[i]
    else:
        ans[-1] = anim1[3 - i]
        ans[1] = ani1[3 - i]
    for j in range(1, n):
        if j >= n - 2:
            if s[j] == 'o':
                if ans[j] == 'S':
                    if ans[j - 1] == 'S':
                        if ans[(j + 1) % n] == 'S':
                            if j == n - 1:
                                print(*ans, sep='')
                                exit()
                        else:
                            break
                    else:
                        if ans[(j + 1) % n] == 'W':
                            if j == n - 1:
                                print(*ans, sep='')
                                exit()
                        else:
                            break
                else:
                    if ans[j - 1] == 'S':
                        if ans[(j + 1) % n] == 'W':
                            if j == n - 1:
                                print(*ans, sep='')
                                exit()
                        else:
                            break
                    else:
                        if ans[(j + 1) % n] == 'S':
                            if j == n - 1:
                                print(*ans, sep='')
                                exit()
                        else:
                            break
            else:
                if ans[j] == 'S':
                    if ans[j - 1] == 'S':
                        if ans[(j + 1) % n] == 'W':
                            if j == n - 1:
                                print(*ans, sep='')
                                exit()
                        else:
                            break
                    else:
                        if ans[(j + 1) % n] == 'S':
                            if j == n - 1:
                                print(*ans, sep='')
                                exit()
                        else:
                            break
                else:
                    if ans[j - 1] == 'S':
                        if ans[(j + 1) % n] == 'S':
                            if j == n - 1:
                                print(*ans, sep='')
                                exit()
                        else:
                            break
                    else:
                        if ans[(j + 1) % n] == 'W':
                            if j == n - 1:
                                print(*ans, sep='')
                                exit()
                        else:
                            break
        if j == n - 1:
            break
        if s[j] == 'o':
            if ans[j] == 'S':
                if ans[j - 1] == 'S':
                    ans[j + 1] = 'S'
                else:
                    ans[j + 1] = 'W'
            else:
                if ans[j - 1] == 'S':
                    ans[j + 1] = 'W'
                else:
                    ans[j + 1] = 'S'
        else:
            if ans[j] == 'S':
                if ans[j - 1] == 'S':
                    ans[j + 1] = 'W'
                else:
                    ans[j + 1] = 'S'
            else:
                if ans[j - 1] == 'S':
                    ans[j + 1] = 'S'
                else:
                    ans[j + 1] = 'W'
print(-1)