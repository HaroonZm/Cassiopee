N = int(input())
A = list(map(int, input().split()))
cnt = 0
while True:
    is_all_even = True
    for i in A:
        if i % 2 != 0:
            is_all_even = False
            break
    if is_all_even:
        new_A = []
        for i in A:
            new_A.append(i / 2)
        A = new_A
        cnt += 1
    else:
        break
print(cnt)