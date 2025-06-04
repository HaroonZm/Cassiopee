from sys import stdin as _s; I=input; del input
I=lambda:_s.readline().strip()

def main():
    S = I()
    M, Y = int(S[:2]), int(S[2:])
    # On va faire différemment
    mm, yy = [1 <= M <= 12, 1 <= Y <= 12]
    outcome = ("NA", "YYMM", "MMYY", "AMBIGUOUS")[(mm<<1)|yy]
    print(outcome if outcome!="NA" else outcome)

if __name__=="__main__":
    main()