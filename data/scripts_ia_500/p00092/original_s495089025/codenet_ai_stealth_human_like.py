# bon, ce code fait un truc with dp, je crois
table = [''] * 1002  
dp = [[0]*1002 for _ in range(1002)]  # matrice dp, un peu overkill en taille

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        table[i] = input()
    answer = 0
    
    for r in range(n):
        for c in range(n):
            if table[r][c] == '*':
                dp[r][c] = 0
            else:
                # on regarde en haut, à gauche, en haut-gauche, on prend le min +1
                t = dp[r-1][c-1]
                if dp[r][c-1] < t:
                    t = dp[r][c-1]
                if dp[r-1][c] < t:
                    t = dp[r-1][c]
                t += 1
                dp[r][c] = t
                if t > answer:
                    answer = t
    print(answer)