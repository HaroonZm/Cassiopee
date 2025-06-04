nb = int(input())
lst = list(map(int, input().split()))

if nb < 3:
    print(0)
    quit()

def desc_sort(L):
    L.sort()
    L.reverse()
desc_sort(lst)

res = 0
LN = len(lst)
i = 0
while i < LN:
    for j in range(i+1, LN):
        k = j + 1
        while k < LN:
            a = lst[i]
            b = lst[j]
            c = lst[k]
            if len(set([a,b,c])) != 3:
                k += 1
                continue
            if a < b + c:
                res = res + 1
            k += 1
    i += 1
print(res)