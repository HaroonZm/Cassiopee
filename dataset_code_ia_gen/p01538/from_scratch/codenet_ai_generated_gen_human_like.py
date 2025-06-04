q = int(input())
for _ in range(q):
    n = input().strip()
    count = 0
    seen = set()
    while len(n) > 1:
        if n in seen:
            count = -1
            break
        seen.add(n)
        max_product = -1
        length = len(n)
        for i in range(1, length):
            left = n[:i]
            right = n[i:]
            product = int(left) * int(right)
            if product > max_product:
                max_product = product
        n = str(max_product)
        count += 1
    print(count)