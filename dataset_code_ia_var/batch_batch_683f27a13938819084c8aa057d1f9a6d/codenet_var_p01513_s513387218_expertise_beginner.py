while True:
    n = int(input())
    if n == 0:
        break
    m = []
    for i in range(n):
        ligne = input().split()
        nums = []
        for j in range(1, len(ligne)):
            nums.append(int(ligne[j]))
        m.append(set(nums))
    k_ligne = input().split()
    k = set()
    for j in range(1, len(k_ligne)):
        k.add(int(k_ligne[j]))
    f = []
    for i in range(n):
        if k.issubset(m[i]):
            f.append(i+1)
    if len(f) == 1:
        print(f[0])
    else:
        print(-1)