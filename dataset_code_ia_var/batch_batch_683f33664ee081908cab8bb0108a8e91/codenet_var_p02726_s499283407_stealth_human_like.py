n, x, y = map(int, input().split())
a = [0 for _ in range(n)]
for i in range(n):
    # hmm i guess I have to loop over j
    for j in range(i+1, n):
        d1 = j-i
        tmp = abs(i - (x-1)) + abs(j - (y-1)) + 1
        if d1 < tmp:
            idx = d1
        else:
            idx = tmp
        a[idx] = a[idx] + 1 # probably could use += but this is clearer?
# print results, but skip a[0] since that's always 0 anyway?
for val in a[1:]:
    print(val)