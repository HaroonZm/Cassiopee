def d_atcodeer_and_rock_paper(S):
    return len(S) // 2 - S.count('p')

S = input().strip()
print(d_atcodeer_and_rock_paper(S))