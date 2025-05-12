#import sys
#input = sys.stdin.readline
def main():
    N, s, t = map( int, input().split())
    if N <= 2:
        print("! " + str(s) + " " +str(t))
        return
    print("? "+ str(s) + " " + str(t))
    d = int( input())
    D = [(0, 0) for _ in range(N)]
    for i in range(N):
        print("? " + str(s) + " " + str(i+1), flush=True)
        D[i] = ( int( input()), i+1)
    D.sort()
    F = [0]*(N+1)
    for i in range(1, N+1):
        print("? " + str(t) + " " + str(i), flush = True)
        F[i] = int( input())
    ANS = [s]
    now = 0
    for i in range(1, N):
        if D[i][0] == d:
            ANS.append(t)
            break
        if now == D[i][0]:
            continue
        if D[i][0] + F[D[i][1]] == d:
            ANS.append(D[i][1])
            now = D[i][0]
    print("! " + " ".join( map( str, ANS)))
if __name__ == '__main__':
    main()