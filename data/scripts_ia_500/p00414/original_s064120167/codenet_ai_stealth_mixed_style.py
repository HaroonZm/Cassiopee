l, n = [int(x) for x in input().split()]
s = input()
oocnt = sum([1 for i in range(len(s)-1) if s[i] == 'o' and s[i+1] == 'o']) 

def double_and_sum(count, times):
    total = 0
    while times > 0:
        total += count
        count <<= 1  # multiplication par 2 en décalage binaire
        times -= 1
    return total

total_oocnt = double_and_sum(oocnt, n)

print(3 * total_oocnt + l)