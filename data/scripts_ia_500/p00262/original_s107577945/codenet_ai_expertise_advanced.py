def is_triangular_number(n: int) -> bool:
    from math import sqrt
    x = int((sqrt(8 * n + 1) - 1) // 2)
    return x * (x + 1) // 2 == n

def is_sequential(lst: list[int]) -> bool:
    return all(val == idx + 1 for idx, val in enumerate(lst))

while True:
    n = int(input())
    if n == 0:
        break
    
    blocks = list(map(int, input().split()))
    if not is_triangular_number(sum(blocks)):
        print(-1)
        continue
    
    count = 0
    while count <= 10000:
        if is_sequential(blocks):
            print(count)
            break
        count += 1
        blocks = [x - 1 for x in blocks if x > 1] + [len(blocks)]
    else:
        print(-1)