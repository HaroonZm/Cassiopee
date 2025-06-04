n_s = input().split()
n = int(n_s[0])
s = int(n_s[1])
li = [int(x) for x in input().split()]

if s > sum(li):
    print(0)
elif s < max(li):
    print(1)
else:
    i = 0
    j = n
    while i + 1 < j:
        mid = (i + j) // 2
        found = False
        sum_ = sum(li[:mid])
        if s <= sum_:
            found = True
        else:
            k = 0
            l = len(li) - mid
            while k < l:
                sum_ -= li[k]
                sum_ += li[k + mid]
                if s <= sum_:
                    found = True
                    break
                k += 1
        if found:
            j = mid
        else:
            i = mid
    print(j)