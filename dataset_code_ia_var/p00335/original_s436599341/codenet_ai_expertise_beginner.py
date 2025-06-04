def solve():
    import sys
    f_i = sys.stdin

    N = int(f_i.readline())
    P = list(map(int, f_i.readline().split()))
    left = P[0]

    answer = N * 6

    for i in range(left + 1):
        temp_P = P[:]
        temp_P[0] -= i
        temp_answer = i

        for j in range(N - 1):
            count = temp_P[j]
            if count > 0:
                temp_P[j + 1] -= count
                temp_answer += 2 * count

        if temp_P[-1] > 0:
            temp_answer += temp_P[-1]

        if temp_answer < answer:
            answer = temp_answer

    print(answer)

solve()