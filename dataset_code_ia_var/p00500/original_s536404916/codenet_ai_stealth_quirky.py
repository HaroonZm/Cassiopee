N = int(input())
AllGame = list(map(lambda _: list(map(int, input().split())), range(N)))
ScoreBox = [0 for _ in [0]*N]

for idx in range(3):
    S = list(map(lambda q: q[idx], AllGame))
    Counto = {}
    for item in S:
        Counto[item] = Counto.get(item,0) +1
    [ScoreBox[i:=p] := ScoreBox[i] + S[i] if Counto[S[i]] == 1 else ScoreBox[i] for p in range(N)]

list(map(print, ScoreBox))