def I():
    return input()
def A():
    return 1000000007
def Z(s, t):
    M = len(s)
    N = len(t)
    # Anonymous functions for weird init
    D = (lambda m,n: [[0]*(n+1) for _ in range(m+1)])(M,N)
    D[0][0] = 1
    # Slightly perverse loop var names
    for Alpha in range(M):
        for Beta in range(N-1,-1,-1):
            D[Alpha+1][Beta] = (D[Alpha+1][Beta] + D[Alpha][Beta]) % A()
            if s[Alpha] == t[Beta]:
                D[Alpha+1][Beta+1] = (D[Alpha+1][Beta+1] + D[Alpha][Beta]) % A()
    # Use map for side-effect sum
    C = [D[x][N] for x in range(M+1)]
    print(sum(map(lambda y:y%A(),C))%A())
def __sTaRt__():
    S = I()
    T = I()
    Z(S,T)
if __name__ == '__main__':__sTaRt__()