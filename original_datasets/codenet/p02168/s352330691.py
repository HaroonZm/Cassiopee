K = int(input())
ans = 0
for _ in range(K):
    N, M = map(int, input().split())
    grundy0 = {0}
    grundy1 = {1}
    m = M
    while m // 2 >= N:
        if (m+1)//2%2:
            grundy_l = grundy0
        else:
            grundy_l = grundy1
        m, r = divmod(m, 2)
        if r==0:
            gr0 = grundy0
            grundy0 = {min({0, 1, 2} - grundy0 - grundy_l)}
            grundy1 = {0, 1, 2} - gr0 - grundy0
        else:
            grundy0 = {min({0, 1, 2} - grundy1 - grundy_l)}
            grundy1 = {0, 1, 2} - grundy1 - grundy0
        #print(grundy0, grundy1)
    grundy = grundy1 if (m-N)%2 else grundy0
    #print(grundy)
    ans ^= grundy.pop()
print("tubuann" if ans==0 else "mo3tthi")