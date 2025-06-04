n=int(input())
cards=input().split()
def val(card): return int(card[1:])
def bubble_sort(arr):
    res=arr[:]
    n=len(res)
    for i in range(n):
        for j in range(n-1,i,-1):
            if val(res[j])<val(res[j-1]):
                res[j],res[j-1]=res[j-1],res[j]
    return res
def selection_sort(arr):
    res=arr[:]
    n=len(res)
    for i in range(n):
        mini=i
        for j in range(i,n):
            if val(res[j])<val(res[mini]):
                mini=j
        res[i],res[mini]=res[mini],res[i]
    return res
def is_stable(original,sorted_arr):
    from collections import defaultdict
    pos=defaultdict(list)
    for i,c in enumerate(original):
        pos[val(c)].append(c)
    for c in sorted_arr:
        v=val(c)
        if pos[v].pop(0)!=c:
            return False
    return True
bs=bubble_sort(cards)
ss=selection_sort(cards)
print(*bs)
print("Stable" if is_stable(cards,bs) else "Not stable")
print(*ss)
print("Stable" if is_stable(cards,ss) else "Not stable")