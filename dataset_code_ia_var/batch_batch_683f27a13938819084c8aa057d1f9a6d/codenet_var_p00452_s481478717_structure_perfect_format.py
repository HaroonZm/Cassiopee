def input_score(N):
    score = []
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
            max_score = max(max_score, now_score)
            left += 1
        elif now_score > M:
            right -= 1
        else:
            max_score = M
            break
    return max_score

def cal_two_sum_score(score):
    two_score = []
    contain_sum = {}
    for i in range(len(score)):
        for j in range(len(score)):
            now_score = score[i] + score[j]
            if not contain_sum.get(now_score):
                contain_sum[now_score] = True
                two_score.append(now_score)
    two_score.sort()
    return two_score

def main():
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        score = input_score(N)
        two_score = cal_two_sum_score(score)
        max_score = cal_four_sum_score(two_score, M)
        print(max_score)

if __name__ == "__main__":
    main()