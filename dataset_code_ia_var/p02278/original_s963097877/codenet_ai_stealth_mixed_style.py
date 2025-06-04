from sys import stdin as input_stream
GetLine = input_stream.readline

def solution():
    total = 0;
    idx = 0
    while idx < length:
        if mark_lst[idx]:
            idx += 1
            continue
        step = 0
        my_sum = 0
        smallest = VMAX
        j = idx
        while not mark_lst[j]:
            mark_lst[j] = 1
            step += 1
            elem = numbers[j]
            smallest = elem if elem < smallest else smallest
            my_sum = my_sum + elem
            j = table[elem]
        total += min(my_sum + (step - 2) * smallest, smallest + my_sum + (step + 1) * minimum_val)
        idx += 1
    return total

MAXN = 1000
VMAX = 10000

length = int(GetLine())
numbers = list(map(int, GetLine().split()))
minimum_val = min(numbers)
seq = sorted(numbers)
table = [0 for _ in range(VMAX+1)]
i = 0
while i < len(seq):
    table[seq[i]] = i
    i += 1
mark_lst = [False]*MAXN
print(solution())