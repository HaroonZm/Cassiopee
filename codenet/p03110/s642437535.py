if __name__ == '__main__':
    N = int(input())

    xu_list = [list(map(str, input().split())) for i in range(N)]

    answer = 0
    for xu in xu_list:
        if xu[1] == 'JPY':
            answer += int(xu[0])
        elif xu[1] == 'BTC':
            answer += float(xu[0]) * 380000.0

    print(answer)