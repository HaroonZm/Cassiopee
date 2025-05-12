n = int(input())
k, *b_arr = map(int, input().split())
masks = [1 << x for x in range(n)]
b_mask = 0
for b in b_arr:
    b_mask += 1 << b

for i in range(1 << n):
    if i & b_mask != b_mask:
        continue
    sub = [idx for idx, mask in enumerate(masks) if i & mask != 0b00]
    print('{}: {}'.format(i, ' '.join(map(str, sub)))) if len(sub) != 0 else print(f'{i}:')