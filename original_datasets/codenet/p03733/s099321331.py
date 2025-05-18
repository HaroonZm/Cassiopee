def resolve():
    '''
    code here
    '''
    N, T = [int(item) for item in input().split()]
    t_list = [int(item) for item in input().split()]
    time = 0

    for i in range(N):
        if i == 0:
            time = T
        else:
            delta_time = t_list[i] - t_list[i-1]
            time += min(T, delta_time)
            
    print(time)

if __name__ == "__main__":
    resolve()