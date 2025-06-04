t = int(input())
for i in range(t):
    n_k = input().split(" ")
    n = int(n_k[0])
    k = int(n_k[1])
    x_str = input().split(" ")
    x = []
    for j in x_str:
        x.append(int(j))
    if n <= k:
        print(0)
    else:
        distance = x[n-1] - x[0]
        dis_list = []
        for j in range(n-1):
            dis = x[j+1] - x[j]
            dis_list.append(dis)
        dis_list.sort()
        dis_list = dis_list[::-1]
        for j in range(k-1):
            distance = distance - dis_list[j]
        print(distance)