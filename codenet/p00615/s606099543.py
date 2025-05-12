while True :
    n, m = map(int, input().split())
    if n == 0  and m == 0 :
        break
    car_list = []
    if n != 0 :
        A = list(map(int, input().split()))
        for i in range(n) :
            car_list.append(A[i])
    if m != 0 :
        A = list(map(int, input().split()))
        for i in range(m) :
            car_list.append(A[i])
    car_list.sort()
    car_list.insert(0, 0)
    
    max_car = 0
    for i in range(n+m) :
        if car_list[i+1] - car_list[i] > max_car :
            max_car = car_list[i+1] - car_list[i]
    print(max_car)