while True:
    morning = []
    afternoon = []
    for _ in range(5):
        a,b = map(int, input().split())
        if a==0 and b==0:
            exit()
        morning.append(a)
        afternoon.append(b)
    total = [m+a for m,a in zip(morning, afternoon)]
    shops = ['A','B','C','D','E']
    max_idx = total.index(max(total))
    print(shops[max_idx], total[max_idx])