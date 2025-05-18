N = int(input())
lst = list(map(int, input().split()))

a = sorted(lst)
center_m = a[N//2 - 1]
center_p = a[N//2]

#print (center_m, center_p)

for i in lst:
    if i <= center_m:
        print (center_p)
    else:
        print (center_m)