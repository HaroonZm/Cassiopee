n = int(input())
def get_sorted_number(s, reverse=False):
    arr=[]
    for ch in s: arr.append(ch)
    arr.sort(reverse=reverse)
    return int("".join(arr))
for _ in range(n):
    s=input()
    mx = get_sorted_number(s, True)
    mn = ''.join(sorted(list(s)))
    print(mx-int(mn))