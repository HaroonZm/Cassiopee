while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for i in range(n):
        items = input().split()
        row = set()
        for num in items[1:]:
            row.add(int(num))
        a.append(row)
    b_input = input().split()
    b = set()
    for num in b_input[1:]:
        b.add(int(num))
    result = []
    for i in range(n):
        if b.issubset(a[i]):
            result.append(i + 1)
    if len(result) == 1:
        print(result[0])
    else:
        print(-1)