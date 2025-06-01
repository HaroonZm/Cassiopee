n = int(input())
a = list(map(int, input().split()))
q = int(input())
commands = [tuple(map(int, input().split())) for _ in range(q)]

def is_sorted(seq):
    for i in range(len(seq)-1):
        if seq[i] > seq[i+1]:
            return False
    return True

if is_sorted(a):
    print(0)
else:
    result = -1
    for i, (x, y) in enumerate(commands, 1):
        # swap elements at positions x-1 and y-1
        a[x-1], a[y-1] = a[y-1], a[x-1]
        if is_sorted(a):
            result = i
            break
    print(result)