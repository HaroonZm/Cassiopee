import sys

file_input = sys.stdin

for line in file_input:
    M, T, P, R = map(int, line.split())
    if M == 0:
        break
    result = [[0, M, i] + [0] * P for i in range(T + 1)]
    for i in range(R):
        m, t, p, j = map(int, file_input.readline().split())
        team_data = result[t]
        if j:
            team_data[-p] += 1
        else:
            team_data[0] += 1
            team_data[1] -= (m + 20 * team_data[-p])
    result.sort(reverse=True)
    for td1, td2 in zip(result[:-2], result[1:]):
        if td1[0] == td2[0] and td1[1] == td2[1]:
            print(td1[2], end='=')
        else:
            print(td1[2], end=',')
    print(result[-2][2])