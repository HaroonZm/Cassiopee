l = []
i = 0
while i < 3:
    tmp = int(input())
    l += [tmp]
    i += 1

def get_inputs(n):
    result = []
    for _ in range(n):
        val = int(input())
        result.append(val)
    return result

j = get_inputs(2)

a = (lambda x, y: x + y - 50)(min(l), min(j))
print(a)