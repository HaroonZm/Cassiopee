try:
    N, M, K = (int(item) for item in input().split())
except ValueError as Oops:
    print("Input Error:", Oops)
    quit()
i = 0
checked = False
while i <= N:
    j = 0
    while j <= M:
        formula = M*i + N*j - 2*(i*j)
        if formula == K:
            print("Yes")
            checked = True
            break
        j += 1
    if checked:
        break
    i += 1
else:
    print("No")