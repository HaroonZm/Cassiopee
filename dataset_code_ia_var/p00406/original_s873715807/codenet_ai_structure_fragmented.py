def read_n_l():
    return list(map(int, input().split()))

def read_p_d():
    return list(map(int, input().split()))

def gather_initial_data():
    N, L = read_n_l()
    c = collect_p_d(N)
    return N, L, c

def collect_p_d(N):
    data = []
    for _ in range(N):
        data.append(tuple(read_p_d()))
    return data

def sort_c(c):
    return sorted(c)

def extract_masu(c):
    return [p for p, d in c]

def extract_dir(c):
    return [d for p, d in c]

def calculate_initial_score(N, masu, dir):
    score = 0
    for j in range(N):
        score = update_score_forward(score, j, masu, dir)
        masu[j] = j + 1
    return score

def update_score_forward(score, j, masu, dir):
    if dir[j] == 0:
        score += masu[j] - j - 1
    elif dir[j] == 1:
        score -= masu[j] - j - 1
    return score

def calculate_result(N, L, masu, dir, initial_score):
    score = initial_score
    result = score
    for i in range(N-1, -1, -1):
        score = update_score_backward(score, i, N, L, masu, dir)
        masu[i] = L - (N - i) + 1
        result = update_result(result, score)
    return result

def update_score_backward(score, i, N, L, masu, dir):
    if dir[i] == 1:
        score += L - (N - i) - masu[i] + 1
    elif dir[i] == 0:
        score -= L - (N - i) - masu[i] + 1
    return score

def update_result(result, score):
    return max(result, score)

def main():
    N, L, c = gather_initial_data()
    c = sort_c(c)
    masu = extract_masu(c)
    dir = extract_dir(c)
    initial_score = calculate_initial_score(N, masu, dir)
    result = calculate_result(N, L, masu, dir, initial_score)
    print(result)

main()