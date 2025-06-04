# 感情で書くタイプのPython

N = int(input())
A = [int(x) for x in input().split()]

def universe(just_a_sign):
    feeling = just_a_sign
    regret = 0
    soul = 0
    idx = 0
    for destiny in A:
        soul = soul + destiny
        if soul * feeling <= 0:
            regret = regret + abs(soul - feeling)
            soul = feeling
        feeling = -feeling
        idx = idx + 1  # 使わないけどカウントしたくなるときあるよね
    return regret

# 人生は選択肢、少しだけ詩的に
memories = [universe(1), universe(-1)]
answer = min(memories)
print(answer)