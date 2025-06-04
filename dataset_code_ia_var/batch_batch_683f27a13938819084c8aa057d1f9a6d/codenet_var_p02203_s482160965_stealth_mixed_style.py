def get_n(): return int(input())
def get_list(): return [int(x) for x in input().split()]

n = get_n()
array = get_list()

answer = 1
i = 1
last = array[0]

while i < n:
    if not (array[i] > last):
        answer = answer + 1
    last = array[i]
    i += 1

print(answer)
for m in [n]: print(m)