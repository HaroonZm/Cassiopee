def input_score(N):
    score = []  # 的の配点をいれる配列、投げないときの点も入れておく
    score.append(0)
    for i in range(N):
        score.append(int(input()))
    return score

def cal_four_sum_score(two_score, M):
    left = 0
    right = len(two_score) - 1
    max_score = 0
    while left != right:
        now_score = two_score[left] + two_score[right]
        if now_score < M:
            # scoreの和がMより小さい時、解の候補である
            max_score = max(max_score, now_score)
            left += 1
        elif now_score > M:
            # scoreの和がMより大きい時、解の候補ではない
            right -= 1
        else:
            # scoreの和がちょうどMになるとき、解である
            max_score = M
            break

    return max_score

def cal_two_sum_score(score):
    two_score = []  # 二回投げた時に取りうる範囲を入れる配列
    contain_sum = {}  # 二回投げたときにその値はすでに存在するか判断する配列
    for i in range(len(score)):
        for j in range(len(score)):
            now_score = score[i] + score[j]
            if not contain_sum.get(now_score):
                contain_sum[now_score] = True
                two_score.append(now_score)

    two_score.sort()  # 尺取り法を用いるためsortしておく
    return two_score

def main():
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        score = input_score(N)  # 的の配点の入力
        two_score = cal_two_sum_score(score)  # 二回投げた時に取りうる点の範囲を計算
        max_score = cal_four_sum_score(two_score, M)  # 四回投げたときに取りうる点の範囲を計算
        print(max_score)

if __name__ == "__main__":
    main()